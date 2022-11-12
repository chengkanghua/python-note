module Tpm {
    /**
     * 登录控制器
     */
    export class LoginController extends BaseController {
        /**控制模块名*/
        public static NAME: string = "LoginController";

        public constructor() {
            super();
        }

        /**App中调用 */
        public onRegister() {
            this.addEvent(EventConst.SocketConnect, this.onSocketSuccess, this);
            var gameSocket: ClientSocket = App.gameSocket;
            gameSocket.register(ProtocolHeadRev.R_100002, this.revSocketLogin, this);
            gameSocket.register(ProtocolHeadRev.R_100010, this.revReconnect, this);
        }

        /**弹出登录对话框*/
        public showLoginDialog() {
            App.PanelManager.open(PanelConst.LoginPanel, false, null, null, true, true, null);
        }

        /**登录入口 
        */
        public loginGate() {
            Tpm.App.LoadingLock.addLock("WEB服务登录中...");

            // 测试账号http登录
            this.sendHttpLogin(App.DataCenter.debugInfo.account, App.DataCenter.debugInfo.password);
        }

        /**发送http登录信息 */
        public sendHttpLogin(account, password) {
            var httpsend = new HttpSender();
            var dataS = {
                action: "Login",
                param: {}
            };
            var accountS = account;
            var passwordS = password;
            dataS.param = { user: account, password: password };
            httpsend.post(dataS, this.revHttpLogin, this);
        }

        /**http登录返回处理 */
        private revHttpLogin(data) {
            var revData = ProtocolHttpData.LoginData;
            revData = data;

            if (!data.ret) {
                Tpm.App.LoadingLock.minusLock();
                var ud = revData.data;
                var su = new UserVO();
                su.initUserFromHttp(ud);
                App.DataCenter.UserInfo.myUserUid = ud.uid;
                App.DataCenter.UserInfo.addUser(su);

                App.DataCenter.ServerInfo.MD5PASS = ud.password;
                App.DataCenter.ServerInfo.SERVER_URL = "ws://" + ud.ip + ":" + ud.port;
                if (!App.DataCenter.debugInfo.skipGameServer) {
                    console.log("hhhhhhhhhhhhhhhhh11111:" + !App.DataCenter.debugInfo.skipHall);
                    this.connectGameServer();
                }
                else
                    this.sendRoomInfo();
            }
            else {
                Tips.showTop(revData.desc)
            }
        }

        /**发送http注册信息 */
        public sendHttpRegister(account, password, nickname) {
            var httpsend = new HttpSender();
            var dataS = {
                action: "register",
                param: {}
            };
            var accountS = account;
            var passwordS = password;
            dataS.param = { user: account, password: password, nickname: nickname };
            httpsend.post(dataS, this.revHttpRegister, this);
        }

        /**http注册返回处理 */
        private revHttpRegister(data) {
            var revData = ProtocolHttpData.LoginData;
            revData = data;

            if (!data.ret) {
                Tpm.App.LoadingLock.minusLock();
                var ud = revData.data;
                var su = new UserVO();
                su.initUserFromHttp(ud);
                App.DataCenter.UserInfo.myUserUid = ud.uid;
                App.DataCenter.UserInfo.addUser(su);

                App.DataCenter.ServerInfo.MD5PASS = ud.password;
                App.DataCenter.ServerInfo.SERVER_URL = "ws://" + ud.ip + ":" + ud.port;
                if (!App.DataCenter.debugInfo.skipGameServer) {
                    console.log("hhhhhhhhhhhhhhhhh11111:" + !App.DataCenter.debugInfo.skipHall);
                    this.connectGameServer();
                }
                else
                    this.sendRoomInfo();
            }
            else {
                Tips.showTop(revData.desc)
            }
        }

        /**连接游戏服务器 */
        public connectGameServer() {
            Tpm.App.LoadingLock.addLock("游戏服务登录中...");
            App.gameSocket.startConnect(App.DataCenter.ServerInfo.SERVER_URL, true);
        }

        /**socket服务器连接成功回调 */
        private onSocketSuccess() {
            this.sendSocketLogin();
        }

        /**发送socket登录请求 */
        public sendSocketLogin() {
            var data = ProtocolDataSend.S_100002;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            // data.passwd = App.DataCenter.ServerInfo.MD5PASS;
            data.passwd = App.DataCenter.debugInfo.password;
            App.gameSocket.send(ProtocolHeadSend.S_100002, data);
        }

        /**是否断线重连 */
        private reconnectFlag: boolean = false;
        /**socket登录返回 */
        private revSocketLogin(data) {
            var revData = ProtocolDataRev.R_100002;
            revData = data;
            if (revData.code == 200) {
                Tpm.App.LoadingLock.minusLock();

                if (revData.info.reconnect) {
                    this.reconnectFlag = true;
                }

                // 获取房间相关信息
                this.sendRoomInfo();
            }
            else {
                Tips.showTop(data.desc);
            }
        }

        /**获取房间信息*/
        public sendRoomInfo() {
            var httpsend = new HttpSender();
            var dataS = ProtocolHttp.getRoomInfo;
            httpsend.sendTest(dataS, this.revRoomInfo, this);
        }

        private revRoomInfo(data) {
            if (data.ret) {
                console.error("get roominfo fail");
                return;
            }

            // 初始化房间信息
            App.DataCenter.roomInfo.initList(data.data.room_cfg_info);

            if (this.reconnectFlag) {
                // 断线重连
                this.sendReconnect();
                this.reconnectFlag = false;
            }
            else {
                App.PanelManager.closeAllPanel();
                // 进入大厅
                App.SceneManager.runScene(SceneConst.HallScene, App.getController(HallController.NAME));
                // 初始化房间UI
                (<HallScene>App.SceneManager.getScene(SceneConst.HallScene)).roomMod.initRoomUI(App.DataCenter.roomInfo.roomList);
            }
        }

        /**发送断线重连 */
        public sendReconnect() {
            var data = ProtocolDataSend.S_100010;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            App.gameSocket.send(ProtocolHeadSend.S_100010, data);
        }

        /**接收断线重连 */
        private revReconnect(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }

            var uData = ArrayTool.deepCopy(data);
            var scene: GameScene = <GameScene>App.SceneManager.runScene(SceneConst.GameScene, App.getController(GameController.NAME));
            scene.reConnect(uData);
        }
    }
}