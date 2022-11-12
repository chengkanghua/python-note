/**
 * @author svenballet
 * @date 2017-08-18
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
    var RegistPanel = (function (_super) {
        __extends(RegistPanel, _super);
        function RegistPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.RegistPanelSkin";
            _this.ctrl = Tpm.App.getController(Tpm.LoginController.NAME);
            return _this;
        }
        RegistPanel.prototype.onEnable = function () {
            this.registBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegister, this);
            this.backBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
        };
        RegistPanel.prototype.onRemove = function () {
            this.registBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onRegister, this);
            this.backBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
            this.nameEdit.text = null;
            this.nickNameEdit.text = null;
            this.passEdit.text = null;
        };
        RegistPanel.prototype.onRegister = function () {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);
            if (!this.nameEdit.text || !this.passEdit.text || !this.nickNameEdit.text) {
                Tpm.Tips.showTop("账号、昵称或密码不能为空");
            }
            else {
                this.ctrl.sendHttpRegister(this.nameEdit.text, this.passEdit.text, this.nickNameEdit.text);
            }
        };
        RegistPanel.prototype.clearInput = function () {
            this.nameEdit.text = null;
            this.passEdit.text = null;
            this.nickNameEdit.text = null;
        };
        RegistPanel.prototype.onBack = function () {
            // SoundManager.Instance.playEffect(SoundEffect.BiuDu);
            this.hide();
            Tpm.App.PanelManager.open(Tpm.PanelConst.LoginPanel, false, null, null, true, true, null);
        };
        return RegistPanel;
    }(Tpm.BasePanel));
    Tpm.RegistPanel = RegistPanel;
    __reflect(RegistPanel.prototype, "Tpm.RegistPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=RegistPanel.js.map