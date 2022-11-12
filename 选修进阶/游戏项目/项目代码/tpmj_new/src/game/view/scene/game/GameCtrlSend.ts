module Tpm {
    /**
     * 消息发送模块
     */
    export class GameCtrlSend {
        private gameCtrl: GameController;

        public constructor(ctrl:GameController) {
            this.gameCtrl = ctrl;
        }

        /**发送退出房间 */
        public sendExitRoom() {
            var data = ProtocolDataSend.S_100103;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            App.gameSocket.send(ProtocolHeadSend.S_100103, data);
        }

        /**发送准备 */
        public sendReady() {
            var data = ProtocolDataSend.S_100100;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            data.ready = 1;
            App.gameSocket.send(ProtocolHeadSend.S_100100, data);
        }

        /**发送操作动作 */
        public sendAct(act: ACT_state, cardList: Array<number> = null) {
             if (act == ACT_state.Act_Guohu) {
                act = ACT_state.Act_Pass;
            }
            console.log("发送操作："+act+"  参数："+cardList);
            var data = ProtocolDataSend.S_100140;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            data.act = act;

            var paramObj = {
                card: 0,
                used_card: [],
                chu_card: 0
            };
            switch (act) {
                case ACT_state.Act_Out:
                    paramObj.card = cardList[0];

                    console.log("out--selectBtnState-----", App.DataCenter.runingData.selectBtnState)
                    if (App.DataCenter.runingData.selectBtnState) {
                        var passData = ArrayTool.deepCopy(ProtocolDataSend.S_100140);
                        passData.user_id = App.DataCenter.UserInfo.myUserUid;
                        passData.act = ACT_state.Act_Pass;
                        App.gameSocket.send(ProtocolHeadSend.S_100140, passData);
                    }
                    break;
                case ACT_state.Act_Chi:
                    paramObj.used_card = cardList;
                    break;
                case ACT_state.Act_AnGang:
                    paramObj.used_card.push(cardList);
                    break;
                case ACT_state.Act_BuGang:
                    paramObj.used_card.push(cardList);
                    break;
                case ACT_state.Act_Ting:
                    paramObj.chu_card = cardList[0];
                    break;
                default:
                    break;
            }
            data.act_params = JSON.stringify(paramObj);
            App.gameSocket.send(ProtocolHeadSend.S_100140, data);
        }

        /**发送解散房间*测试 */
        public sendJieSanTest() {
            var data = ProtocolDataSend.S_100112;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            App.gameSocket.send(ProtocolHeadSend.S_100112, data);
        }

        /**发送断线重连 */
        public sendReconnect() {
            var data = ProtocolDataSend.S_100010;
            data.user_id = App.DataCenter.UserInfo.myUserUid;
            App.gameSocket.send(ProtocolHeadSend.S_100010, data);
        }
    }
}