var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 接收消息协议号
     */
    var ProtocolHeadRev = (function () {
        function ProtocolHeadRev() {
        }
        return ProtocolHeadRev;
    }());
    /**登录游戏服务器 */
    ProtocolHeadRev.R_100002 = "100002";
    /**断线重连 */
    ProtocolHeadRev.R_100010 = "100010";
    /**准备 */
    ProtocolHeadRev.R_100100 = "100100";
    /**退出桌子 */
    ProtocolHeadRev.R_100103 = "100103";
    /**快速开始 */
    ProtocolHeadRev.R_100104 = "100104";
    /**选择房间 */
    ProtocolHeadRev.R_100105 = "100105";
    /**推送玩家操作 */
    ProtocolHeadRev.R_101001 = "101001";
    /**推送玩家摸牌 */
    ProtocolHeadRev.R_101002 = "101002";
    /**推送游戏结束 */
    ProtocolHeadRev.R_101003 = "101003";
    /**推送定庄 */
    ProtocolHeadRev.R_101004 = "101004";
    /**推送发牌信息 */
    ProtocolHeadRev.R_101005 = "101005";
    /**推送游戏结算 */
    ProtocolHeadRev.R_101006 = "101006";
    /**推送摸牌补花 */
    ProtocolHeadRev.R_101007 = "101007";
    /**推送发牌补花 */
    ProtocolHeadRev.R_101008 = "101008";
    /**推送点数变化 */
    ProtocolHeadRev.R_101100 = "101100";
    /**推送其他设备登录 */
    ProtocolHeadRev.R_101101 = "101101";
    /**推送玩家退出桌子 */
    ProtocolHeadRev.R_101105 = "101105";
    /**推送准备/取消准备 */
    ProtocolHeadRev.R_101106 = "101106";
    /**推送玩家加入房间 */
    ProtocolHeadRev.R_101107 = "101107";
    /**推送玩家断线重连 */
    ProtocolHeadRev.R_101109 = "101109";
    /**推送玩家连接状态 */
    ProtocolHeadRev.R_101110 = "101110";
    /**推送玩家操作响应 */
    ProtocolHeadRev.R_101112 = "101112";
    /**换牌等测试接口 */
    ProtocolHeadRev.R_100999 = "100999";
    Tpm.ProtocolHeadRev = ProtocolHeadRev;
    __reflect(ProtocolHeadRev.prototype, "Tpm.ProtocolHeadRev");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolHeadRev.js.map