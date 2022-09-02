/**
 * @author svenballet 
 * @date 2017-08-17
 */

module Tpm {
	export class LoginPanel extends BasePanel {
        protected ctrl: LoginController;

        public nameEdit:eui.EditableText;
        public passEdit:eui.EditableText;
        public loginBtn:eui.Button;
        public registBtn:eui.Button;

        public constructor() {
            super();
            this.skinName = "TpmSkin.LoginPanelSkin";
            this.ctrl = (<LoginController>App.getController(LoginController.NAME))
        }

        public onEnable() {
            this.loginBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onLogin, this);
            this.registBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegist, this);
        }

        public onRemove() {
            this.loginBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onLogin, this);
            this.registBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegist, this);

            this.nameEdit.text = null;
            this.passEdit.text = null;
        }

        private onLogin() {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);

            if (!this.nameEdit.text || !this.passEdit.text) {
                Tips.showTop("账号或密码不能为空");
            }
            else {
                this.ctrl.sendHttpLogin(this.nameEdit.text, this.passEdit.text);
            }
        }

        private onRegist() {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);
            
            this.hide();
            App.PanelManager.open(PanelConst.RegistPanel, false, null, null, true, true, null);
            // PanelManager.Instance.show(PanelConst.RegistPanel);
        }
    } 
}