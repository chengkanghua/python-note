var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var BaseController = (function () {
        function BaseController() {
        }
        /**绑定Scene添加到显示列表后调用, 无绑定SCEN则手动调用*/
        BaseController.prototype.onRegister = function () {
        };
        /**绑定Scene移除显示列表后调用*/
        BaseController.prototype.onRemove = function () {
        };
        /**
         * 发送事件
         * @type 事件名
         * @args 发送数据
         */
        BaseController.prototype.sendEvent = function (type) {
            var args = [];
            for (var _i = 1; _i < arguments.length; _i++) {
                args[_i - 1] = arguments[_i];
            }
            Tpm.App.EventManager.sendEvent(type, args);
        };
        /**
         * 监听事件
         * @type 事件名
         * @listener 回调函数
         * @thisObject 执行对象
         */
        BaseController.prototype.addEvent = function (type, listener, thisObject) {
            Tpm.App.EventManager.addEvent(type, listener, thisObject);
        };
        /**
         * 移除监听
         * @type 事件名
         * @listener 回调函数
         * @thisObject 执行对象
         */
        BaseController.prototype.removeEvent = function (type, listener, thisObject) {
            Tpm.App.EventManager.removeEvent(type, listener, thisObject);
        };
        return BaseController;
    }());
    Tpm.BaseController = BaseController;
    __reflect(BaseController.prototype, "Tpm.BaseController");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=BaseController.js.map