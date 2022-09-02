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
     * 牌模块相关基础逻辑
     */
    var CardModBase = (function (_super) {
        __extends(CardModBase, _super);
        function CardModBase() {
            return _super.call(this) || this;
        }
        Object.defineProperty(CardModBase.prototype, "cardFactory", {
            /**获取牌工厂 */
            get: function () {
                return Tpm.CardFactory.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        CardModBase.prototype.initList = function () {
            this.outCardList = [[], []];
            this.handCardList = [[], []];
            this.chiCardList = [[], []];
            this.pengCardList = [[], []];
            this.gangCardList = [[], []];
            this.angCardList = [[], []];
            this.moCardList = [[], []];
            this.huCardList = [[], []];
        };
        /**放下所有手牌 */
        CardModBase.prototype.drownAllHandCard = function () {
            for (var i = 0; i < this.handCardList[Tpm.UserPosition.Down].length; i++) {
                this.handCardList[Tpm.UserPosition.Down][i].toDown();
            }
            this.moCardList[Tpm.UserPosition.Down][0] && this.moCardList[Tpm.UserPosition.Down][0].toDown();
        };
        /**
         * 获取吃碰杠总次数
         */
        CardModBase.prototype.getEatAllLen = function (pos) {
            var chiCount = Math.floor(this.chiCardList[pos].length / 3);
            var pengCount = Math.floor(this.pengCardList[pos].length / 3);
            var gangCount = Math.floor(this.gangCardList[pos].length / 4);
            var angCount = Math.floor(this.angCardList[pos].length / 4);
            var allCount = chiCount + pengCount + gangCount + angCount;
            // console.log("Pos==" + pos + "Chi==" + chiCount + "Peng==" + pengCount + "Gang==" + gangCount + "Ang==" + angCount + "All==" + allCount);
            return allCount;
        };
        /**
         * 添加牌到出牌
         */
        CardModBase.prototype.addCardToOut = function (card, pos) {
            var realX = 0;
            var realY = Tpm.CardPos.outCardPosYList[pos];
            if (pos == Tpm.UserPosition.Down) {
                realX = Tpm.CardPos.outCardPosXList[pos] + Tpm.CardPos.outCardGapList[pos] * this.outCardList[pos].length;
            }
            else if (pos == Tpm.UserPosition.Up) {
                realX = Tpm.CardPos.outCardPosXList[pos] - Tpm.CardPos.outCardGapList[pos] * this.outCardList[pos].length;
            }
            card.x = realX;
            card.y = realY;
            this.outCardList[pos].push(card);
            this.outGro.addChild(card);
        };
        /**
         * 添加牌到手牌
         */
        CardModBase.prototype.addCardToHand = function (card, pos) {
            var realX = 0;
            var realY = Tpm.CardPos.handCardPosYlist[pos];
            var eatLimitLen = 3;
            var eatAllLen = this.getEatAllLen(pos);
            if (pos == Tpm.UserPosition.Down) {
                realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * (eatAllLen * eatLimitLen + this.handCardList[pos].length);
            }
            else if (pos == Tpm.UserPosition.Up) {
                realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * this.handCardList[pos].length;
            }
            card.x = realX;
            card.y = realY;
            this.handCardList[pos].push(card);
            this.cardGro.addChild(card);
        };
        /**
         * 添加牌到吃牌,碰牌
         */
        CardModBase.prototype.addCardToEat = function (cardList, pos, pengFlag) {
            if (pengFlag === void 0) { pengFlag = false; }
            if (cardList.length != 3) {
                console.error("添加吃、碰牌异常");
                return;
            }
            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realY = Tpm.CardPos.eatCardPosYList[pos];
            var realX = 0;
            for (var i = 0; i < cardList.length; i++) {
                var card = this.cardFactory.getEatCard(cardList[i], pos);
                if (pos == Tpm.UserPosition.Down) {
                    realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + Tpm.CardPos.eatCardGapList[pos] * i;
                }
                else if (pos == Tpm.UserPosition.Up) {
                    realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + Tpm.CardPos.eatCardOffset[pos] + Tpm.CardPos.eatCardGapList[pos] * i;
                }
                card.x = realX;
                card.y = realY;
                if (pengFlag) {
                    this.pengCardList[pos].push(card);
                }
                else {
                    this.chiCardList[pos].push(card);
                }
                this.cardGro.addChild(card);
            }
        };
        /**
         * 添加牌到杠牌
         */
        CardModBase.prototype.addCardToGang = function (cardList, pos, angFlag) {
            if (angFlag === void 0) { angFlag = false; }
            if (cardList.length != 4) {
                console.error("添加杠牌异常");
                return;
            }
            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realX = 0;
            var realY = Tpm.CardPos.eatCardPosYList[pos];
            for (var i = 0; i < cardList.length; i++) {
                var card;
                if (i == eatLimitLen) {
                    var posI = 1;
                    if (angFlag && pos == Tpm.UserPosition.Up) {
                        card = this.cardFactory.getAnGangCard(cardList[i], pos);
                        this.angCardList[pos].push(card);
                    }
                    else if (angFlag) {
                        card = this.cardFactory.getEatCard(cardList[i], pos);
                        this.angCardList[pos].push(card);
                    }
                    else {
                        card = this.cardFactory.getEatCard(cardList[i], pos);
                        this.gangCardList[pos].push(card);
                    }
                    if (pos == Tpm.UserPosition.Down) {
                        realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + Tpm.CardPos.eatCardGapList[pos] * posI;
                        if (angFlag) {
                            realX = realX + 1;
                        }
                    }
                    else if (pos == Tpm.UserPosition.Up) {
                        realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + Tpm.CardPos.eatCardOffset[pos] + Tpm.CardPos.eatCardGapList[pos] * posI;
                    }
                    if (angFlag) {
                        realY = realY + Tpm.CardPos.angFourOffsetY[pos];
                    }
                    else {
                        realY = realY + Tpm.CardPos.gangFourOffsetY[pos];
                    }
                }
                else {
                    if (angFlag) {
                        card = this.cardFactory.getAnGangCard(cardList[i], pos);
                        this.angCardList[pos].push(card);
                    }
                    else {
                        card = this.cardFactory.getEatCard(cardList[i], pos);
                        this.gangCardList[pos].push(card);
                    }
                    if (pos == Tpm.UserPosition.Down) {
                        realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + Tpm.CardPos.eatCardGapList[pos] * i;
                    }
                    else if (pos == Tpm.UserPosition.Up) {
                        realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + Tpm.CardPos.eatCardOffset[pos] + Tpm.CardPos.eatCardGapList[pos] * i;
                    }
                }
                card.x = realX;
                card.y = realY;
                this.cardGro.addChild(card);
            }
        };
        /**
         * 添加牌到补杠位置
         */
        CardModBase.prototype.addCardToBu = function (cardValue, pos) {
            var count = 0;
            console.log("bgbg===", cardValue);
            console.log("pengList===", this.pengCardList[pos]);
            for (var i = 0; i < this.pengCardList[pos].length; i++) {
                if (this.pengCardList[pos][i].cardValue == cardValue) {
                    count++;
                    if (count == 2) {
                        var card = this.cardFactory.getEatCard(cardValue, pos);
                        card.x = this.pengCardList[pos][i].x;
                        card.y = this.pengCardList[pos][i].y + Tpm.CardPos.gangFourOffsetY[pos];
                        this.cardGro.addChild(card);
                        this.gangCardList[pos].push(this.pengCardList[pos][i - 1]);
                        this.gangCardList[pos].push(this.pengCardList[pos][i]);
                        this.gangCardList[pos].push(this.pengCardList[pos][i + 1]);
                        this.gangCardList[pos].push(card);
                        this.pengCardList[pos].splice(i + 1, 1);
                        this.pengCardList[pos].splice(i, 1);
                        this.pengCardList[pos].splice(i - 1, 1);
                        return;
                    }
                }
            }
            console.error("bu gang error");
            return;
        };
        /**
         * 添加牌到摸牌
         */
        CardModBase.prototype.addCardToMo = function (card, pos) {
            var realX = Tpm.CardPos.moCardPosXList[pos];
            var realY = Tpm.CardPos.handCardPosYlist[pos];
            card.x = realX;
            card.y = realY;
            this.moCardList[pos][0] = card;
            this.cardGro.addChild(card);
        };
        /**添加牌到胡牌 */
        CardModBase.prototype.addCardToHu = function (cardValue, pos, huFlag) {
            if (huFlag === void 0) { huFlag = false; }
            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realY = Tpm.CardPos.eatCardPosYList[pos];
            var realX = 0;
            var huOffsetX = 0;
            if (huFlag) {
                huOffsetX = Tpm.CardPos.huCardOffsetX[pos];
            }
            var card = this.cardFactory.getEatCard(cardValue, pos);
            if (pos == Tpm.UserPosition.Down) {
                realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + Tpm.CardPos.eatCardGapList[pos] * this.huCardList[pos].length + huOffsetX;
            }
            else if (pos == Tpm.UserPosition.Up) {
                if (huFlag) {
                    realX = Tpm.CardPos.handCardPosXList[pos] + this.handCardList[pos].length * Tpm.CardPos.eatCardOffset[pos] / eatLimitLen + Tpm.CardPos.huCardOffsetX[pos] - Tpm.CardPos.eatCardGapList[pos];
                }
                else {
                    realX = Tpm.CardPos.handCardPosXList[pos] + this.handCardList[pos].length * Tpm.CardPos.eatCardOffset[pos] / eatLimitLen + Tpm.CardPos.eatCardGapList[pos] * this.huCardList[pos].length;
                }
            }
            card.x = realX;
            card.y = realY;
            this.huCardList[pos].push(card);
            this.cardGro.addChild(card);
        };
        /**重新排列手牌位置 */
        CardModBase.prototype.reHandCardPos = function (pos) {
            Tpm.CardLogic.getInstance().sortHandCardAB(this.handCardList[pos]);
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                var card = this.handCardList[pos][i];
                var realX = 0;
                var eatLimitLen = 3;
                var eatAllLen = this.getEatAllLen(pos);
                if (pos == Tpm.UserPosition.Down) {
                    realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * (eatAllLen * eatLimitLen + i);
                }
                else if (pos == Tpm.UserPosition.Up) {
                    realX = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * i;
                }
                card.x = realX;
            }
        };
        /**删除最后一张出牌 */
        CardModBase.prototype.removeLastOutCard = function (pos) {
            this.outCardList[pos][this.outCardList[pos].length - 1].recycle();
            this.outCardList[pos].pop();
        };
        /**移除手牌中的指定牌 */
        CardModBase.prototype.deletHandCard = function (cardValue, pos, forceMo) {
            if (forceMo === void 0) { forceMo = false; }
            if (pos == Tpm.UserPosition.Up && !Tpm.App.DataCenter.runingData.ownTingState) {
                cardValue = 0;
            }
            console.log("dddddddddddddd===vv=======", cardValue);
            if (forceMo) {
                if (this.moCardList[pos][0]) {
                    this.moCardList[pos][0].recycle();
                    this.moCardList[pos] = [];
                }
                else {
                    console.error("delete mocard error");
                }
                return;
            }
            var deletFlag = false;
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                if (this.handCardList[pos][i].cardValue == cardValue || (cardValue == 0 && pos == Tpm.UserPosition.Up)) {
                    this.handCardList[pos][i].recycle();
                    this.handCardList[pos].splice(i, 1);
                    deletFlag = true;
                    break;
                }
            }
            if (!deletFlag) {
                if (this.moCardList[pos][0] && this.moCardList[pos][0].cardValue == cardValue) {
                    this.moCardList[pos][0].recycle();
                    this.moCardList[pos] = [];
                }
                else {
                    console.error("delete handcard error");
                }
            }
        };
        /**替换手牌某张牌值,测试接口使用，正常流程请勿使用 */
        CardModBase.prototype.reCardValue = function (oriValue, targetValue) {
            if (oriValue == 0 || targetValue == 0) {
                return;
            }
            var pos = Tpm.UserPosition.Down;
            var flag = true;
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                if (this.handCardList[pos][i].cardValue == oriValue) {
                    this.handCardList[pos][i].setCardValueAndSHow(targetValue);
                    this.reHandCardPos(pos);
                    flag = false;
                    return;
                }
            }
            if (flag) {
                if (oriValue == this.moCardList[pos][0].cardValue) {
                    this.moCardList[pos][0].setCardValueAndSHow(targetValue);
                }
            }
        };
        /**初始化翻牌动画列表 */
        CardModBase.prototype.initDb = function () {
            var factory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes("tpm_fanpai_ske_json"));
            factory.parseTextureAtlasData(RES.getRes("tpm_fanpai_tex_json"), RES.getRes("tpm_fanpai_tex_png"));
            this.cardDbMovieList = [];
            for (var i = 0; i < 13; i++) {
                var ar = factory.buildArmatureDisplay("Armature");
                this.cardDbMovieList.push(ar);
            }
        };
        /**播放翻牌动画 */
        CardModBase.prototype.showFanDb = function (index) {
            if (!this.cardDbMovieList[index].parent) {
                var pos = Tpm.UserPosition.Down;
                this.cardDbMovieList[index].y = Tpm.CardPos.handCardPosYlist[pos] + 61;
                this.cardDbMovieList[index].x = Tpm.CardPos.handCardPosXList[pos] + Tpm.CardPos.handCardGapList[pos] * index + 42.5;
                this.dbGro.addChild(this.cardDbMovieList[index]);
            }
            this.cardDbMovieList[index].animation.play("fanpai_erren", 1);
        };
        /**获取某张牌的剩余张数，胡牌提示时 */
        CardModBase.prototype.getCardResidue = function (residueCardValue) {
            if (residueCardValue > 83 || residueCardValue < 17) {
                console.error("get residue cardvalue error");
                return 0;
            }
            var origionNum = 4;
            for (var i = 0; i < this.chiCardList.length; i++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.chiCardList[i]);
            }
            for (var i = 0; i < this.pengCardList.length; i++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.pengCardList[i]);
            }
            for (var i = 0; i < this.gangCardList.length; i++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.gangCardList[i]);
            }
            for (var i = 0; i < this.outCardList.length; i++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.outCardList[i]);
            }
            for (var i = 0; i < this.moCardList.length; i++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.moCardList[i]);
            }
            origionNum -= this.getCardNumFromList(residueCardValue, this.angCardList[Tpm.UserPosition.Down]);
            origionNum -= this.getCardNumFromList(residueCardValue, this.handCardList[Tpm.UserPosition.Down]);
            if (origionNum < 0) {
                console.error("residue error", origionNum);
                origionNum = 0;
            }
            return origionNum;
        };
        CardModBase.prototype.getCardNumFromList = function (tCardValue, list) {
            var count = 0;
            for (var i = 0; i < list.length; i++) {
                if (tCardValue == list[i].cardValue) {
                    count++;
                }
            }
            return count;
        };
        /**清理牌 */
        CardModBase.prototype.clearAllCard = function () {
            this.movieGro.removeChildren();
            this.clearCardList(this.outCardList);
            this.clearCardList(this.handCardList);
            this.clearCardList(this.chiCardList);
            this.clearCardList(this.pengCardList);
            this.clearCardList(this.gangCardList);
            this.clearCardList(this.angCardList);
            this.clearCardList(this.huCardList);
            this.clearCardList(this.moCardList);
            this.outCardList = [[], []];
            this.handCardList = [[], []];
            this.chiCardList = [[], []];
            this.pengCardList = [[], []];
            this.gangCardList = [[], []];
            this.angCardList = [[], []];
            this.huCardList = [[], []];
            this.moCardList = [[], []];
            this.cardGro.removeChildren();
            this.cardGro.addChild(this.outGro);
        };
        CardModBase.prototype.clearCardList = function (cardList) {
            for (var i = 0; i < cardList.length; i++) {
                if (!cardList[i]) {
                    console.error("list eeee");
                }
                for (var j = 0; j < cardList[i].length; j++) {
                    cardList[i][j].recycle();
                }
            }
        };
        return CardModBase;
    }(Tpm.BaseGameMod));
    Tpm.CardModBase = CardModBase;
    __reflect(CardModBase.prototype, "Tpm.CardModBase");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=CardModBase.js.map