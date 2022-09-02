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
    var GameHeadMod = (function (_super) {
        __extends(GameHeadMod, _super);
        function GameHeadMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameHeadModSkin;
            return _this;
        }
        GameHeadMod.prototype.childrenCreated = function () {
            this.headImg.mask = this.headMask;
        };
        GameHeadMod.prototype.onEnable = function () {
            this.zhuangImg.visible = false;
            this.reGoldLab(0);
        };
        GameHeadMod.prototype.onRemove = function () {
        };
        /**根据UserInfo刷新头像状态 */
        GameHeadMod.prototype.reHeadState = function (pos) {
            var user = Tpm.App.DataCenter.UserInfo.getUserByPos(pos);
            if (user) {
                this.visible = true;
                this.reGoldLab(user.gold);
                this.reZhuangFlag(pos);
            }
            else {
                this.visible = false;
            }
        };
        /**设置庄家图片状态 */
        GameHeadMod.prototype.reZhuangFlag = function (pos) {
            var user = Tpm.App.DataCenter.UserInfo.getUserByPos(pos);
            if (user && user.zhuangFlag) {
                this.zhuangImg.visible = true;
            }
            else {
                this.zhuangImg.visible = false;
            }
        };
        /**设置金币数 */
        GameHeadMod.prototype.reGoldLab = function (goldNumb) {
            this.goldLab.text = Tpm.NumberTool.formatGoldHead(goldNumb);
        };
        return GameHeadMod;
    }(Tpm.BaseUI));
    Tpm.GameHeadMod = GameHeadMod;
    __reflect(GameHeadMod.prototype, "Tpm.GameHeadMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameHeadMod.js.map