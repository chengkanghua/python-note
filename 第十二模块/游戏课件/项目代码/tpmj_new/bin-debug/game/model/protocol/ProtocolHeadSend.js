var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 发送消息协议号
     */
    var ProtocolHeadSend = (function () {
        function ProtocolHeadSend() {
        }
        return ProtocolHeadSend;
    }());
    /**登录游戏服务器 */
    ProtocolHeadSend.S_100002 = "100002";
    /**断线重连 */
    ProtocolHeadSend.S_100010 = "100010";
    /**准备 */
    ProtocolHeadSend.S_100100 = "100100";
    /**退出桌子 */
    ProtocolHeadSend.S_100103 = "100103";
    /**快速开始 */
    ProtocolHeadSend.S_100104 = "100104";
    /**选择房间 */
    ProtocolHeadSend.S_100105 = "100105";
    /**断线测试 */
    ProtocolHeadSend.S_100130 = "100130";
    /**玩家操作 */
    ProtocolHeadSend.S_100140 = "100140";
    /**解散房间测试 */
    ProtocolHeadSend.S_100112 = "100112";
    /**换牌等测试接口 */
    ProtocolHeadSend.S_100999 = "100999";
    Tpm.ProtocolHeadSend = ProtocolHeadSend;
    __reflect(ProtocolHeadSend.prototype, "Tpm.ProtocolHeadSend");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolHeadSend.js.map