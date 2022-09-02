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
    var BaseScene = (function (_super) {
        __extends(BaseScene, _super);
        function BaseScene() {
            return _super.call(this) || this;
        }
        /**
         * 设置
         */
        BaseScene.prototype.setController = function (ctrl) {
            this.ctrl = ctrl;
        };
        return BaseScene;
    }(Tpm.BaseUI));
    Tpm.BaseScene = BaseScene;
    __reflect(BaseScene.prototype, "Tpm.BaseScene");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=BaseScene.js.map