module Tpm {
    export class GameTingMod extends BaseUI {
        private tingImg: eui.Image;
        private guoGro: eui.Group;
        private timesLab: eui.BitmapLabel;

        private tingState: TingState;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameTingModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.setState(TingState.normal);
        }

        protected onRemove() {
        }

        /**
         * 设置状态、过胡次数,并改变UI
         */
        public setState(state: TingState, num: number = 1, addFlag:boolean = false) {
            this.tingState = state;
            switch (this.tingState) {
                case TingState.normal:
                    this.tingImg.visible = false;
                    this.guoGro.visible = false;
                    this.timesLab.text = "0";
                    break;
                case TingState.guo:
                    this.tingImg.visible = false;
                    this.guoGro.visible = true;
                    if (addFlag) {
                        this.timesLab.text = Number(this.timesLab.text) + num + "";
                    }
                    else {
                        this.timesLab.text = num.toString();
                    }
                    break;
                case TingState.ting:
                    this.tingImg.visible = true;
                    this.guoGro.visible = false;
                    break;
                default:
                    this.tingImg.visible = false;
                    this.guoGro.visible = false;
                    break;
            }
        }
    }

    /**
     * 听牌，过胡状态
     */
    export enum TingState {
        normal,
        ting,
        guo
    }
}