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
    var HallController = (function (_super) {
        __extends(HallController, _super);
        function HallController() {
            return _super.call(this) || this;
        }
        Object.defineProperty(HallController.prototype, "hallScene", {
            /**绑定的Scene */
            get: function () {
                return Tpm.App.SceneManager.getScene(Tpm.SceneConst.HallScene);
            },
            enumerable: true,
            configurable: true
        });
        /**对应场景添加到显示列表时调用 */
        HallController.prototype.onRegister = function () {
            var gameSocket = Tpm.App.gameSocket;
            gameSocket.register(Tpm.ProtocolHeadRev.R_100104, this.revQuickBegin, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_100105, this.revQuickBegin, this);
        };
        /**对应场景从显示列表移除是调用 */
        HallController.prototype.onRemove = function () {
        };
        /**选择房间发送 */
        HallController.prototype.sendChooseRoom = function (type) {
            var data = Tpm.ProtocolDataSend.S_100105;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            data.room_type = type;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100105, data);
        };
        /**快速开始发送 */
        HallController.prototype.sendQuickBegin = function () {
            var data = Tpm.ProtocolDataSend.S_100104;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100104, data);
        };
        /**快速开始返回处理, 选择房间返回处理 */
        HallController.prototype.revQuickBegin = function (data) {
            if (data.code == 200) {
                var revData = Tpm.ProtocolDataRev.R_100104;
                revData = data;
                Tpm.App.DataCenter.runingData.curentRoomType = revData.info.room_type;
                // 更新用户信息
                for (var key in revData.info.seat_info) {
                    if (revData.info.seat_info[key].user_id == Tpm.App.DataCenter.UserInfo.myUserUid) {
                        Tpm.App.DataCenter.UserInfo.myUserInfo.seatID = revData.info.seat_info[key].seat_id;
                        Tpm.App.DataCenter.UserInfo.myUserInfo.gold = revData.info.seat_info[key].point;
                    }
                    else {
                        var user = new Tpm.UserVO();
                        user.initUserFromSocket(revData.info.seat_info[key]);
                        Tpm.App.DataCenter.UserInfo.addUser(user);
                    }
                }
                // 进入牌局
                var scene = Tpm.App.SceneManager.runScene(Tpm.SceneConst.GameScene, Tpm.App.getController(Tpm.GameController.NAME));
                scene.intoRoom();
            }
            else {
                Tpm.Tips.showTop(data.desc);
            }
        };
        /**发送解散房间*测试 */
        HallController.prototype.sendJieSanTest = function () {
            var data = Tpm.ProtocolDataSend.S_100112;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100112, data);
        };
        /**获取房间信息*/
        HallController.prototype.sendRoomNum = function () {
            var httpsend = new Tpm.HttpSender();
            var dataS = Tpm.ProtocolHttp.getRoomNum;
            httpsend.sendTest(dataS, this.revRoomNum, this);
        };
        HallController.prototype.revRoomNum = function (data) {
            if (data.ret) {
                data.desc ? Tpm.Tips.showTop(data.desc) : Tpm.Tips.showTop("获取房间人数失败");
                return;
            }
            Tpm.App.DataCenter.roomInfo.reRoomNum(data.data.room_people_count);
            this.hallScene.roomMod.reRoomNum(Tpm.App.DataCenter.roomInfo.roomList);
        };
        return HallController;
    }(Tpm.BaseController));
    /**控制模块名*/
    HallController.NAME = "HallController";
    Tpm.HallController = HallController;
    __reflect(HallController.prototype, "Tpm.HallController");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallController.js.map