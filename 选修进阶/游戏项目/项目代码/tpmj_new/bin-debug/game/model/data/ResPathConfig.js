var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 代码中用到的资源配置
     */
    var ResPathConfig = (function () {
        function ResPathConfig() {
        }
        return ResPathConfig;
    }());
    /**加载资源背景*/
    ResPathConfig.loadBg = "tpm_hall_bg_png";
    /**Tips middle 文字背景 */
    ResPathConfig.tipsBg = "tpm_tips_bg_png";
    /**Tips top 文字背景 */
    ResPathConfig.tipsTopBg = "tpm_tips_top_bg_png";
    /**loadingLock旋转图 */
    ResPathConfig.lockRotat = "";
    Tpm.ResPathConfig = ResPathConfig;
    __reflect(ResPathConfig.prototype, "Tpm.ResPathConfig");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ResPathConfig.js.map