var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var EmailData = (function () {
        function EmailData() {
        }
        return EmailData;
    }());
    /**邮件列表单条数据 */
    EmailData.emailItemData = {
        icon: "",
        title: "",
        content: "",
        time: "",
        id: 0 //邮件ID
    };
    /**邮件详情数据 */
    EmailData.emailDetailData = {
        icon: "",
        title: "",
        content: "",
        time: "",
        id: 0 //邮件ID
    };
    Tpm.EmailData = EmailData;
    __reflect(EmailData.prototype, "Tpm.EmailData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EmailData.js.map