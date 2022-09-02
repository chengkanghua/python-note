var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 消息发送模块
     */
    var GameCtrlSend = (function () {
        function GameCtrlSend(ctrl) {
            this.gameCtrl = ctrl;
        }
        /**发送退出房间 */
        GameCtrlSend.prototype.sendExitRoom = function () {
            var data = Tpm.ProtocolDataSend.S_100103;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100103, data);
        };
        /**发送准备 */
        GameCtrlSend.prototype.sendReady = function () {
            var data = Tpm.ProtocolDataSend.S_100100;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            data.ready = 1;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100100, data);
        };
        /**发送操作动作 */
        GameCtrlSend.prototype.sendAct = function (act, cardList) {
            if (cardList === void 0) { cardList = null; }
            if (act == Tpm.ACT_state.Act_Guohu) {
                act = Tpm.ACT_state.Act_Pass;
            }
            console.log("发送操作：" + act + "  参数：" + cardList);
            var data = Tpm.ProtocolDataSend.S_100140;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            data.act = act;
            var paramObj = {
                card: 0,
                used_card: [],
                chu_card: 0
            };
            switch (act) {
                case Tpm.ACT_state.Act_Out:
                    paramObj.card = cardList[0];
                    console.log("out--selectBtnState-----", Tpm.App.DataCenter.runingData.selectBtnState);
                    if (Tpm.App.DataCenter.runingData.selectBtnState) {
                        var passData = Tpm.ArrayTool.deepCopy(Tpm.ProtocolDataSend.S_100140);
                        passData.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
                        passData.act = Tpm.ACT_state.Act_Pass;
                        Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100140, passData);
                    }
                    break;
                case Tpm.ACT_state.Act_Chi:
                    paramObj.used_card = cardList;
                    break;
                case Tpm.ACT_state.Act_AnGang:
                    paramObj.used_card.push(cardList);
                    break;
                case Tpm.ACT_state.Act_BuGang:
                    paramObj.used_card.push(cardList);
                    break;
                case Tpm.ACT_state.Act_Ting:
                    paramObj.chu_card = cardList[0];
                    break;
                default:
                    break;
            }
            data.act_params = JSON.stringify(paramObj);
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100140, data);
        };
        /**发送解散房间*测试 */
        GameCtrlSend.prototype.sendJieSanTest = function () {
            var data = Tpm.ProtocolDataSend.S_100112;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100112, data);
        };
        /**发送断线重连 */
        GameCtrlSend.prototype.sendReconnect = function () {
            var data = Tpm.ProtocolDataSend.S_100010;
            data.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100010, data);
        };
        return GameCtrlSend;
    }());
    Tpm.GameCtrlSend = GameCtrlSend;
    __reflect(GameCtrlSend.prototype, "Tpm.GameCtrlSend");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameCtrlSend.js.map