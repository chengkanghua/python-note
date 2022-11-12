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
    var GameMenuMod = (function (_super) {
        __extends(GameMenuMod, _super);
        function GameMenuMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameMenuModSkin;
            return _this;
        }
        GameMenuMod.prototype.childrenCreated = function () {
        };
        GameMenuMod.prototype.onEnable = function () {
            this.initUI();
            this.gameAddBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
            this.gameRuleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRule, this);
            this.gameSetBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSet, this);
        };
        GameMenuMod.prototype.onRemove = function () {
        };
        /**
         * 初始化
         */
        GameMenuMod.prototype.initUI = function () {
            this.menuState = false;
            this.bg.visible = this.menuState;
            this.addGro.visible = this.menuState;
        };
        /**
         * 玩法
         */
        GameMenuMod.prototype.onRule = function () {
            Tpm.App.PanelManager.open(Tpm.PanelConst.PlayMethodPanel, true);
            this.onAdd();
        };
        /**
         * 设置
         */
        GameMenuMod.prototype.onSet = function () {
            Tpm.App.PanelManager.open(Tpm.PanelConst.SetPanel, true);
            this.onAdd();
        };
        /**
         * 下拉响应
         */
        GameMenuMod.prototype.onAdd = function () {
            this.menuState = !this.menuState;
            this.bg.visible = this.menuState;
            this.addGro.visible = this.menuState;
            if (this.menuState) {
                this.gameAddBtn.rotation = 180;
            }
            else {
                this.gameAddBtn.rotation = 0;
            }
        };
        return GameMenuMod;
    }(Tpm.BaseUI));
    Tpm.GameMenuMod = GameMenuMod;
    __reflect(GameMenuMod.prototype, "Tpm.GameMenuMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameMenuMod.js.map