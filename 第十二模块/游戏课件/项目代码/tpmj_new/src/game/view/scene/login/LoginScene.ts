module Tpm {
    export class LoginScene extends BaseScene {
        /**登录场景控制类*/
        protected ctrl: LoginController;

        public constructor() {
            super();
            this.skinName = TpmSkin.LoginSceneSkin;
        }

        protected onEnable() {
            this.ctrl.showLoginDialog();
        }

        protected onRemove() {
            this.ctrl.onRemove();
        }
    }
}