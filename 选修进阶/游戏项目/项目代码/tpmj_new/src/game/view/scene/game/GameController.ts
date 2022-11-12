module Tpm {
    export class GameController extends BaseController {
        /**控制模块名*/
        public static NAME: string = "GameController";

        public sendMod: GameCtrlSend;
        private receiveMod: GameCtrlReceive;

        /**绑定的Scene */
        public get gameScene():GameScene {
            return App.SceneManager.getScene(SceneConst.GameScene);
        }

        public constructor() {
            super();
            this.sendMod = new GameCtrlSend(this);
            this.receiveMod = new GameCtrlReceive(this);
        }

        /**对应场景添加到显示列表时调用 */
        public onRegister() {
            this.receiveMod.onRegister();
        }
        
        /**对应场景从显示列表移除时调用 */
        public onRemove() {
            this.receiveMod.onRemove();
        }

        /**发送游戏内头像信息 */
        public sendHeadInfo(uid: number) {
            var httpsend = new HttpSender();
            var dataS = ProtocolHttp.getHeadInfo;
            dataS.uid = App.DataCenter.UserInfo.myUserUid;
            dataS.param.base.uid = uid;
            httpsend.send(dataS, this.revHeadInfo, this);
        }

        private revHeadInfo(data) {
            if (data.ret) {
                data.desc ? Tips.showTop(data.desc):Tips.showTop("获取个人信息失败");
                return;
            }

            App.PanelManager.open(PanelConst.PersonalInfoPanel, true, null, null, true, true, data.data);
        }
    }
}