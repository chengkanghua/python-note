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
    var LoginScene = (function (_super) {
        __extends(LoginScene, _super);
        function LoginScene() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.LoginSceneSkin;
            return _this;
        }
        LoginScene.prototype.onEnable = function () {
            this.ctrl.showLoginDialog();
        };
        LoginScene.prototype.onRemove = function () {
            this.ctrl.onRemove();
        };
        return LoginScene;
    }(Tpm.BaseScene));
    Tpm.LoginScene = LoginScene;
    __reflect(LoginScene.prototype, "Tpm.LoginScene");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LoginScene.js.map