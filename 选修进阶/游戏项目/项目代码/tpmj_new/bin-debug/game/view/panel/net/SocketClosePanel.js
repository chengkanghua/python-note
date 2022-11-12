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
    var SocketClosePanel = (function (_super) {
        __extends(SocketClosePanel, _super);
        function SocketClosePanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.SocketClosePanelSkin";
            return _this;
        }
        /**添加到场景中*/
        SocketClosePanel.prototype.onEnable = function () {
            this.sureBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
        };
        /**从场景中移除*/
        SocketClosePanel.prototype.onRemove = function () {
            this.sureBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
        };
        SocketClosePanel.prototype.onSure = function (e) {
            Tpm.App.DataCenter.runingData.clearData();
            Tpm.App.DataCenter.UserInfo.deleteAllUserExcptMe();
            Tpm.App.getController(Tpm.LoginController.NAME).connectGameServer();
            Tpm.App.PanelManager.closeAllPanel();
            this.hide();
        };
        return SocketClosePanel;
    }(Tpm.BasePanel));
    Tpm.SocketClosePanel = SocketClosePanel;
    __reflect(SocketClosePanel.prototype, "Tpm.SocketClosePanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=SocketClosePanel.js.map