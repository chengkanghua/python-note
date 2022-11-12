/**
 * @author svenballet
 * @date 2017-08-17
 */
var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Tpm;
(function (Tpm) {
    var LoginPanel = (function (_super) {
        __extends(LoginPanel, _super);
        function LoginPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.LoginPanelSkin";
            _this.ctrl = Tpm.App.getController(Tpm.LoginController.NAME);
            return _this;
        }
        LoginPanel.prototype.onEnable = function () {
            this.loginBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onLogin, this);
            this.registBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegist, this);
        };
        LoginPanel.prototype.onRemove = function () {
            this.loginBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onLogin, this);
            this.registBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegist, this);
            this.nameEdit.text = null;
            this.passEdit.text = null;
        };
        LoginPanel.prototype.onLogin = function () {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);
            if (!this.nameEdit.text || !this.passEdit.text) {
                Tpm.Tips.showTop("账号或密码不能为空");
            }
            else {
                this.ctrl.sendHttpLogin(this.nameEdit.text, this.passEdit.text);
            }
        };
        LoginPanel.prototype.onRegist = function () {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);
            this.hide();
            Tpm.App.PanelManager.open(Tpm.PanelConst.RegistPanel, false, null, null, true, true, null);
            // PanelManager.Instance.show(PanelConst.RegistPanel);
        };
        return LoginPanel;
    }(Tpm.BasePanel));
    Tpm.LoginPanel = LoginPanel;
    __reflect(LoginPanel.prototype, "Tpm.LoginPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LoginPanel.js.map