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
    var EmailPanel = (function (_super) {
        __extends(EmailPanel, _super);
        function EmailPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.EmailPanelSkin";
            return _this;
        }
        /**添加到场景中*/
        EmailPanel.prototype.onEnable = function () {
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        EmailPanel.prototype.recDataFun = function (data) {
            var ac = new eui.ArrayCollection();
            var arr = [];
            var len = data.length;
            if (len > 0) {
                this.emailEmptyGroup.visible = false;
                for (var i = 0; i < len; i++) {
                    var itemData = Tpm.ArrayTool.deepCopy(Tpm.ProtocolHttpData.EmailListItemData);
                    itemData.id = data[i].id;
                    itemData.content = Tpm.StringTool.formatNickName(data[i].content, 26);
                    itemData.title = Tpm.StringTool.formatNickName(data[i].title, 20);
                    itemData.time_desc = data[i].time_desc;
                    arr.push(itemData);
                }
                ac.source = arr;
                this.emailList.itemRenderer = Tpm.EmailItem;
                this.emailList.dataProvider = ac;
            }
            else
                this.emailEmptyGroup.visible = true;
        };
        /**从场景中移除*/
        EmailPanel.prototype.onRemove = function () {
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        return EmailPanel;
    }(Tpm.BasePanel));
    Tpm.EmailPanel = EmailPanel;
    __reflect(EmailPanel.prototype, "Tpm.EmailPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EmailPanel.js.map