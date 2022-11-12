module Tpm {
    /**
     * 牌模块相关基础逻辑
     */
    export class CardModBase extends BaseGameMod{
        /**实际的牌容器 */
        protected cardGro: eui.Group;
        /**出牌容器，cardGro子容器 */
        protected outGro:eui.Group;
        /**动画牌容器 */
        protected movieGro: eui.Group;
        /**龙骨动画层 */
        protected dbGro: eui.Group;

        //---------牌相关数据----------
        protected outCardList: Array<Array<Card>>;
        protected handCardList: Array<Array<Card>>;
        protected chiCardList: Array<Array<Card>>;
        protected pengCardList: Array<Array<Card>>;
        protected gangCardList: Array<Array<Card>>;
        protected angCardList: Array<Array<Card>>;
        protected moCardList: Array<Array<Card>>;
        protected huCardList: Array<Array<Card>>;

        //---------其他----------------
        private cardDbMovieList: Array<dragonBones.EgretArmatureDisplay>;

        public constructor() {
            super();
        }

        /**获取牌工厂 */
        protected get cardFactory() {
            return CardFactory.getInstance();
        }

        protected initList() {
            this.outCardList = [[], []];
            this.handCardList = [[], []];
            this.chiCardList = [[], []];
            this.pengCardList = [[], []];
            this.gangCardList = [[], []];
            this.angCardList = [[], []];
            this.moCardList = [[], []];
            this.huCardList = [[], []];
        }

        /**放下所有手牌 */
        protected drownAllHandCard() {
            for (var i = 0; i < this.handCardList[UserPosition.Down].length; i++) {
                this.handCardList[UserPosition.Down][i].toDown();
            }
            this.moCardList[UserPosition.Down][0] && this.moCardList[UserPosition.Down][0].toDown();
        }

        /**
         * 获取吃碰杠总次数
         */
        protected getEatAllLen(pos: UserPosition) {
            var chiCount = Math.floor(this.chiCardList[pos].length / 3);
            var pengCount = Math.floor(this.pengCardList[pos].length / 3);
            var gangCount = Math.floor(this.gangCardList[pos].length / 4);
            var angCount = Math.floor(this.angCardList[pos].length / 4);
            var allCount = chiCount + pengCount + gangCount + angCount;
            // console.log("Pos==" + pos + "Chi==" + chiCount + "Peng==" + pengCount + "Gang==" + gangCount + "Ang==" + angCount + "All==" + allCount);

            return allCount;
        }

        /**
         * 添加牌到出牌
         */
        protected addCardToOut(card: Card, pos: UserPosition) {
            var realX = 0;
            var realY = CardPos.outCardPosYList[pos];
            if (pos == UserPosition.Down) {
                realX = CardPos.outCardPosXList[pos] + CardPos.outCardGapList[pos] * this.outCardList[pos].length;
            }
            else if (pos == UserPosition.Up) {
                realX = CardPos.outCardPosXList[pos] - CardPos.outCardGapList[pos] * this.outCardList[pos].length;
            }
            card.x = realX;
            card.y = realY;

            this.outCardList[pos].push(card);
            this.outGro.addChild(card);
        }
        
        /**
         * 添加牌到手牌
         */
        protected addCardToHand(card: Card, pos: UserPosition) {
            var realX = 0;
            var realY = CardPos.handCardPosYlist[pos];
            var eatLimitLen = 3;
            var eatAllLen = this.getEatAllLen(pos);
            if (pos == UserPosition.Down) {
                realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * (eatAllLen * eatLimitLen + this.handCardList[pos].length);
            }
            else if (pos == UserPosition.Up) {
                realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * this.handCardList[pos].length;
            }
            card.x = realX;
            card.y = realY;

            this.handCardList[pos].push(card);
            this.cardGro.addChild(card);
        }

        /**
         * 添加牌到吃牌,碰牌
         */
        protected addCardToEat(cardList: Array<number>, pos: UserPosition, pengFlag: boolean = false) {
            if (cardList.length != 3) {
                console.error("添加吃、碰牌异常");
                return;
            }

            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realY = CardPos.eatCardPosYList[pos];
            var realX = 0;

            for (var i = 0; i < cardList.length; i++) {
                var card = this.cardFactory.getEatCard(cardList[i], pos)
                if (pos == UserPosition.Down) {
                    realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + CardPos.eatCardGapList[pos] * i;
                }
                else if (pos == UserPosition.Up) {
                    realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + CardPos.eatCardOffset[pos] + CardPos.eatCardGapList[pos] * i;
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
        }

        /**
         * 添加牌到杠牌
         */
        protected addCardToGang(cardList: Array<number>, pos: UserPosition, angFlag: boolean = false) {
            if (cardList.length != 4) {
                console.error("添加杠牌异常");
                return;
            }

            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realX = 0;
            var realY = CardPos.eatCardPosYList[pos];

            for (var i = 0; i < cardList.length; i++) {
                var card: Card;
                if (i == eatLimitLen) {
                    var posI = 1;
                    if (angFlag && pos == UserPosition.Up) {
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

                    if (pos == UserPosition.Down) {
                        realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + CardPos.eatCardGapList[pos] * posI;
                        if (angFlag) {
                            realX = realX + 1;
                        }
                    }
                    else if (pos == UserPosition.Up) {
                        realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + CardPos.eatCardOffset[pos] + CardPos.eatCardGapList[pos] * posI;
                    }

                    if (angFlag) {
                        realY = realY + CardPos.angFourOffsetY[pos];
                    }
                    else {
                        realY = realY + CardPos.gangFourOffsetY[pos];
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

                    if (pos == UserPosition.Down) {
                        realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + CardPos.eatCardGapList[pos] * i;
                    }
                    else if (pos == UserPosition.Up) {
                        realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * (handAllLen - (eatAllLen + 1) * eatLimitLen) + CardPos.eatCardOffset[pos] + CardPos.eatCardGapList[pos] * i;
                    }
                }
                card.x = realX;
                card.y = realY;
                this.cardGro.addChild(card);
            }
        }

        /**
         * 添加牌到补杠位置
         */
        protected addCardToBu(cardValue, pos) {
            var count = 0;
            console.log("bgbg===", cardValue);
            console.log("pengList===", this.pengCardList[pos]);
            for (var i = 0; i < this.pengCardList[pos].length; i++) {
                if (this.pengCardList[pos][i].cardValue == cardValue) {
                    count++;
                    if (count == 2) {
                        var card = this.cardFactory.getEatCard(cardValue, pos);
                        card.x = this.pengCardList[pos][i].x;
                        card.y = this.pengCardList[pos][i].y + CardPos.gangFourOffsetY[pos];
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
        }

        /**
         * 添加牌到摸牌
         */
        protected addCardToMo(card: Card, pos: UserPosition) {
            var realX = CardPos.moCardPosXList[pos];
            var realY = CardPos.handCardPosYlist[pos];
            card.x = realX;
            card.y = realY;

            this.moCardList[pos][0] = card;
            this.cardGro.addChild(card);
        }

        /**添加牌到胡牌 */
        protected addCardToHu(cardValue: number, pos: UserPosition, huFlag: boolean = false) {
            var eatLimitLen = 3;
            var handAllLen = 13;
            var eatAllLen = this.getEatAllLen(pos);
            var realY = CardPos.eatCardPosYList[pos];
            var realX = 0;
            var huOffsetX = 0;

            if (huFlag) {
                huOffsetX = CardPos.huCardOffsetX[pos];
            }

            var card = this.cardFactory.getEatCard(cardValue, pos)
            if (pos == UserPosition.Down) {
                realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * eatLimitLen * eatAllLen + CardPos.eatCardGapList[pos] * this.huCardList[pos].length + huOffsetX;
            }
            else if (pos == UserPosition.Up) {
                if (huFlag) {
                    realX = CardPos.handCardPosXList[pos] + this.handCardList[pos].length*CardPos.eatCardOffset[pos]/eatLimitLen + CardPos.huCardOffsetX[pos] - CardPos.eatCardGapList[pos];
                }
                else {
                    realX = CardPos.handCardPosXList[pos] + this.handCardList[pos].length*CardPos.eatCardOffset[pos]/eatLimitLen + CardPos.eatCardGapList[pos] * this.huCardList[pos].length;
                }
            }
            card.x = realX;
            card.y = realY;

            this.huCardList[pos].push(card);

            this.cardGro.addChild(card);
        }

        /**重新排列手牌位置 */
        protected reHandCardPos(pos) {
            CardLogic.getInstance().sortHandCardAB(this.handCardList[pos]);
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                var card = this.handCardList[pos][i];
                var realX = 0;
                var eatLimitLen = 3;
                var eatAllLen = this.getEatAllLen(pos);
                if (pos == UserPosition.Down) {
                    realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * (eatAllLen * eatLimitLen + i);
                }
                else if (pos == UserPosition.Up) {
                    realX = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * i;
                }
                card.x = realX;
            }
        }

        /**删除最后一张出牌 */
        protected removeLastOutCard(pos: number) {
            this.outCardList[pos][this.outCardList[pos].length - 1].recycle();
            this.outCardList[pos].pop();
        }

        /**移除手牌中的指定牌 */
        protected deletHandCard(cardValue: number, pos: UserPosition, forceMo: boolean = false) {
            if (pos == UserPosition.Up && !App.DataCenter.runingData.ownTingState) {
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

            var deletFlag:boolean = false;
            for (var i = 0; i < this.handCardList[pos].length; i++) {
                if (this.handCardList[pos][i].cardValue == cardValue || (cardValue == 0 && pos == UserPosition.Up)) {
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
        }

        /**替换手牌某张牌值,测试接口使用，正常流程请勿使用 */
        public reCardValue(oriValue: number, targetValue: number) {
            if (oriValue == 0 || targetValue == 0) {
                return;
            }
            var pos = UserPosition.Down;
            var flag = true; 
            for (var i = 0;i < this.handCardList[pos].length;i ++) {
                if(this.handCardList[pos][i].cardValue == oriValue) {
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
        }

        /**初始化翻牌动画列表 */
        protected initDb() {
            var factory: dragonBones.EgretFactory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes("tpm_fanpai_ske_json"));
            factory.parseTextureAtlasData(RES.getRes("tpm_fanpai_tex_json"), RES.getRes("tpm_fanpai_tex_png"));
            this.cardDbMovieList = [];
            for (var i = 0; i < 13; i++) {
                var ar: dragonBones.EgretArmatureDisplay = factory.buildArmatureDisplay("Armature");
                this.cardDbMovieList.push(ar);
            }
        }

        /**播放翻牌动画 */
        protected showFanDb(index: number) {
            if (!this.cardDbMovieList[index].parent) {
                var pos = UserPosition.Down;
                this.cardDbMovieList[index].y = CardPos.handCardPosYlist[pos] + 61;
                this.cardDbMovieList[index].x = CardPos.handCardPosXList[pos] + CardPos.handCardGapList[pos] * index + 42.5;
                this.dbGro.addChild(this.cardDbMovieList[index]);
            }
            this.cardDbMovieList[index].animation.play("fanpai_erren", 1);
        }

        /**获取某张牌的剩余张数，胡牌提示时 */
        public getCardResidue(residueCardValue: number):number {
            if (residueCardValue > 83 || residueCardValue < 17) {
                console.error("get residue cardvalue error");
                return 0;
            }
            var origionNum = 4;
            for(var i = 0;i < this.chiCardList.length;i ++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.chiCardList[i]);
            }
            for(var i = 0;i < this.pengCardList.length;i ++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.pengCardList[i]);
            }
            for(var i = 0;i < this.gangCardList.length;i ++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.gangCardList[i]);
            }
            for(var i = 0;i < this.outCardList.length;i ++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.outCardList[i]);
            }
            for(var i = 0;i < this.moCardList.length;i ++) {
                origionNum -= this.getCardNumFromList(residueCardValue, this.moCardList[i]);
            }
            origionNum -= this.getCardNumFromList(residueCardValue, this.angCardList[UserPosition.Down]);
            origionNum -= this.getCardNumFromList(residueCardValue, this.handCardList[UserPosition.Down]);

            if (origionNum < 0) {
                console.error("residue error", origionNum);
                origionNum = 0;
            }
            return origionNum;
        }

        private getCardNumFromList(tCardValue: number, list: Array<Card>):number {
            var count = 0;
            for(var i = 0;i < list.length;i ++) {
                if (tCardValue == list[i].cardValue) {
                    count ++;
                }
            }
            return count;
        }

        /**清理牌 */
        public clearAllCard() {
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
        }

        private clearCardList(cardList: Array<Array<Card>>) {
            for (var i = 0;i < cardList.length;i ++) {
                if (!cardList[i]) {
                    console.error("list eeee");
                }
                for (var j = 0;j < cardList[i].length;j ++) {
                    cardList[i][j].recycle();
                }
            }
        }
    }
}