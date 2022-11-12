var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var PlatFormEventConst = (function () {
        function PlatFormEventConst() {
        }
        return PlatFormEventConst;
    }());
    /**监听用户信息事件*/
    PlatFormEventConst.setUseInfo = "setUseInfo";
    /**监听游戏开始事件 */
    PlatFormEventConst.gameStart = "gameStart";
    /**发送游戏结束事件*/
    PlatFormEventConst.gameEnd = "gameEnd";
    /**发送支付事件*/
    PlatFormEventConst.payStart = "payStart";
    /**监听支付结束事件 */
    PlatFormEventConst.payEnd = "payEnd";
    /**发送分享开始事件 shareStart*/
    PlatFormEventConst.shareStart = "shareStart";
    /*监听分享完成事件**/
    PlatFormEventConst.shareEnd = "shareEnd";
    Tpm.PlatFormEventConst = PlatFormEventConst;
    __reflect(PlatFormEventConst.prototype, "Tpm.PlatFormEventConst");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PlatFormEventConst.js.map