module Tpm {
    /**
     * 接收消息协议号
     */
    export class ProtocolHeadRev {
        /**登录游戏服务器 */
        public static R_100002 = "100002";
        /**断线重连 */
        public static R_100010 = "100010";
        /**准备 */
        public static R_100100 = "100100";
        /**退出桌子 */
        public static R_100103 = "100103";
        /**快速开始 */
        public static R_100104 = "100104";
        /**选择房间 */
        public static R_100105 = "100105";
        /**推送玩家操作 */
        public static R_101001 = "101001";
        /**推送玩家摸牌 */
        public static R_101002 = "101002";
        /**推送游戏结束 */
        public static R_101003 = "101003";
        /**推送定庄 */
        public static R_101004 = "101004";
        /**推送发牌信息 */
        public static R_101005 = "101005";
        /**推送游戏结算 */
        public static R_101006 = "101006";
        /**推送摸牌补花 */
        public static R_101007 = "101007";
        /**推送发牌补花 */
        public static R_101008 = "101008";
        /**推送点数变化 */
        public static R_101100 = "101100";
        /**推送其他设备登录 */
        public static R_101101 = "101101";
        /**推送玩家退出桌子 */
        public static R_101105 = "101105";
        /**推送准备/取消准备 */
        public static R_101106 = "101106";
        /**推送玩家加入房间 */
        public static R_101107 = "101107";
        /**推送玩家断线重连 */
        public static R_101109 = "101109";
        /**推送玩家连接状态 */
        public static R_101110 = "101110";
        /**推送玩家操作响应 */
        public static R_101112 = "101112";
        /**换牌等测试接口 */
        public static R_100999 = "100999";
    }
}