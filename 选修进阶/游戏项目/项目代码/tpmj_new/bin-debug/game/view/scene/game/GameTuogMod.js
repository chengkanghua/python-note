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
     * 托管
     */
    var GameTuogMod = (function (_super) {
        __extends(GameTuogMod, _super);
        function GameTuogMod() {
            var _this = _super.call(this) || this;
            /**托管状态 */
            _this.tuoGuanState = false;
            _this.skinName = TpmSkin.GameTuogModSkin;
            return _this;
        }
        GameTuogMod.prototype.childrenCreated = function () {
        };
        GameTuogMod.prototype.onEnable = function () {
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        GameTuogMod.prototype.onRemove = function () {
        };
        GameTuogMod.prototype.setState = function (state) {
            this.tuoGuanState = state;
            this.visible = this.tuoGuanState;
        };
        /**点击取消 */
        GameTuogMod.prototype.onTouch = function () {
        };
        return GameTuogMod;
    }(Tpm.BaseUI));
    Tpm.GameTuogMod = GameTuogMod;
    __reflect(GameTuogMod.prototype, "Tpm.GameTuogMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameTuogMod.js.map