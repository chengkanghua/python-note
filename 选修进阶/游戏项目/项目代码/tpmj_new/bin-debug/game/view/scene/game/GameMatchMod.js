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
    var GameMatchMod = (function (_super) {
        __extends(GameMatchMod, _super);
        function GameMatchMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameMatchModSkin;
            return _this;
        }
        GameMatchMod.prototype.childrenCreated = function () {
        };
        GameMatchMod.prototype.onEnable = function () {
        };
        GameMatchMod.prototype.onRemove = function () {
            this.removeCircleTween();
        };
        /**
         * 设置类型、倒计时时间,并更新相关UI
         */
        GameMatchMod.prototype.setType = function (type) {
            this.uiType = type;
            this.removeCircleTween();
            switch (this.uiType) {
                case MatchType.common:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = false;
                    break;
                case MatchType.match:
                    this.matchGro.visible = true;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = false;
                    this.curentCircleImg = this.circleImg;
                    this.circleRound();
                    break;
                case MatchType.jieSan:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = true;
                    this.curentCircleImg = null;
                    break;
                case MatchType.reMatch:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = true;
                    this.jieSanGro.visible = false;
                    this.curentCircleImg = this.circleImgRe;
                    this.circleRound();
                    break;
                default:
                    console.error("type error");
                    break;
            }
        };
        /**
         * 转圈圈
         */
        GameMatchMod.prototype.circleRound = function () {
            egret.Tween.get(this.curentCircleImg, { loop: true }).to({ rotation: 360 }, 1000);
        };
        GameMatchMod.prototype.removeCircleTween = function () {
            this.curentCircleImg && egret.Tween.removeTweens(this.curentCircleImg);
        };
        return GameMatchMod;
    }(Tpm.BaseUI));
    Tpm.GameMatchMod = GameMatchMod;
    __reflect(GameMatchMod.prototype, "Tpm.GameMatchMod");
    /**
     * MatchMod的显示类型
     */
    var MatchType;
    (function (MatchType) {
        MatchType[MatchType["common"] = 0] = "common";
        MatchType[MatchType["match"] = 1] = "match";
        MatchType[MatchType["jieSan"] = 2] = "jieSan";
        MatchType[MatchType["reMatch"] = 3] = "reMatch";
    })(MatchType = Tpm.MatchType || (Tpm.MatchType = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameMatchMod.js.map