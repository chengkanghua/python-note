module Tpm {
    export class DataCenter extends SingleClass {
        /**用户信息*/
        public UserInfo: UserInfo;
        /**服务器信息*/
        public ServerInfo: ServerInfo;
        /**桌子信息*/
        public deskInfo: DeskInfo;
        /**运行时关键数据 */
        public runingData: RuningData;
        /**测试配置 */
        public debugInfo: DebugInfo;
        /**消息队列 */
        public MsgCache: MsgCache;
        /**场次信息 */
        public roomInfo: RoomInfo;

        public constructor() {
            super();
            this.UserInfo = new UserInfo();
            this.ServerInfo = new ServerInfo();
            this.deskInfo = new DeskInfo();
            this.runingData = new RuningData();
            this.debugInfo = new DebugInfo();
            this.MsgCache = new MsgCache();
            this.roomInfo = new RoomInfo();
        }
    }
}
