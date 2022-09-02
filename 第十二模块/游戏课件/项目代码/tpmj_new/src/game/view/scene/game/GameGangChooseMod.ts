module Tpm {
    export class GameGangChooseMod extends BaseGameMod {
        private twoGro:eui.Group;
        private threeGro:eui.Group;
        private cancleBtn:eui.Button;

        private twoCardList: Array<Array<Card>>;
        private threeCardList: Array<Array<Card>>;
        private rectList: Array<eui.Rect>;
        private tValueList: Array<Array<number>>;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameGangChooseModSkin;
        }

        protected childrenCreated() {
            this.initRectList();

            this.twoCardList = [[], []];
            this.threeCardList = [[], [], []];
        }

        protected onEnable() {
            for (var i = 0;i < this.rectList.length;i ++) {
                this.rectList[i].addEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            } 
            this.cancleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        }

        protected onRemove() {
            for (var i = 0;i < this.rectList.length;i ++) {
                this.rectList[i].removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            } 
            this.cancleBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        }

        private initRectList() {
            this.rectList = [];

            for (var i = 0;i < 2;i ++) {
                this.rectList.push(<eui.Rect>this.twoGro.getChildAt(i+2));
            }
            for (var i = 0;i < 3;i ++) {
                this.rectList.push(<eui.Rect>this.threeGro.getChildAt(i+3));
            }
        }

        /**选择 */
        private onChoose(e: egret.Event) {
            var target = e.target;
            var chooseList: Array<number>;
            switch (target) {
                case this.rectList[0]:
                    chooseList = this.tValueList[0];
                    break;
                case this.rectList[1]:
                    chooseList = this.tValueList[1];
                    break;
                case this.rectList[2]:
                    chooseList = this.tValueList[0];
                    break;
                case this.rectList[3]:
                    chooseList = this.tValueList[1];
                    break;
                case this.rectList[4]:
                    chooseList = this.tValueList[2];
                    break;
                default:
                    console.error("gang choose error");
                    break;
            }
            if (!chooseList || chooseList.length < 3) {
                console.error("gang choose list error");
            }
            console.log("chooseList===", chooseList);
            this.hideCombo();
            this.dispatchEventWith("selectComboEvent", false, chooseList);
        }

        /**取消 */
        private onCancle() {
            this.hideCombo();
            this.gameScene.selectBtnMod.reShow();
        }
 
        public showCombo(valueList: Array<Array<number>>) {
            if (!valueList || valueList.length < 2 || valueList[0].length < 3) {
                console.error("param error");
                return;
            }
            this.tValueList = valueList;

            if (this.twoCardList[0].length < 1) {
                this.initCard();
            }

            var eatLen = 4;
            var curentCardList: Array<Array<Card>>;
            if (valueList.length == 2) {
                this.twoGro.visible = true;
                this.threeGro.visible = false;
                curentCardList = this.twoCardList;
            }
            else if (valueList.length == 3) {
                this.twoGro.visible = false;
                this.threeGro.visible = true;
                curentCardList = this.threeCardList;
            }
            for (var i = 0; i < valueList.length;i ++) {
                for (var j = 0; j < eatLen; j ++) {
                    curentCardList[i][j].setCardValueAndSHow(valueList[i][j]);
                }
            }

            this.visible = true;
        }

        /**隐藏 */
        public hideCombo() {
            this.visible = false;
        }

        private initCard() {
            var eatLen = 4;
            var xGap = 60;
            var origX = 10;
            var origY = 10;
            var scaleAll = 0.65;
            var cardFactory: CardFactory = CardFactory.getInstance();
            for(var i = 0;i < this.twoCardList.length;i ++) {
                for (var j = 0;j < eatLen;j ++) {
                    var tCard = cardFactory.getHandCard(0, UserPosition.Down);
                    (<eui.Group>this.twoGro.getChildAt(i)).addChild(tCard);
                    tCard.x = origX + xGap*j;
                    tCard.y = origY;
                    tCard.scaleX = tCard.scaleY = scaleAll;
                    
                    this.twoCardList[i].push(tCard);
                }
            }

            for(var i = 0;i < this.threeCardList.length;i ++) {
                for (var j = 0;j < eatLen;j ++) {
                    var tCard = cardFactory.getHandCard(0, UserPosition.Down);
                    (<eui.Group>this.threeGro.getChildAt(i)).addChild(tCard);
                    tCard.x = origX + xGap*j;
                    tCard.y = origY;
                    tCard.scaleX = tCard.scaleY = scaleAll;
                    this.threeCardList[i].push(tCard);
                }
            }
        }
    }
}