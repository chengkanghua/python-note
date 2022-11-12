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
    var CommonMessageBoxPanel = (function (_super) {
        __extends(CommonMessageBoxPanel, _super);
        function CommonMessageBoxPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.CommonMessageBoxPanelSkin";
            return _this;
        }
        /**添加到场景中*/
        CommonMessageBoxPanel.prototype.onEnable = function () {
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.sureBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        CommonMessageBoxPanel.prototype.recDataFun = function (data) {
            if (data.content && data.content != "")
                this.tipsMessage.text = data.content;
        };
        /**从场景中移除*/
        CommonMessageBoxPanel.prototype.onRemove = function () {
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.sureBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        return CommonMessageBoxPanel;
    }(Tpm.BasePanel));
    Tpm.CommonMessageBoxPanel = CommonMessageBoxPanel;
    __reflect(CommonMessageBoxPanel.prototype, "Tpm.CommonMessageBoxPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=CommonMessageBoxPanel.js.map