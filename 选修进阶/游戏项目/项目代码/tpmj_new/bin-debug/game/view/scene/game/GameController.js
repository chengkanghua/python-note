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
    var GameController = (function (_super) {
        __extends(GameController, _super);
        function GameController() {
            var _this = _super.call(this) || this;
            _this.sendMod = new Tpm.GameCtrlSend(_this);
            _this.receiveMod = new Tpm.GameCtrlReceive(_this);
            return _this;
        }
        Object.defineProperty(GameController.prototype, "gameScene", {
            /**绑定的Scene */
            get: function () {
                return Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene);
            },
            enumerable: true,
            configurable: true
        });
        /**对应场景添加到显示列表时调用 */
        GameController.prototype.onRegister = function () {
            this.receiveMod.onRegister();
        };
        /**对应场景从显示列表移除时调用 */
        GameController.prototype.onRemove = function () {
            this.receiveMod.onRemove();
        };
        /**发送游戏内头像信息 */
        GameController.prototype.sendHeadInfo = function (uid) {
            var httpsend = new Tpm.HttpSender();
            var dataS = Tpm.ProtocolHttp.getHeadInfo;
            dataS.uid = Tpm.App.DataCenter.UserInfo.myUserUid;
            dataS.param.base.uid = uid;
            httpsend.send(dataS, this.revHeadInfo, this);
        };
        GameController.prototype.revHeadInfo = function (data) {
            if (data.ret) {
                data.desc ? Tpm.Tips.showTop(data.desc) : Tpm.Tips.showTop("获取个人信息失败");
                return;
            }
            Tpm.App.PanelManager.open(Tpm.PanelConst.PersonalInfoPanel, true, null, null, true, true, data.data);
        };
        return GameController;
    }(Tpm.BaseController));
    /**控制模块名*/
    GameController.NAME = "GameController";
    Tpm.GameController = GameController;
    __reflect(GameController.prototype, "Tpm.GameController");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameController.js.map