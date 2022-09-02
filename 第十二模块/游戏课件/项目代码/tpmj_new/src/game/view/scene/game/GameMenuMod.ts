module Tpm {
    export class GameMenuMod extends BaseUI {
        private bg:eui.Image;
        private gameAddBtn:eui.Button;
        private addGro:eui.Group;
        private gameRuleBtn:eui.Button;
        private gameSetBtn:eui.Button;

        private menuState: boolean;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameMenuModSkin;
        }

        protected childrenCreated() {

        }

        protected onEnable() {
            this.initUI();

            this.gameAddBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
            this.gameRuleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRule, this);
            this.gameSetBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSet, this);
        }

        protected onRemove() {
            
        }

        /**
         * 初始化
         */
        private initUI() {
            this.menuState = false;
            this.bg.visible = this.menuState;
            this.addGro.visible = this.menuState;
        }

        /**
         * 玩法
         */
        private onRule() {
            App.PanelManager.open(PanelConst.PlayMethodPanel,true);
            this.onAdd();
        }

        /**
         * 设置
         */
        private onSet() {
            App.PanelManager.open(PanelConst.SetPanel, true);
            this.onAdd();
        }

        /**
         * 下拉响应
         */
        private onAdd() {
            this.menuState = !this.menuState;
            this.bg.visible = this.menuState;
            this.addGro.visible = this.menuState;
            if (this.menuState) {
                this.gameAddBtn.rotation = 180;
            }
            else {
                this.gameAddBtn.rotation = 0;
            }
        }
    }
}