var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Tpm;
(function (Tpm) {
    /**
     * 登录控制器
     */
    var LoginController = (function (_super) {
        __extends(LoginController, _super);
        function LoginController() {
            var _this = _super.call(this) || this;
            /**是否断线重连 */
            _this.reconnectFlag = false;
            return _this;
        }
        /**App中调用 */
        LoginController.prototype.onRegister = function () {
            this.addEvent(Tpm.EventConst.SocketConnect, this.onSocketSuccess, this);
            var gameSocket = Tpm.App.gameSocket;
            gameSocket.register(Tpm.ProtocolHeadRev.R_100002, this.revSocketLogin, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_100010, this.revReconnect, this);
        };
        /**弹出登录对话框*/
        LoginController.prototype.showLoginDialog = function () {
            Tpm.App.PanelManager.open(Tpm.PanelConst.LoginPanel, false, null, null, true, true, null);
        };
        /**登录入口
        */
        LoginController.prototype.loginGate = function () {
            Tpm.App.LoadingLock.addLock("WEB服务登录中...");
            // 测试账号http登录
            this.sendHttpLogin(Tpm.App.DataCenter.debugInfo.account, Tpm.App.DataCenter.debugInfo.password);
        };
        /**发送http登录信息 */
        LoginController.prototype.sendHttpLogin = function (account, password) {
            var httpsend = new Tpm.HttpSender();
            var dataS = {
                action: "Login",
                param: {}
            };
            var accountS = account;
            var passwordS = password;
            dataS.param = { user: account, password: password };
            httpsend.post(dataS, this.revHttpLogin, this);
        };
        /**http登录返回处理 */
        LoginController.prototype.revHttpLogin = function (data) {
            var revData = Tpm.ProtocolHttpData.LoginData;
            revData = data;
            if (!data.ret) {
                Tpm.App.LoadingLock.minusLock();
                var ud = revData.data;
                var su = new Tpm.UserVO();
                su.initUserFromHttp(ud);
                Tpm.App.DataCenter.UserInfo.myUserUid = ud.uid;
                Tpm.App.DataCenter.UserInfo.addUser(su);
                Tpm.App.DataCenter.ServerInfo.MD5PASS = ud.password;
                Tpm.App.DataCenter.ServerInfo.SERVER_URL = "ws://" + ud.ip + ":" + ud.port;
                if (!Tpm.App.DataCenter.debugInfo.skipGameServer) {
                    console.log("hhhhhhhhhhhhhhhhh11111:" + !Tpm.App.DataCenter.debugInfo.skipHall);
                    this.connectGameServer();
                }
                else
                    this.sendRoomInfo();
            }
            else {
                Tpm.Tips.showTop(revData.desc);
            }
        };
        /**发送http注册信息 */
        LoginController.prototype.sendHttpRegister = function (account, password, nickname) {
            var httpsend = new Tpm.HttpSender();
            var dataS = {
                action: "register",
                param: {}
            };
            var accountS = account;
            var passwordS = password;
            dataS.param = { user: account, password: password, nickname: nickname };
            httpsend.post(dataS, this.revHttpRegister, this);
        };
        /**http注册返回处理 */
        LoginController.prototype.revHttpRegister = function (data) {
            var revData = Tpm.ProtocolHttpData.LoginData;
            revData = data;
            if (!data.ret) {
                Tpm.App.LoadingLock.minusLock();
                var ud = revData.data;
                var su = new Tpm.UserVO();
                su.initUserFromHttp(ud);
                Tpm.App.DataCenter.UserInfo.myUserUid = ud.uid;
                Tpm.App.DataCenter.UserInfo.addUser(su);
                Tpm.App.DataCenter.ServerInfo.MD5PASS = ud.password;
                Tpm.App.DataCenter.ServerInfo.SERVER_URL = "ws://" + ud.ip + ":" + ud.port;
                if (!Tpm.App.DataCenter.debugInfo.skipGameServer) {
                    console.log("hhhhhhhhhhhhhhhhh11111:" + !Tpm.App.DataCenter.debugInfo.skipHall);
                    this.connectGameServer();
                }
                else
                    this.sendRoomInfo();
            }
            else {
                Tpm.Tips.showTop(revData.desc);
            }
        };
        /**连接游戏服务器 */
        LoginController.prototype.connectGameServer = function () {
            Tpm.App.LoadingLock.addLock("游戏服务登录中...");
            Tpm.App.gameSocket.startConnect(Tpm.App.DataCenter.ServerInfo.SERVER_URL, true);
        };
        /**socket服务器连接成功回调 */
        LoginController.prototype.onSocketSuccess = function () {
            this.sendSocketLogin();
        };
        /**发送socket登录请求 */
        LoginController.prototype.sendSocketLogin = function () {
            var data = Tpm.ProtocolDataSend.S_100002;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            // data.passwd = App.DataCenter.ServerInfo.MD5PASS;
            data.passwd = Tpm.App.DataCenter.debugInfo.password;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100002, data);
        };
        /**socket登录返回 */
        LoginController.prototype.revSocketLogin = function (data) {
            var revData = Tpm.ProtocolDataRev.R_100002;
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
                Tpm.Tips.showTop(data.desc);
            }
        };
        /**获取房间信息*/
        LoginController.prototype.sendRoomInfo = function () {
            var httpsend = new Tpm.HttpSender();
            var dataS = Tpm.ProtocolHttp.getRoomInfo;
            httpsend.sendTest(dataS, this.revRoomInfo, this);
        };
        LoginController.prototype.revRoomInfo = function (data) {
            if (data.ret) {
                console.error("get roominfo fail");
                return;
            }
            // 初始化房间信息
            Tpm.App.DataCenter.roomInfo.initList(data.data.room_cfg_info);
            if (this.reconnectFlag) {
                // 断线重连
                this.sendReconnect();
                this.reconnectFlag = false;
            }
            else {
                Tpm.App.PanelManager.closeAllPanel();
                // 进入大厅
                Tpm.App.SceneManager.runScene(Tpm.SceneConst.HallScene, Tpm.App.getController(Tpm.HallController.NAME));
                // 初始化房间UI
                Tpm.App.SceneManager.getScene(Tpm.SceneConst.HallScene).roomMod.initRoomUI(Tpm.App.DataCenter.roomInfo.roomList);
            }
        };
        /**发送断线重连 */
        LoginController.prototype.sendReconnect = function () {
            var data = Tpm.ProtocolDataSend.S_100010;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100010, data);
        };
        /**接收断线重连 */
        LoginController.prototype.revReconnect = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var uData = Tpm.ArrayTool.deepCopy(data);
            var scene = Tpm.App.SceneManager.runScene(Tpm.SceneConst.GameScene, Tpm.App.getController(Tpm.GameController.NAME));
            scene.reConnect(uData);
        };
        return LoginController;
    }(Tpm.BaseController));
    /**控制模块名*/
    LoginController.NAME = "LoginController";
    Tpm.LoginController = LoginController;
    __reflect(LoginController.prototype, "Tpm.LoginController");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LoginController.js.map