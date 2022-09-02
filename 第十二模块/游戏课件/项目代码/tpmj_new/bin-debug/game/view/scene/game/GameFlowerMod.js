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
    var GameFlowerMod = (function (_super) {
        __extends(GameFlowerMod, _super);
        function GameFlowerMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameFlowerModSkin;
            return _this;
        }
        GameFlowerMod.prototype.childrenCreated = function () {
        };
        GameFlowerMod.prototype.onEnable = function () {
        };
        GameFlowerMod.prototype.onRemove = function () {
        };
        /**初始化 */
        GameFlowerMod.prototype.initUI = function () {
            this.downGro.visible = false;
            this.upGro.visible = false;
            this.upNum = 0;
            this.downNum = 0;
        };
        GameFlowerMod.prototype.setFlowerState = function (pos, times) {
            if (times < 1) {
                return;
            }
            if (pos == Tpm.UserPosition.Down) {
                this.downGro.visible = true;
                this.downNum += times;
                this.flowerLabDown.text = "x" + this.downNum;
            }
            else {
                this.upGro.visible = true;
                this.upNum += times;
                this.flowerLabUp.text = "x" + this.upNum;
            }
        };
        return GameFlowerMod;
    }(Tpm.BaseUI));
    Tpm.GameFlowerMod = GameFlowerMod;
    __reflect(GameFlowerMod.prototype, "Tpm.GameFlowerMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameFlowerMod.js.map