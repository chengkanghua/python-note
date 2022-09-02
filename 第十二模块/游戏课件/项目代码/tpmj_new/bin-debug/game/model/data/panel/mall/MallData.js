var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var MallData = (function () {
        function MallData() {
        }
        return MallData;
    }());
    MallData.mallItemData = {
        icon: "",
        money: "",
        price: "" //价格
    };
    Tpm.MallData = MallData;
    __reflect(MallData.prototype, "Tpm.MallData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=MallData.js.map