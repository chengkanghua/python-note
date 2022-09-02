module Tpm {
    /**
     * 麻将牌显示逻辑相关模块
     */
    export class GameCardMod extends CardModBase {
        protected cardGro: eui.Group;
        protected outGro:eui.Group;
        protected movieGro: eui.Group;
        protected dbGro: eui.Group;
        private cardTestGro: eui.Group;

        //----------延时相关配置--------

        //-------------其他------------
        private dragMoveCard: Card;
        private dragCardValue: number = 0;
        /**记录拖拽的牌 */
        private curTouchCard: Card;
        /**记录拖拽并触发出牌的牌 */
        private curTouchOutCard: Card;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameCardModSkin;
        }

        protected childrenCreated() {
            this.initDb();
        }

        protected onEnable() {
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
        }

        protected onRemove() {

        }

        /**本家是否有摸牌 */
        public getOwnMoFlag():boolean {
            if (this.moCardList[UserPosition.Down][0]) {
                return true;
            }
            return false;
        }

        /**
         * 牌模块点击监听，主要用于牌点击
         */
        private onTouchTap(e: egret.TouchEvent) {
            var target = e.target;
            console.log("ontouch--------");
            // 手牌点击
            if (target instanceof Card) {
                target as Card;
                if (target.userPos == UserPosition.Up || target.parent != this.cardGro) {
                    console.log("target error==", target);
                    return;
                }

                if (App.DataCenter.runingData.bAllowOutCard) {
                    if (target.bUp) {
                        if (target.arrowState) {
                            // 发送听牌
                            this.ctrl.sendMod.sendAct(ACT_state.Act_Ting, [target.cardValue]);
                        }
                        else {
                            // 发送出牌
                            this.ctrl.sendMod.sendAct(ACT_state.Act_Out, [target.cardValue]);
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
                    var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
                    console.log("听牌数据：", data);
                    var tingList = [];
                    for (var key in data.act_info[ACT_state.Act_Ting][target.cardValue]) {
                        var item = {
                            outCardValue: Number(key),
                            fanNum: data.act_info[ACT_state.Act_Ting][target.cardValue][key].fan,
                            residueNum: this.gameScene.cardMod.getCardResidue(Number(key))
                        }
                        tingList.push(item);

                        /**test */
                        var huList = data.act_info[ACT_state.Act_Ting][target.cardValue][key].type_list;
                        var str = "";
                        for (var i = 0;i < huList.length;i ++) {
                            str += HuType.HuTypeName[huList[i]];
                            str += ";";
                        }
                        console.log(CardName.Name[key]+":" + str);
                    }
                    
                    this.gameScene.huTipsMod.showHuTips(tingList, target.cardValue);
                }
            }
        }

        /**开始点击 */
        private onTouchBegin(e: egret.TouchEvent) {
            if (e.target instanceof Card) {
                var target:Card = e.target;
                if (target.parent == this.cardGro && !target.arrowState) {
                    this.curTouchCard = target;
                    this.dragCardValue = target.cardValue;
                    App.LayerManager.RootLayer.addEventListener(egret.TouchEvent.TOUCH_MOVE, this.onDragMove, this);
                    App.LayerManager.RootLayer.addEventListener(egret.TouchEvent.TOUCH_END, this.onDragEnd, this);
                }
            }
        }

        private onDragMove(e: egret.TouchEvent) {
            if (this.dragCardValue != 0) {
                if (this.dragMoveCard == null && e.stageY < CardPos.handCardPosYlist[UserPosition.Down]) {
                    this.dragMoveCard = this.cardFactory.getHandCard(this.dragCardValue, UserPosition.Down);
                    this.movieGro.addChild(this.dragMoveCard);
                }
                if (this.dragMoveCard) {
                    this.dragMoveCard.x = e.stageX - this.dragMoveCard.width / 2;
                    this.dragMoveCard.y = e.stageY - this.dragMoveCard.height / 2;
                }
            }
        }

        /**
         * 释放牌的拖拽
         */
        private onDragEnd(e: egret.TouchEvent) {
            this.dragCardValue = 0;
            if (!this.dragMoveCard) {
                return;
            }

            var dragCardValue = this.dragMoveCard.cardValue;
            this.clearDragCard();

            if (App.DataCenter.runingData.bAllowOutCard && e.stageY < CardPos.handCardPosYlist[UserPosition.Down]) {
                this.curTouchOutCard = this.curTouchCard;

                // 发送出牌
                this.ctrl.sendMod.sendAct(ACT_state.Act_Out, [this.curTouchOutCard.cardValue]);
            }
        }

        //清理拖拽牌
        private clearDragCard() {
            App.LayerManager.RootLayer.removeEventListener(egret.TouchEvent.TOUCH_MOVE, this.onDragMove, this);
            App.LayerManager.RootLayer.removeEventListener(egret.TouchEvent.TOUCH_END, this.onDragEnd, this);
            this.dragCardValue = 0;
            if (this.dragMoveCard) {
                this.dragMoveCard.recycle();
                this.dragMoveCard = null;
            }
        }

        private testOut(pos: UserPosition) {
            var testList = [17, 18, 19, 20, 22, 23, 24, 53, 54, 55];

            for (var i = 0; i < testList.length; i++) {
                var card = this.cardFactory.getOutCard(testList[i], pos);
                this.addCardToOut(card, pos);
            }
        }

        private testHand(pos: UserPosition) {
            var testList = [66, 67, 81, 82, 97, 102, 104];
            for (var i = 0; i < testList.length; i++) {
                var card = this.cardFactory.getHandCard(testList[i], pos, App.DataCenter.runingData.ownTingState);
                this.addCardToHand(card, pos);
            }
        }

        private testChi(pos: UserPosition) {
            var testList = [23, 23, 23];
            this.addCardToEat(testList, pos);
        }
        
        private testGang(pos: UserPosition, ang: boolean = false) {
            var testList = [23, 23, 23, 24];
            this.addCardToGang(testList, pos, ang);
        }

        private testMo(pos) {
            var cardValue = 0;
            cardValue = pos ? 0 : 53;
            var card = this.cardFactory.getHandCard(cardValue, pos, App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);
        }

        /**
         * 发牌
         */
        public dealCardShow(downCardValueList: Array<number>) {
            var handLen = 13;
            var upCardValueList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
            for (var i = 0; i < handLen; i++) {
                var cardDown = this.cardFactory.getHandCard(downCardValueList[i], UserPosition.Down);
                this.addCardToHand(cardDown, UserPosition.Down);
                cardDown.visible = false;

                var cardUp = this.cardFactory.getHandCard(upCardValueList[i], UserPosition.Up);
                this.addCardToHand(cardUp, UserPosition.Up);
                cardUp.visible = false;
            }

            for (var i = 0; i < 4; i++) {
                this.delayShowAGroup(i, UserPosition.Down);
                this.delayShowAGroup(i, UserPosition.Up);
            }
        }

        /**
         * 分组发牌动画
         */
        private delayShowAGroup(groIndex: number, pos: UserPosition) {
            // var delay = 500;
            var delay = 900;
            var handLen = 13;

            if (pos == UserPosition.Down) {
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

                setTimeout(() => {
                    for (var i = 4 * groIndex; i < 4 * groIndex + 4; i++) {
                        if (i >= handLen) {
                            break;
                        }
                        var card: Card = this.handCardList[pos][i];
                        card.setBack(true);

                        this.showFanDb(i);

                        var localI = i;
                        egret.setTimeout(()=>{
                            if (localI == handLen - 1) {
                                egret.setTimeout(()=>{
                                    this.downCardBackSHow();
                                },this, 200);
                            }

                            for (var j = i-1;j > i-4-1;j --) {
                                if (!this.handCardList[pos][j]) {
                                    break;
                                }
                                this.handCardList[pos][j].setBack(false);
                                this.handCardList[pos][j].visible = true;
                            }
                        }, this, 730);
                    }
                }, delay * groIndex, this)
            }
            else {
                setTimeout(() => {
                    for (var i = handLen - 1 - 4 * groIndex; i > handLen - 1 - 4 * groIndex - 4; i--) {
                        if (i < 0) {
                            break;
                        }
                        var card: Card = this.handCardList[pos][i];
                        card.y = card.initY + CardPos.moCardOffsetY[pos];
                        card.visible = true;
                        egret.Tween.get(card).wait(200).to({ y: card.initY }, 50);
                    }
                }, delay * groIndex, this)
            }
        }

        /**
         * 下家手牌盖牌动画
         */
        private downCardBackSHow() {
            for (var i = 0; i < this.handCardList[UserPosition.Down].length; i++) {
                var handCard = this.handCardList[UserPosition.Down][i];
                handCard.setBack(true);
                handCard.visible = false;
            }

            // 发牌补花
            this.dealCardBuHua();

            // 排序,重新排位置
            CardLogic.getInstance().sortHandCardAB(this.handCardList[UserPosition.Down]);
            for (var i = 0; i < this.handCardList[UserPosition.Down].length; i++) {
                this.handCardList[UserPosition.Down][i].x = CardPos.handCardPosXList[UserPosition.Down] + i * CardPos.handCardGapList[UserPosition.Down];
            }

            for (var i = 0; i < 13; i++) {
                this.showFanDb(i);
            }

            setTimeout(() => {
                for (var i = 0; i < this.handCardList[UserPosition.Down].length; i++) {
                    var handCard = this.handCardList[UserPosition.Down][i];
                    handCard.setBack(false);
                    handCard.visible = true;
                }

                // 首发牌
                this.ctrl.sendMod.sendAct(ACT_state.Act_Fa, []);

                // 处理发牌阶段可能触发的动作
                App.DataCenter.MsgCache.exeMsg(ProtocolHeadRev.R_101001, false);

                App.DataCenter.runingData.gameState = GameState.Playing;
            }, 740, this);
        }

        /**
         * 发牌补花
         */
        private dealCardBuHua() {
            var data: Array<any> = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101008);
            if (!data) {
                return;
            }

            for (var i = 0; i < data.length; i++) {
                // 本家补花
                if (data[i].seat_id == App.DataCenter.UserInfo.myUserInfo.seatID) {
                    this.gameScene.dbMod.showActDb(ACT_state.Act_Buhua, UserPosition.Down);
                    this.gameScene.flowerMod.setFlowerState(UserPosition.Down, data[i].hua_card.length);

                    for (var k = 0; k < data[i].hua_card.length; k++) {
                        for (var j = 0; j < this.handCardList[UserPosition.Down].length; j++) {
                            if (this.handCardList[UserPosition.Down][j].cardValue == data[i].hua_card[k]) {
                                this.handCardList[UserPosition.Down][j].setCardValueAndSHow(data[i].bu_cards[k]);
                            }
                        }
                    }
                }
                // 对家补花
                else {
                    this.gameScene.dbMod.showActDb(ACT_state.Act_Buhua, UserPosition.Up);
                    this.gameScene.flowerMod.setFlowerState(UserPosition.Up, data[i].hua_card.length);
                }
            }
        }

        /**
         * 摸牌补花
         */
        public moCardBuHua(pos) {
            this.gameScene.dbMod.showActDb(ACT_state.Act_Buhua, pos);
            if (!this.moCardList[pos][0]) {
                console.error("mo card error");
                return;
            }
            if (this.moCardList[pos][0].cardValue > 96) {
                egret.Tween.get(this.moCardList[pos][0])
                .to({ alpha: 0.8 }, 500)
                .to({ alpha: 0 }, 200)
                .call(()=>{
                    egret.Tween.removeTweens(this.moCardList[pos][0]);
                })
            }
        }

        /**
         * 摸牌
         */
        public moCardShow(cardValue: number, pos: UserPosition) {
            if (this.moCardList[pos][0]) {
                this.moCardList[pos][0].recycle();
                this.moCardList[pos].pop();
            }

            var moCard = this.cardFactory.getHandCard(cardValue, pos, App.DataCenter.runingData.ownTingState);
            this.addCardToMo(moCard, pos);
            moCard.visible = false;

            var movieMoCard = this.cardFactory.getHandCard(cardValue, pos, App.DataCenter.runingData.ownTingState);
            movieMoCard.x = moCard.x;
            movieMoCard.y = moCard.y + CardPos.moCardOffsetY[pos];
            this.movieGro.addChild(movieMoCard);

            if (pos == UserPosition.Down && App.DataCenter.runingData.ownTingState) {
                moCard.setGray(true);
                movieMoCard.setGray(true);
            }

            egret.Tween.get(movieMoCard)
                .wait(200)
                .to({ y: this.moCardList[pos][0].initY}, 50)
                .call(()=>{
                    moCard.visible = true;
                    movieMoCard && movieMoCard.parent && movieMoCard.parent.removeChild(movieMoCard);
                    egret.Tween.removeTweens(movieMoCard);
                })
        }

        /**
         * 出牌
         */
        public outCardShow(pos: UserPosition = UserPosition.Down, cardValue: number = 0) {
            var handleCard: Card;
            if (this.moCardList[pos][0].cardValue == cardValue) {
                handleCard = this.moCardList[pos][0];
            }
            else if (pos == UserPosition.Up && (App.DataCenter.runingData.curentRoomType == RoomType.noob || !App.DataCenter.runingData.ownTingState) ) {
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
            if (pos == UserPosition.Up) {
                tCardValue = cardValue;
            }

            var outCard = this.cardFactory.getOutCard(tCardValue, pos);
            this.addCardToOut(outCard, pos);
            outCard.visible = false;

            var movieSmallCard = this.cardFactory.getOutCard(tCardValue, pos);
            movieSmallCard.x = handleCard.x;
            movieSmallCard.y = handleCard.y + CardPos.moCardOffsetY[pos];
            this.movieGro.addChild(movieSmallCard);

            var moFlag: boolean = false;
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
                .call(() => {
                    movieSmallCard && movieSmallCard.parent && movieSmallCard.parent.removeChild(movieSmallCard);
                    outCard.visible = true;
                    if (!moFlag) {
                        this.moveMoCardToHand(pos);
                    }
                }, this)
        }

        /**
         * 摸牌移动到手牌指定位置
         */
        private moveMoCardToHand(pos: UserPosition = UserPosition.Down) {
            var offsetYList = [-130, -10];
            var tMoCard = this.moCardList[pos][0];
            if (!tMoCard) {
                console.error("have not mocard");
                return;
            }

            var tHandCard = this.cardFactory.getHandCard(tMoCard.cardValue, pos, App.DataCenter.runingData.ownTingState);
            this.addCardToHand(tHandCard, pos);
            tHandCard.visible = false;
            if (App.DataCenter.runingData.ownTingState && pos == UserPosition.Down) {
                tHandCard.setGray(true);
            }

            var movieCard = this.cardFactory.getHandCard(tMoCard.cardValue, pos, App.DataCenter.runingData.ownTingState);
            movieCard.x = tMoCard.x;
            movieCard.y = tMoCard.y;
            this.movieGro.addChild(movieCard);
            if (App.DataCenter.runingData.ownTingState && pos == UserPosition.Down) {
                movieCard.setGray(true);
            }

            tMoCard.recycle();
            this.moCardList[pos].pop();

            egret.Tween.get(movieCard)
                .to({ y: tHandCard.initY + offsetYList[pos] }, 100)
                .call(() => {
                    // 排列手牌
                    this.reHandCardPos(pos);

                    egret.Tween.get(movieCard)
                        .to({ x: tHandCard.x }, 200)
                        .to({ y: tHandCard.initY }, 100)
                        .call(() => {
                            tHandCard.visible = true;
                            movieCard && movieCard.parent && movieCard.parent.removeChild(movieCard);
                        }, this)
                }, this)
        }

        /**吃牌,碰牌操作 */
        public eatCardShow(cardValueList: Array<number>, pos: UserPosition, pengFlag: boolean = false) {
            var eatLen = 3;

            var rPos = 0;
            if (pos == 0) {
                rPos = 1;
            }
            this.removeLastOutCard(rPos);

            this.addCardToEat(cardValueList, pos, pengFlag);

            if (pos == UserPosition.Down || (App.DataCenter.runingData.ownTingState && App.DataCenter.runingData.guoHuFlag)) {
                for (var i = 0; i < cardValueList.length; i++) {
                    if (cardValueList[i] == App.DataCenter.runingData.latelyCardValue) {
                        cardValueList.splice(i, 1);
                        break;
                    }
                }
                for (var i = 0;i < cardValueList.length;i ++) {
                    this.deletHandCard(cardValueList[i], pos);
                }
            }
            else {
                for (var i = eatLen; i > 1; i--) {
                    this.handCardList[pos][this.handCardList[pos].length - 1].recycle();
                    this.handCardList[pos].pop();
                }
            }

            var card = this.cardFactory.getHandCard(this.handCardList[pos][this.handCardList[pos].length - 1].cardValue, pos, App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);
            this.handCardList[pos][this.handCardList[pos].length - 1].recycle();
            this.handCardList[pos].pop();

            this.reHandCardPos(pos);
        }

        /**杠牌操作 */
        public gangCardShow(gangType: ACT_state, cardValue: number, pos: UserPosition) {
            var gangLen = 4;
            var angFlag = false;
            if (gangType == ACT_state.Act_AnGang) {
                angFlag = true;
            }

            // 添加到杠牌
            if (gangType == ACT_state.Act_BuGang) {
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
            if (gangType == ACT_state.Act_Gang) {
                var rPos = 0;
                if (pos == 0) {
                    rPos = 1;
                }
                this.removeLastOutCard(rPos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
                this.deletHandCard(cardValue, pos);
            }
            else if (gangType == ACT_state.Act_BuGang) {
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
        }

        /**捉炮时，手牌和对家出牌的处理 */
        public dianHuCardShow(cardValue: number, pos: UserPosition) {
            var card = this.cardFactory.getHandCard(cardValue, pos, App.DataCenter.runingData.ownTingState);
            this.addCardToMo(card, pos);

            var rPos = 0;
            if (pos == 0) {
                rPos = 1;
            }
            this.removeLastOutCard(rPos);

            if (cardValue != this.moCardList[pos][0].cardValue) {
                console.error("dianHu card error");
            }
        }

        private testHu(pos, list: Array<number> = null) {
            var testList = [66, 67, 81, 82, 97, 102, 104];
            var list = list || testList;
            for (var i = 0;i < list.length;i ++) {
                this.addCardToHu(list[i], pos);
            }
        }

        /**清理牌相关动画GRO, 切换前后台时调用 */
        public clearCardMovieGro() {
            this.movieGro.removeChildren();
        }

        /**点击听牌后界面变化 */
        public tingCardShow() {
            this.drownAllHandCard();

            var pos = UserPosition.Down;
            var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
            var tingValueList = [];
            for (var key in data.act_info[ACT_state.Act_Ting]) {
                tingValueList.push(Number(key));
            }

            for (var i = 0;i < this.handCardList[pos].length;i ++) {
                var grayFlag = true;
                for (var j = 0;j < tingValueList.length;j ++) {
                    if (this.handCardList[pos][i].cardValue == tingValueList[j]) {
                        this.handCardList[pos][i].setArrow(true);
                        grayFlag = false;
                        break;
                    }
                }
                this.handCardList[pos][i].setGray(grayFlag);
            }

            var moFlag:boolean = false;
            for (var i = 0;i < tingValueList.length;i ++) {
                if (tingValueList[i] == this.moCardList[pos][0].cardValue) {
                    moFlag = true;
                }
            }
            this.moCardList[pos][0].setGray(true);
            if (moFlag) {
                this.moCardList[pos][0].setGray(false);
                this.moCardList[pos][0].setArrow(true);
            }
        }

        /**听牌完成后牌变化 */
        public tingDidShow(handList) {
            var pos = UserPosition.Down;
            for (var i = 0;i < this.handCardList[pos].length; i ++) {
                this.handCardList[pos][i].setArrow(false);
                this.handCardList[pos][i].setGray(true);
            }

            this.moCardList[pos][0].setArrow(false);
            this.moCardList[pos][0].setGray(true);

            this.tingDidCardShow(handList);
        }

        /**高级场听牌时对家牌处理 */
        private tingDidCardShow(handList) {
            if (App.DataCenter.runingData.curentRoomType != RoomType.noob && App.DataCenter.runingData.ownTingState) {
                var pos = UserPosition.Up;
                
                var tHandList = handList[App.DataCenter.UserInfo.getUserByPos(pos).seatID].hand_card;
                for (var i = 0;i < tHandList.length;i ++) {
                    var tCardValue = tHandList[i];
                    tCardValue && this.handCardList[pos][i].setHandSkin(tCardValue, pos, App.DataCenter.runingData.ownTingState);
                }
            }
        }

        /**取消听牌时的处理 */
        public tingCancleShow() {
            var pos = UserPosition.Down;
            this.drownAllHandCard();

            for (var i = 0;i < this.handCardList[pos].length; i ++) {
                this.handCardList[pos][i].setArrow(false);
                this.handCardList[pos][i].setGray(false);
            }

            this.moCardList[pos][0].setArrow(false);
            this.moCardList[pos][0].setGray(false);
        }

        /**胡牌时手牌推倒 */
        public huCardShow(pos: UserPosition, huCardValueList: Array<Array<number>>) {
            var listLen = huCardValueList.length;
            if (!listLen) {
                console.error("game over handcard error");
                return;
            }
            for (var i = 0;i < huCardValueList[listLen-2].length;i ++) {
                this.addCardToHu(huCardValueList[listLen-2][i], pos);
            }
            if (huCardValueList[listLen-1].length > 0) {
                this.addCardToHu(huCardValueList[listLen-1][0], pos, true);
            }

            for (var i = 0;i < this.handCardList[pos].length; i ++) {
                this.handCardList[pos][i].recycle();
            }
            this.handCardList[pos] = [];

            if (this.moCardList[pos][0]) {
                this.moCardList[pos][0].recycle();
                this.moCardList[pos] = [];
            }

            // Up暗杠处理
            if (pos == UserPosition.Up) {
                var gangList = [];
                for (var i = 0;i < huCardValueList.length;i ++) {
                    if (huCardValueList[i].length == 4 && huCardValueList[i][1] == 0) {
                        gangList.push(huCardValueList[i][0]);
                    }
                }
                if (gangList.length < 1) {
                    return;
                }

                console.log("this.angCardList[pos]======", this.angCardList[pos]);
                for (var i = 0;i < this.angCardList[pos].length/4; i ++) {
                    var oriCard:Card = this.angCardList[pos][i*4 +3];
                    var card = this.cardFactory.getEatCard(gangList[i], pos);
                    card.x = oriCard.x;
                    card.y = oriCard.y;
                    this.cardGro.addChild(card);

                    oriCard.recycle();
                    this.angCardList[pos][i*4+3] = card;
                }
            }
        }

        /**重连时的牌处理 */
        public reConnectCardShow(pos: UserPosition, orderCardList: Array<Array<number>>, lastValue: number, outCardList: Array<number>) {
            var handList: Array<number>;
            for (var i = 0;i < orderCardList.length;i ++) {
                var itemList = ArrayTool.deepCopy(orderCardList[i]);
                var itemLen = itemList.length;
                
                if (i == orderCardList.length-1) {
                    if (itemLen > 0) {
                        var card = this.cardFactory.getHandCard(itemList[0], pos, App.DataCenter.runingData.ownTingState);
                        this.addCardToMo(card, pos);
                    }
                }
                else if (i == orderCardList.length-2) {
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

            if (handList.length%3 == 2) {
                var moFlag = true;
                for (var i = 0;i < handList.length;i ++) {
                    if (handList[i] == lastValue) {
                        moFlag = false;
                        var card = this.cardFactory.getHandCard(lastValue, pos, App.DataCenter.runingData.ownTingState);
                        this.addCardToMo(card, pos);
                        handList.splice(i, 1);

                        if (pos == UserPosition.Down && App.DataCenter.runingData.ownTingState) {
                            card.setGray(true);
                        }
                        break;
                    }
                }
                // 如果最后一张操作牌找不到
                if (moFlag) {
                    var tLastValue = handList[handList.length-1];
                    var card = this.cardFactory.getHandCard(tLastValue, pos, App.DataCenter.runingData.ownTingState);
                    this.addCardToMo(card, pos);
                    handList.splice(handList.length-1, 1);
                    if (pos == UserPosition.Down && App.DataCenter.runingData.ownTingState) {
                        card.setGray(true);
                    }
                }
            }
            for (var i = 0;i < handList.length;i ++) {
                var card = this.cardFactory.getHandCard(handList[i], pos, App.DataCenter.runingData.ownTingState);
                this.addCardToHand(card, pos);

                if (pos == UserPosition.Down && App.DataCenter.runingData.ownTingState) {
                    card.setGray(true);
                }
            }

            for(var i = 0;i < outCardList.length;i ++) {
                var card = this.cardFactory.getOutCard(outCardList[i], pos);
                this.addCardToOut(card, pos);
            }
        }
    }
}