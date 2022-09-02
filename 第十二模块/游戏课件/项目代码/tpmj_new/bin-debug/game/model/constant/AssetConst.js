var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var AssetConst = (function () {
        function AssetConst() {
        }
        return AssetConst;
    }());
    /**预加载*/
    AssetConst.Preload = "preload";
    Tpm.AssetConst = AssetConst;
    __reflect(AssetConst.prototype, "Tpm.AssetConst");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=AssetConst.js.map