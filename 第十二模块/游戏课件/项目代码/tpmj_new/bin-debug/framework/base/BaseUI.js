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
    var BaseUI = (function (_super) {
        __extends(BaseUI, _super);
        function BaseUI() {
            var _this = _super.call(this) || this;
            _this.addEventListener(egret.Event.ADDED_TO_STAGE, _this.onEnable, _this);
            _this.addEventListener(egret.Event.REMOVED_FROM_STAGE, _this.onRemove, _this);
            _this.addEventListener(egret.TouchEvent.TOUCH_TAP, function (e) {
                if (e.target instanceof eui.Button) {
                    //按钮声音统一的话，在此播放
                    Tpm.App.SoundManager.playEffect(Tpm.SoundManager.button);
                }
            }, _this);
            return _this;
        }
        /**组件创建完毕*/
        BaseUI.prototype.childrenCreated = function () {
        };
        /**添加到场景中*/
        BaseUI.prototype.onEnable = function () {
        };
        /**从场景中移除*/
        BaseUI.prototype.onRemove = function () {
        };
        /**销毁*/
        BaseUI.prototype.onDestroy = function () {
        };
        /**隐藏*/
        BaseUI.prototype.hide = function () {
            this.parent && this.parent.removeChild(this);
        };
        return BaseUI;
    }(eui.Component));
    Tpm.BaseUI = BaseUI;
    __reflect(BaseUI.prototype, "Tpm.BaseUI");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=BaseUI.js.map