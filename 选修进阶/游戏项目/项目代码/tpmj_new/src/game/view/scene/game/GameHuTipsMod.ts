module Tpm {
    export class GameHuTipsMod extends BaseGameMod {
        private cancleBtn:eui.Button;
        private framGro:eui.Group;
        private fanList:eui.List;

        private itemWidth:number = 129;
        private itemHeight:number = 83;
        private frameMaxWidth:number = 536;
        private frameMaxHeight:number = 320;

        private curValue:number;
        private curList: Array<number>;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameHuTipsModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.cancleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        }

        protected onRemove() {
            this.hideTips();
        }

        /**显示胡牌提示 */
        public showHuTips(cardValueList: Array<any>, outCardValue:number) {
            if (this.curValue == outCardValue || this.curList == cardValueList) {
                // console.log("不用更新UI");
                return;
            }
            this.curList = cardValueList;
            this.curValue = outCardValue;
            // console.log("showHuTips=cardValueList==", cardValueList);
            var listLen = cardValueList.length;
            if (listLen < 1) {
                console.error("valuelist error");
                return;
            }

            var realWidth = this.frameMaxWidth;
            var realHeight = this.frameMaxHeight;
            if (listLen < 7 && listLen > 3) {
                realHeight = realHeight - (this.itemHeight+6);
            }
            else if (listLen < 4) {
                realHeight = realHeight - 2*(this.itemHeight+6);
            }

            if (listLen == 2) {
                realWidth = realWidth - this.itemWidth;
            }
            else if (listLen == 1) {
                realWidth = realWidth - 2*this.itemWidth;
            }
            this.framGro.width = realWidth;
            this.framGro.height = realHeight;
            this.validateNow();

            var ac = new eui.ArrayCollection();
            ac.source = cardValueList;
            this.fanList.dataProvider = ac;
            this.fanList.itemRenderer = HuTipsItem;

            this.framGro.visible = true;
        }

        /**显示听牌取消按钮 */
        public showCancle() {
            this.visible = true;
            this.framGro.visible = false;
        }

        /**隐藏胡牌提示 */
        public hideTips() {
            this.curValue = null;
            this.visible = false;
        }

        /**取消响应 */
        private onCancle() {
            this.hideTips();
            this.gameScene.selectBtnMod.reShow();
            this.gameScene.cardMod.tingCancleShow();
        }
    }
}