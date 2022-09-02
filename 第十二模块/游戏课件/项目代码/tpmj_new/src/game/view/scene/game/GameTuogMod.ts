module Tpm {
    /**
     * 托管
     */
    export class GameTuogMod extends BaseUI {
        /**托管状态 */
        private tuoGuanState: boolean = false;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameTuogModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        }

        protected onRemove() {
        }

        public setState(state:boolean) {
            this.tuoGuanState = state;
            this.visible = this.tuoGuanState;
        }

        /**点击取消 */
        private onTouch() {

        }
    }
}