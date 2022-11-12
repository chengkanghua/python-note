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
    var EmailItem = (function (_super) {
        __extends(EmailItem, _super);
        function EmailItem() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.EmailItemSkin";
            return _this;
        }
        EmailItem.prototype.dataChanged = function () {
            var data = Tpm.ProtocolHttpData.EmailListItemData;
            data = this.data;
            if (data.icon != "")
                this.emailIcon.source = data.icon;
            this.emailTitle.text = data.title;
            this.emailContent.text = data.content;
            this.sendTime.text = data.time_desc.substr(5);
            this.id = data.id;
        };
        EmailItem.prototype.childrenCreated = function () {
            this.readEmailBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.readEmail, this);
        };
        EmailItem.prototype.readEmail = function (e) {
            // App.PanelManager.open(PanelConst.EmailDetailPanel);
            Tpm.HallHttpDataSend.sendReadEmail(this.id);
        };
        return EmailItem;
    }(eui.ItemRenderer));
    Tpm.EmailItem = EmailItem;
    __reflect(EmailItem.prototype, "Tpm.EmailItem");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EmailItem.js.map