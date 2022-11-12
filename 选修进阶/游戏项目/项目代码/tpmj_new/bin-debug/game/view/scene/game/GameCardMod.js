var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Tpm;
(function (Tpm) {
    /**
     * 麻将牌显示逻辑相关模块
     */
    var GameCardMod = (function (_super) {
        __extends(GameCardMod, _super);
        function GameCardMod() {
            var _this = _super.call(this) || this;
            _this.dragCardValue = 0;
            _this.skinName = TpmSkin.GameCardModSkin;
            return _this;
        }
        GameCardMod.prototype.childrenCreated = function () {
            this.initDb();
        };
        GameCardMod.prototype.onEnable = function () {
            this.cardTestGro && (this.cardTestGro.visible = false);
            this.initList();
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouchTap, this);
            this.addEventListener(egret.TouchEvent.TOUCH_BEGIN, this.onTouchBegin, this);
            /** test ------------------*/
            // this.testOut(UserPosition.Down);
            // this.testOut(UserPosition.Up);
            // for (var i = 0;i < this.handCardList[UserPosition.Down].length; i ++) {
            //     this.handCardList[UserPosition.Down][i].setBack(true);
            // }
            // this.testHand(UserPosition.Down);
            /** test ----------------*/
            // this.dealCardShow([23,24,19,18,17,18,19,19,19,19,20,21,22]);
        };
        GameCardMod.prototype.onRemove = function () {
        };
        /**本家是否有摸牌 */
        GameCardMod.prototype.getOwnMoFlag = function () {
            if (this.moCardList[Tpm.UserPosition.Down][0]) {
                return true;
            }
            return false;
        };
        /**
         * 牌模块点击监听，主要用于牌点击
         */
        GameCardMod.prototype.onTouchTap = function (e) {
            var target = e.target;
            console.log("ontouch--------");
            // 手牌点击
            if (target instanceof Tpm.Card) {
                target;
                if (target.userPos == Tpm.UserPosition.Up || target.parent != this.cardGro) {
                    console.log("target error==", target);
                    return;
                }
                if (Tpm.App.DataCenter.runingData.bAllowOutCard) {
                    if (target.bUp) {
                        if (target.arrowState) {
                            // 发送听牌
                            this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_Ting, [target.cardValue]);
                        }
                        else {
                            // 发送出牌
                            this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_Out, [target.cardValue]);
                        }
                    }
                    else {
                        this.drownAllHandCard();
                        target.toUp();
                    }
                }
                else {
                    if (target.bUp) {
                        target.toDown();
                    }
                    else {
                        this.drownAllHandCard();
                        target.toUp();
                    }
                }
                if (target.arrowState && target.bUp) {
                    // 显示胡牌提示
                    var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
                    console.log("听牌数据：", data);
                    var tingList = [];
                    for (var key in data.act_info[Tpm.ACT_state.Act_Ting][target.cardValue]) {
                        var item = {
                            outCardValue: Number(key),
                            fanNum: data.act_info[Tpm.ACT_state.Act_Ting][target.cardValue][key].fan,
                            residueNum: this.gameScene.cardMod.getCardResidue(Number(key))
                        };
                        tingList.push(item);
                        /**test */
                        var huList = data.act_info[Tpm.ACT_state.Act_Ting][target.cardValue][key].type_list;
                        var str = "";
                        for (var i = 0; i < huList.length; i++) {
                            str += Tpm.HuType.HuTypeName[huList[i]];
                            str += ";";
                        }
                        console.log(Tpm.CardName.Name[key] + ":" + str);
                    }
                    this.gameScene.huTipsMod.showHuTips(tingList, target.cardValue);
                }
            }
        };
        /**开始点击 */
        GameCardMod.prototype.onTouchBegin = function (e) {
            if (e.target instanceof Tpm.Card) {
                var target = e.target;
                if (target.parent == this.cardGro && !target.arrowState) {
                    this.curTouchCard = target;
                    this.dragCardValue = target.cardValue;
                    Tpm.App.LayerManager.RootLayer.addEventListener(egret.TouchEvent.TOUCH_MOVE, this.onDragMove, this);
                    Tpm.App.LayerManager.RootLayer.addEventListener(egret.TouchEvent.TOUCH_END, this.onDragEnd, this);
                }
            }
        };
        GameCardMod.prototype.onDragMove = function (e) {
            if (this.dragCardValue != 0) {
                if (this.dragMoveCard == null && e.stageY < Tpm.CardPos.handCardPosYlist[Tpm.UserPosition.Down]) {
                    this.dragMoveCard = this.cardFactory.getHandCard(this.dragCardValue, Tpm.UserPosition.Down);
                    this.movieGro.addChild(this.dragMoveCard);
                }
                if (this.dragMoveCard) {
                    this.dragMoveCard.x = e.stageX - this.dragMoveCard.width / 2;
                    this.dragMoveCard.y = e.stageY - this.dragMoveCard.height / 2;
                }
            }
        };
        /**
         * 释放牌的拖拽
         */
        GameCardMod.prototype.onDragEnd = function (e) {
            this.dragCardValue = 0;
            if (!this.dragMoveCard) {
                return;
            }
            var dragCardValue = this.dragMoveCard.cardValue;
            this.clearDragCard();
            if (Tpm.App.DataCenter.runingData.bAllowOutCard && e.stageY < Tpm.CardPos.handCardPosYlist[Tpm.UserPosition.Down]) {
                this.curTouchOutCard = this.curTouchCard;
                // 发送出牌
                this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_Out, [this.curTouchOutCard.cardValue]);
            }
        };
        //清理拖拽牌
        GameCardMod.prototype.clearDragCard = function () {
            Tpm.App.LayerManager.RootLayer.removeEventListener(egret.TouchEvent.TOUCH_MOVE, this.onDragMove, this);
            Tpm.App.LayerManager.RootLayer.removeEventListener(egret.TouchEvent.TOUCH_END, this.onDragEnd, this);
            this.dragCardValue = 0;
            if (this.dragMoveCard) {
                this.dragMoveCard.recycle();
                this.dragMoveCard = null;
            }
        };
        GameCardMod.prototype.testOut = function (pos) {
            var testList = [17, 18, 19, 20, 22, 23, 24, 53, 54, 55];
            for (var i = 0; i < testList.length; i++) {
                var card = this.cardFactory.getOutCard(testList[i], pos);
                this.addCardToOut(card, pos);
            }
        };
        GameCardMod.prototype.testHand = function (pos) {
            var testList = [66, 67, 81, 82, 97, 102, 104];
            for (var i = 0; i < testList.length; i++) {
                var card = this.cardFactory.getHandCard(testList[i], pos, Tpm.App.DataCenter.runingData.ownTingState);
                this.addCardToHand(card, pos);
            }
        };
        GameCardMod.prototype.testChi = function (pos) {
            var testList = [23, 23, 23];
            this.addCardToEat(testList, pos);
        };
        GameCardMod.prototype.testGang = function (pos, ang) {
            if (ang === void 0) { ang = false; }
            var testList = [23, 23, 23, 24];
            this.addCardToGang(testList, pos, ang);
        };
        GameCardMod.prototype.testMo = function (pos) {
            var cardValue = 0;
            cardValue = pos ? 0 : 53;
            var card = this.cardFactory.getHandCard(cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);
        };
        /**
         * 发牌
         */
        GameCardMod.prototype.dealCardShow = function (downCardValueList) {
            var handLen = 13;
            var upCardValueList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            for (var i = 0; i < handLen; i++) {
                var cardDown = this.cardFactory.getHandCard(downCardValueList[i], Tpm.UserPosition.Down);
                this.addCardToHand(cardDown, Tpm.UserPosition.Down);
                cardDown.visible = false;
                var cardUp = this.cardFactory.getHandCard(upCardValueList[i], Tpm.UserPosition.Up);
                this.addCardToHand(cardUp, Tpm.UserPosition.Up);
                cardUp.visible = false;
            }
            for (var i = 0; i < 4; i++) {
                this.delayShowAGroup(i, Tpm.UserPosition.Down);
                this.delayShowAGroup(i, Tpm.UserPosition.Up);
            }
        };
        /**
         * 分组发牌动画
         */
        GameCardMod.prototype.delayShowAGroup = function (groIndex, pos) {
            var _this = this;
            // var delay = 500;
            var delay = 900;
            var handLen = 13;
            if (pos == Tpm.UserPosition.Down) {
                // setTimeout(() => {
                //     for (var i = 4 * groIndex; i < 4 * groIndex + 4; i++) {
                //         if (i >= handLen) {
                //             break;
                //         }
                //         var card: Card = this.handCardList[pos][i];
                //         card.y = card.initY + CardPos.moCardOffsetY[pos];
                //         card.visible = true;
                //         var localI = i;
                //         egret.Tween.get(card).wait(200).to({ y: card.initY }, 50).call(() => {
                //             egret.Tween.removeTweens(card);
                //             if (localI == handLen - 1) {
                //                 this.downCardBackSHow();
                //             }
                //         }, this);
                //     }
                // }, delay * groIndex, this)
                setTimeout(function () {
                    for (var i = 4 * groIndex; i < 4 * groIndex + 4; i++) {
                        if (i >= handLen) {
                            break;
                        }
                        var card = _this.handCardList[pos][i];
                        card.setBack(true);
                        _this.showFanDb(i);
                        var localI = i;
                        egret.setTimeout(function () {
                            if (localI == handLen - 1) {
                                egret.setTimeout(function () {
                                    _this.downCardBackSHow();
                                }, _this, 200);
                            }
                            for (var j = i - 1; j > i - 4 - 1; j--) {
                                if (!_this.handCardList[pos][j]) {
                                    break;
                                }
                                _this.handCardList[pos][j].setBack(false);
                                _this.handCardList[pos][j].visible = true;
                            }
                        }, _this, 730);
                    }
                }, delay * groIndex, this);
            }
            else {
                setTimeout(function () {
                    for (var i = handLen - 1 - 4 * groIndex; i > handLen - 1 - 4 * groIndex - 4; i--) {
                        if (i < 0) {
                            break;
                        }
                        var card = _this.handCardList[pos][i];
                        card.y = card.initY + Tpm.CardPos.moCardOffsetY[pos];
                        card.visible = true;
                        egret.Tween.get(card).wait(200).to({ y: card.initY }, 50);
                    }
                }, delay * groIndex, this);
            }
        };
        /**
         * 下家手牌盖牌动画
         */
        GameCardMod.prototype.downCardBackSHow = function () {
            var _this = this;
            for (var i = 0; i < this.handCardList[Tpm.UserPosition.Down].length; i++) {
                var handCard = this.handCardList[Tpm.UserPosition.Down][i];
                handCard.setBack(true);
                handCard.visible = false;
            }
            // 发牌补花
            this.dealCardBuHua();
            // 排序,重新排位置
            Tpm.CardLogic.getInstance().sortHandCardAB(this.handCardList[Tpm.UserPosition.Down]);
            for (var i = 0; i < this.handCardList[Tpm.UserPosition.Down].length; i++) {
                this.handCardList[Tpm.UserPosition.Down][i].x = Tpm.CardPos.handCardPosXList[Tpm.UserPosition.Down] + i * Tpm.CardPos.handCardGapList[Tpm.UserPosition.Down];
            }
            for (var i = 0; i < 13; i++) {
                this.showFanDb(i);
            }
            setTimeout(function () {
                for (var i = 0; i < _this.handCardList[Tpm.UserPosition.Down].length; i++) {
                    var handCard = _this.handCardList[Tpm.UserPosition.Down][i];
                    handCard.setBack(false);
                    handCard.visible = true;
                }
                // 首发牌
                _this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_Fa, []);
                // 处理发牌阶段可能触发的动作
                Tpm.App.DataCenter.MsgCache.exeMsg(Tpm.ProtocolHeadRev.R_101001, false);
                Tpm.App.DataCenter.runingData.gameState = Tpm.GameState.Playing;
            }, 740, this);
        };
        /**
         * 发牌补花
         */
        GameCardMod.prototype.dealCardBuHua = function () {
            var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101008);
            if (!data) {
                return;
            }
            for (var i = 0; i < data.length; i++) {
                // 本家补花
                if (data[i].seat_id == Tpm.App.DataCenter.UserInfo.myUserInfo.seatID) {
                    this.gameScene.dbMod.showActDb(Tpm.ACT_state.Act_Buhua, Tpm.UserPosition.Down);
                    this.gameScene.flowerMod.setFlowerState(Tpm.UserPosition.Down, data[i].hua_card.length);
                    for (var k = 0; k < data[i].hua_card.length; k++) {
                        for (var j = 0; j < this.handCardList[Tpm.UserPosition.Down].length; j++) {
                            if (this.handCardList[Tpm.UserPosition.Down][j].cardValue == data[i].hua_card[k]) {
                                this.handCardList[Tpm.UserPosition.Down][j].setCardValueAndSHow(data[i].bu_cards[k]);
                            }
                        }
                    }
                }
                else {
                    this.gameScene.dbMod.showActDb(Tpm.ACT_state.Act_Buhua, Tpm.UserPosition.Up);
                    this.gameScene.flowerMod.setFlowerState(Tpm.UserPosition.Up, data[i].hua_card.length);
                }
            }
        };
        /**
         * 摸牌补花
         */
        GameCardMod.prototype.moCardBuHua = function (pos) {
            var _this = this;
            this.gameScene.dbMod.showActDb(Tpm.ACT_state.Act_Buhua, pos);
            if (!this.moCardList[pos][0]) {
                console.error("mo card error");
                return;
            }
            if (this.moCardList[pos][0].cardValue > 96) {
                egret.Tween.get(this.moCardList[pos][0])
                    .to({ alpha: 0.8 }, 500)
                    .to({ alpha: 0 }, 200)
                    .call(function () {
                    egret.Tween.removeTweens(_this.moCardList[pos][0]);
                });
            }
        };
        /**
         * 摸牌
         */
        GameCardMod.prototype.moCardShow = function (cardValue, pos) {
            if (this.moCardList[pos][0]) {
                this.moCardList[pos][0].recycle();
                this.moCardList[pos].pop();
            }
            var moCard = this.cardFactory.getHandCard(cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            this.addCardToMo(moCard, pos);
            moCard.visible = false;
            var movieMoCard = this.cardFactory.getHandCard(cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            movieMoCard.x = moCard.x;
            movieMoCard.y = moCard.y + Tpm.CardPos.moCardOffsetY[pos];
            this.movieGro.addChild(movieMoCard);
            if (pos == Tpm.UserPosition.Down && Tpm.App.DataCenter.runingData.ownTingState) {
                moCard.setGray(true);
                movieMoCard.setGray(true);
            }
            egret.Tween.get(movieMoCard)
                .wait(200)
                .to({ y: this.moCardList[pos][0].initY }, 50)
                .call(function () {
                moCard.visible = true;
                movieMoCard && movieMoCard.parent && movieMoCard.parent.removeChild(movieMoCard);
                egret.Tween.removeTweens(movieMoCard);
            });
        };
        /**
         * 出牌
         */
        GameCardMod.prototype.outCardShow = function (pos, cardValue) {
            var _this = this;
            if (pos === void 0) { pos = Tpm.UserPosition.Down; }
            if (cardValue === void 0) { cardValue = 0; }
            var handleCard;
            if (this.moCardList[pos][0].cardValue == cardValue) {
                handleCard = this.moCardList[pos][0];
            }
            else if (pos == Tpm.UserPosition.Up && (Tpm.App.DataCenter.runingData.curentRoomType == Tpm.RoomType.noob || !Tpm.App.DataCenter.runingData.ownTingState)) {
                handleCard = this.moCardList[pos][0];
            }
            else {
                for (var i = 0; i < this.handCardList[pos].length; i++) {
                    if (this.handCardList[pos][i].cardValue == cardValue) {
                        handleCard = this.handCardList[pos][i];
                        break;
                    }
                }
            }
            if (!handleCard) {
                console.error("out card null");
                return;
            }
            var tCardValue = handleCard.cardValue || cardValue;
            if (pos == Tpm.UserPosition.Up) {
                tCardValue = cardValue;
            }
            var outCard = this.cardFactory.getOutCard(tCardValue, pos);
            this.addCardToOut(outCard, pos);
            outCard.visible = false;
            var movieSmallCard = this.cardFactory.getOutCard(tCardValue, pos);
            movieSmallCard.x = handleCard.x;
            movieSmallCard.y = handleCard.y + Tpm.CardPos.moCardOffsetY[pos];
            this.movieGro.addChild(movieSmallCard);
            var moFlag = false;
            // 牌回收，数组更新
            if (handleCard == this.moCardList[pos][0]) {
                handleCard.recycle();
                this.moCardList[pos].pop();
                moFlag = true;
            }
            else {
                for (var i = 0; i < this.handCardList[pos].length; i++) {
                    if (this.handCardList[pos][i] == handleCard) {
                        handleCard.recycle();
                        this.handCardList[pos].splice(i, 1);
                        break;
                    }
                }
                moFlag = false;
            }
            this.drownAllHandCard();
            // 动画
            egret.Tween.get(movieSmallCard)
                .to({ x: outCard.x, y: outCard.y }, 200)
                .call(function () {
                movieSmallCard && movieSmallCard.parent && movieSmallCard.parent.removeChild(movieSmallCard);
                outCard.visible = true;
                if (!moFlag) {
                    _this.moveMoCardToHand(pos);
                }
            }, this);
        };
        /**
         * 摸牌移动到手牌指定位置
         */
        GameCardMod.prototype.moveMoCardToHand = function (pos) {
            var _this = this;
            if (pos === void 0) { pos = Tpm.UserPosition.Down; }
            var offsetYList = [-130, -10];
            var tMoCard = this.moCardList[pos][0];
            if (!tMoCard) {
                console.error("have not mocard");
                return;
            }
            var tHandCard = this.cardFactory.getHandCard(tMoCard.cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            this.addCardToHand(tHandCard, pos);
            tHandCard.visible = false;
            if (Tpm.App.DataCenter.runingData.ownTingState && pos == Tpm.UserPosition.Down) {
                tHandCard.setGray(true);
            }
            var movieCard = this.cardFactory.getHandCard(tMoCard.cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            movieCard.x = tMoCard.x;
            movieCard.y = tMoCard.y;
            this.movieGro.addChild(movieCard);
            if (Tpm.App.DataCenter.runingData.ownTingState && pos == Tpm.UserPosition.Down) {
                movieCard.setGray(true);
            }
            tMoCard.recycle();
            this.moCardList[pos].pop();
            egret.Tween.get(movieCard)
                .to({ y: tHandCard.initY + offsetYList[pos] }, 100)
                .call(function () {
                // 排列手牌
                _this.reHandCardPos(pos);
                egret.Tween.get(movieCard)
                    .to({ x: tHandCard.x }, 200)
                    .to({ y: tHandCard.initY }, 100)
                    .call(function () {
                    tHandCard.visible = true;
                    movieCard && movieCard.parent && movieCard.parent.removeChild(movieCard);
                }, _this);
            }, this);
        };
        /**吃牌,碰牌操作 */
        GameCardMod.prototype.eatCardShow = function (cardValueList, pos, pengFlag) {
            if (pengFlag === void 0) { pengFlag = false; }
            var eatLen = 3;
            var rPos = 0;
            if (pos == 0) {
                rPos = 1;
            }
            this.removeLastOutCard(rPos);
            this.addCardToEat(cardValueList, pos, pengFlag);
            if (pos == Tpm.UserPosition.Down || (Tpm.App.DataCenter.runingData.ownTingState && Tpm.App.DataCenter.runingData.guoHuFlag)) {
                for (var i = 0; i < cardValueList.length; i++) {
                    if (cardValueList[i] == Tpm.App.DataCenter.runingData.latelyCardValue) {
                        cardValueList.splice(i, 1);
                        break;
                    }
                }
                for (var i = 0; i < cardValueList.length; i++) {
                    this.deletHandCard(cardValueList[i], pos);
                }
            }
            else {
                for (var i = eatLen; i > 1; i--) {
                    this.handCardList[pos][this.handCardList[pos].length - 1].recycle();
                    this.handCardList[pos].pop();
                }
            }
            var card = this.cardFactory.getHandCard(this.handCardList[pos][this.handCardList[pos].length - 1].cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);
            this.handCardList[pos][this.handCardList[pos].length - 1].recycle();
            this.handCardList[pos].pop();
            this.reHandCardPos(pos);
        };
        /**杠牌操作 */
        GameCardMod.prototype.gangCardShow = function (gangType, cardValue, pos) {
            var gangLen = 4;
            var angFlag = false;
            if (gangType == Tpm.ACT_state.Act_AnGang) {
                angFlag = true;
            }
            // 添加到杠牌
            if (gangType == Tpm.ACT_state.Act_BuGang) {
                this.addCardToBu(cardValue, pos);
            }
            else {
                var list = [];
                for (var i = 0; i < gangLen; i++) {
                    list.push(cardValue);
                }
                this.addCardToGang(list, pos, angFlag);
            }
            // 移除牌
            if (gangType == Tpm.ACT_state.Act_Gang) {
                var rPos = 0;
                if (pos == 0) {
                    rPos = 1;
                }
                this.removeLastOutCard(rPos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
            }
            else if (gangType == Tpm.ACT_state.Act_BuGang) {
                this.deletHandCard(cardValue, pos);
                if (this.moCardList[pos].length > 0) {
                    this.handCardList[pos].push(this.moCardList[pos][0]);
                    this.moCardList[pos] = [];
                }
            }
            else {
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
                if (this.moCardList[pos].length > 0) {
                    this.handCardList[pos].push(this.moCardList[pos][0]);
                    this.moCardList[pos] = [];
                }
            }
            this.reHandCardPos(pos);
        };
        /**捉炮时，手牌和对家出牌的处理 */
        GameCardMod.prototype.dianHuCardShow = function (cardValue, pos) {
            var card = this.cardFactory.getHandCard(cardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);
            var rPos = 0;
            if (pos == 0) {
                rPos = 1;
            }
            this.removeLastOutCard(rPos);
            if (cardValue != this.moCardList[pos][0].cardValue) {
                console.error("dianHu card error");
            }
        };
        GameCardMod.prototype.testHu = function (pos, list) {
            if (list === void 0) { list = null; }
            var testList = [66, 67, 81, 82, 97, 102, 104];
            var list = list || testList;
            for (var i = 0; i < list.length; i++) {
                this.addCardToHu(list[i], pos);
            }
        };
        /**清理牌相关动画GRO, 切换前后台时调用 */
        GameCardMod.prototype.clearCardMovieGro = function () {
            this.movieGro.removeChildren();
        };
        /**点击听牌后界面变化 */
        GameCardMod.prototype.tingCardShow = function () {
            this.drownAllHandCard();
            var pos = Tpm.UserPosition.Down;
            var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
            var tingValueList = [];
            for (var key in data.act_info[Tpm.ACT_state.Act_Ting]) {
                tingValueList.push(Number(key));
            }
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                var grayFlag = true;
                for (var j = 0; j < tingValueList.length; j++) {
                    if (this.handCardList[pos][i].cardValue == tingValueList[j]) {
                        this.handCardList[pos][i].setArrow(true);
                        grayFlag = false;
                        break;
                    }
                }
                this.handCardList[pos][i].setGray(grayFlag);
            }
            var moFlag = false;
            for (var i = 0; i < tingValueList.length; i++) {
                if (tingValueList[i] == this.moCardList[pos][0].cardValue) {
                    moFlag = true;
                }
            }
            this.moCardList[pos][0].setGray(true);
            if (moFlag) {
                this.moCardList[pos][0].setGray(false);
                this.moCardList[pos][0].setArrow(true);
            }
        };
        /**听牌完成后牌变化 */
        GameCardMod.prototype.tingDidShow = function (handList) {
            var pos = Tpm.UserPosition.Down;
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                this.handCardList[pos][i].setArrow(false);
                this.handCardList[pos][i].setGray(true);
            }
            this.moCardList[pos][0].setArrow(false);
            this.moCardList[pos][0].setGray(true);
            this.tingDidCardShow(handList);
        };
        /**高级场听牌时对家牌处理 */
        GameCardMod.prototype.tingDidCardShow = function (handList) {
            if (Tpm.App.DataCenter.runingData.curentRoomType != Tpm.RoomType.noob && Tpm.App.DataCenter.runingData.ownTingState) {
                var pos = Tpm.UserPosition.Up;
                var tHandList = handList[Tpm.App.DataCenter.UserInfo.getUserByPos(pos).seatID].hand_card;
                for (var i = 0; i < tHandList.length; i++) {
                    var tCardValue = tHandList[i];
                    tCardValue && this.handCardList[pos][i].setHandSkin(tCardValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
                }
            }
        };
        /**取消听牌时的处理 */
        GameCardMod.prototype.tingCancleShow = function () {
            var pos = Tpm.UserPosition.Down;
            this.drownAllHandCard();
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                this.handCardList[pos][i].setArrow(false);
                this.handCardList[pos][i].setGray(false);
            }
            this.moCardList[pos][0].setArrow(false);
            this.moCardList[pos][0].setGray(false);
        };
        /**胡牌时手牌推倒 */
        GameCardMod.prototype.huCardShow = function (pos, huCardValueList) {
            var listLen = huCardValueList.length;
            if (!listLen) {
                console.error("game over handcard error");
                return;
            }
            for (var i = 0; i < huCardValueList[listLen - 2].length; i++) {
                this.addCardToHu(huCardValueList[listLen - 2][i], pos);
            }
            if (huCardValueList[listLen - 1].length > 0) {
                this.addCardToHu(huCardValueList[listLen - 1][0], pos, true);
            }
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                this.handCardList[pos][i].recycle();
            }
            this.handCardList[pos] = [];
            if (this.moCardList[pos][0]) {
                this.moCardList[pos][0].recycle();
                this.moCardList[pos] = [];
            }
            // Up暗杠处理
            if (pos == Tpm.UserPosition.Up) {
                var gangList = [];
                for (var i = 0; i < huCardValueList.length; i++) {
                    if (huCardValueList[i].length == 4 && huCardValueList[i][1] == 0) {
                        gangList.push(huCardValueList[i][0]);
                    }
                }
                if (gangList.length < 1) {
                    return;
                }
                console.log("this.angCardList[pos]======", this.angCardList[pos]);
                for (var i = 0; i < this.angCardList[pos].length / 4; i++) {
                    var oriCard = this.angCardList[pos][i * 4 + 3];
                    var card = this.cardFactory.getEatCard(gangList[i], pos);
                    card.x = oriCard.x;
                    card.y = oriCard.y;
                    this.cardGro.addChild(card);
                    oriCard.recycle();
                    this.angCardList[pos][i * 4 + 3] = card;
                }
            }
        };
        /**重连时的牌处理 */
        GameCardMod.prototype.reConnectCardShow = function (pos, orderCardList, lastValue, outCardList) {
            var handList;
            for (var i = 0; i < orderCardList.length; i++) {
                var itemList = Tpm.ArrayTool.deepCopy(orderCardList[i]);
                var itemLen = itemList.length;
                if (i == orderCardList.length - 1) {
                    if (itemLen > 0) {
                        var card = this.cardFactory.getHandCard(itemList[0], pos, Tpm.App.DataCenter.runingData.ownTingState);
                        this.addCardToMo(card, pos);
                    }
                }
                else if (i == orderCardList.length - 2) {
                    handList = itemList;
                }
                else if (itemLen == 3) {
                    if (itemList[0] == itemList[1]) {
                        this.addCardToEat(itemList, pos, true);
                    }
                    else {
                        this.addCardToEat(itemList, pos, false);
                    }
                }
                else if (itemLen == 4) {
                    if (itemList[1] == 0) {
                        itemList[3] = itemList[0];
                        itemList[0] = 0;
                        this.addCardToGang(itemList, pos, true);
                    }
                    else {
                        this.addCardToGang(itemList, pos, false);
                    }
                }
            }
            if (handList.length % 3 == 2) {
                var moFlag = true;
                for (var i = 0; i < handList.length; i++) {
                    if (handList[i] == lastValue) {
                        moFlag = false;
                        var card = this.cardFactory.getHandCard(lastValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
                        this.addCardToMo(card, pos);
                        handList.splice(i, 1);
                        if (pos == Tpm.UserPosition.Down && Tpm.App.DataCenter.runingData.ownTingState) {
                            card.setGray(true);
                        }
                        break;
                    }
                }
                // 如果最后一张操作牌找不到
                if (moFlag) {
                    var tLastValue = handList[handList.length - 1];
                    var card = this.cardFactory.getHandCard(tLastValue, pos, Tpm.App.DataCenter.runingData.ownTingState);
                    this.addCardToMo(card, pos);
                    handList.splice(handList.length - 1, 1);
                    if (pos == Tpm.UserPosition.Down && Tpm.App.DataCenter.runingData.ownTingState) {
                        card.setGray(true);
                    }
                }
            }
            for (var i = 0; i < handList.length; i++) {
                var card = this.cardFactory.getHandCard(handList[i], pos, Tpm.App.DataCenter.runingData.ownTingState);
                this.addCardToHand(card, pos);
                if (pos == Tpm.UserPosition.Down && Tpm.App.DataCenter.runingData.ownTingState) {
                    card.setGray(true);
                }
            }
            for (var i = 0; i < outCardList.length; i++) {
                var card = this.cardFactory.getOutCard(outCardList[i], pos);
                this.addCardToOut(card, pos);
            }
        };
        return GameCardMod;
    }(Tpm.CardModBase));
    Tpm.GameCardMod = GameCardMod;
    __reflect(GameCardMod.prototype, "Tpm.GameCardMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameCardMod.js.map