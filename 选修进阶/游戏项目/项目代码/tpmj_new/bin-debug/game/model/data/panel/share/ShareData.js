var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var ShareData = (function () {
        function ShareData() {
        }
        return ShareData;
    }());
    ShareData.wxShareData = {
        shareType: "wxShare",
        type: 0,
        title: "",
        content: "",
        picUrlstr: "" //图标 URL地址（网络地址）
    };
    ShareData.qqShareData = {
        shareType: "qqShare",
        title: "",
        url: "",
        description: "",
        picUrlstr: "" //图标 URL地址（网络地址）
    };
    Tpm.ShareData = ShareData;
    __reflect(ShareData.prototype, "Tpm.ShareData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ShareData.js.map