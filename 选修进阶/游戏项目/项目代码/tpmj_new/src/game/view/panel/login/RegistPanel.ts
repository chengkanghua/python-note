/**
 * @author svenballet 
 * @date 2017-08-18
 */

module Tpm {
	export class RegistPanel extends BasePanel {
        protected ctrl: LoginController;

        public nameEdit:eui.EditableText;
        public nickNameEdit:eui.EditableText;
        public passEdit:eui.EditableText;
        public registBtn:eui.Button;
        public backBtn:eui.Button;

        public constructor() {
            super();
            this.skinName = "TpmSkin.RegistPanelSkin";
            this.ctrl = (<LoginController>App.getController(LoginController.NAME))
        }

        public onEnable() {
            this.registBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegister, this);
            this.backBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
        }

        public onRemove() {
            this.registBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegister, this);
            this.backBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);

            this.nameEdit.text = null;
            this.nickNameEdit.text = null;
            this.passEdit.text = null;
        }

        private onRegister() {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);

            if (!this.nameEdit.text || !this.passEdit.text || !this.nickNameEdit.text) {
                Tips.showTop("账号、昵称或密码不能为空");
            }
            else {
                this.ctrl.sendHttpRegister(this.nameEdit.text, this.passEdit.text, this.nickNameEdit.text);
            }
        }

        public clearInput() {
            this.nameEdit.text = null;
            this.passEdit.text = null;
            this.nickNameEdit.text = null;
        }

        private onBack() {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);

            this.hide();
            App.PanelManager.open(PanelConst.LoginPanel, false, null, null, true, true, null);
        }
    }
}