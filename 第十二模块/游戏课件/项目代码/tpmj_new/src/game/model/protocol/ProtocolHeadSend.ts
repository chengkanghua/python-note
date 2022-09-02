module Tpm {
    /**
     * 发送消息协议号
     */
    export class ProtocolHeadSend {
        /**登录游戏服务器 */
        public static S_100002 = "100002";
        /**断线重连 */
        public static S_100010 = "100010";
        /**准备 */
        public static S_100100 = "100100";
        /**退出桌子 */
        public static S_100103 = "100103";
        /**快速开始 */
        public static S_100104 = "100104";
        /**选择房间 */
        public static S_100105 = "100105";
        /**断线测试 */
        public static S_100130 = "100130";
        /**玩家操作 */
        public static S_100140 = "100140";
        /**解散房间测试 */
        public static S_100112 = "100112";
        /**换牌等测试接口 */
        public static S_100999 = "100999";
    }
}