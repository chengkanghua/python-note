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
    var BasePanel = (function (_super) {
        __extends(BasePanel, _super);
        function BasePanel() {
            var _this = _super.call(this) || this;
            _this.listenerVisible();
            return _this;
        }
        /***监听visible属性变化 避免没有调用hide半透明不移除*/
        BasePanel.prototype.listenerVisible = function () {
            var _this = this;
            eui.Binding.bindHandler(this, ["visible"], function (value) {
                if (!value) {
                    _this.hide();
                }
            }, this);
        };
        /**
         * 显示
         * @lock 是否锁定屏幕(增加半透明黑色背景)
         * @click 是否点击空白处可关闭弹框
         */
        BasePanel.prototype.show = function (lock, click) {
            if (lock === void 0) { lock = true; }
            if (click === void 0) { click = true; }
            Tpm.App.PopUpManager.addPopUp(this, lock, click);
        };
        /**隐藏*/
        BasePanel.prototype.hide = function () {
            Tpm.App.PopUpManager.removePopUp(this);
        };
        /**接收参数 */
        BasePanel.prototype.recDataFun = function (data) {
            this.recData = data;
        };
        return BasePanel;
    }(Tpm.BaseUI));
    Tpm.BasePanel = BasePanel;
    __reflect(BasePanel.prototype, "Tpm.BasePanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=BasePanel.js.map