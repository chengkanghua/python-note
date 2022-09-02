module Tpm {
    export class GameFlowerMod extends BaseUI {
        private downGro:eui.Group;
        private flowerLabDown:eui.Label;
        private upGro:eui.Group;
        private flowerLabUp:eui.Label;

        private upNum: number;
        private downNum: number;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameFlowerModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
        }

        protected onRemove() {
        }

        /**初始化 */
        public initUI() {
            this.downGro.visible = false;
            this.upGro.visible = false;
            this.upNum = 0;
            this.downNum = 0;
        }

        public setFlowerState(pos: UserPosition, times: number) {
            if (times < 1) {
                return;
            }

            if (pos == UserPosition.Down) {
                this.downGro.visible = true;
                this.downNum += times;
                this.flowerLabDown.text = "x"+this.downNum;
            }
            else {
                this.upGro.visible = true;
                this.upNum += times;
                this.flowerLabUp.text = "x"+this.upNum;
            }
        }
    }
}