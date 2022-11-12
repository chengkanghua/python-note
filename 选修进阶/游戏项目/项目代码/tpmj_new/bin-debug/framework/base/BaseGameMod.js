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
    var BaseGameMod = (function (_super) {
        __extends(BaseGameMod, _super);
        function BaseGameMod() {
            return _super.call(this) || this;
        }
        Object.defineProperty(BaseGameMod.prototype, "gameScene", {
            /**对应Scene */
            get: function () {
                return this.parent;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(BaseGameMod.prototype, "ctrl", {
            /**对应的控制器 */
            get: function () {
                return Tpm.App.getController(Tpm.GameController.NAME);
            },
            enumerable: true,
            configurable: true
        });
        return BaseGameMod;
    }(Tpm.BaseUI));
    Tpm.BaseGameMod = BaseGameMod;
    __reflect(BaseGameMod.prototype, "Tpm.BaseGameMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=BaseGameMod.js.map