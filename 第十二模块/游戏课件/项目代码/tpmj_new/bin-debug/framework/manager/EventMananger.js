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
    var EventMananger = (function (_super) {
        __extends(EventMananger, _super);
        function EventMananger() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            /**事件列表*/
            _this.eventList = {};
            return _this;
        }
        /**
         * 发送事件
         * @type 事件类型
         * @args 携带数据
         */
        EventMananger.prototype.sendEvent = function (type) {
            var args = [];
            for (var _i = 1; _i < arguments.length; _i++) {
                args[_i - 1] = arguments[_i];
            }
            var arr = this.eventList[type];
            if (arr != null) {
                var len = arr.length;
                var listen;
                var thisObject;
                for (var i = 0; i < len; i++) {
                    var msg = arr[i];
                    listen = msg[0];
                    thisObject = msg[1];
                    listen.apply(thisObject, args);
                }
            }
        };
        /**
         * 监听事件
         * @type 事件类型
         * @listener 回调函数
         * @thisObject 回调执行对象
         */
        EventMananger.prototype.addEvent = function (type, listener, thisObject) {
            var arr = this.eventList[type];
            if (arr == null) {
                arr = [];
                this.eventList[type] = arr;
            }
            else {
                var len = arr.length;
                for (var i = 0; i < len; i++) {
                    if (arr[i][0] == listener && arr[i][1] == thisObject) {
                        return;
                    }
                }
            }
            arr.push([listener, thisObject]);
        };
        /**
         * 移除事件
         * @type 事件类型
         * @listener 回调函数
         * @thisObject 回调执行对象
         */
        EventMananger.prototype.removeEvent = function (type, listener, thisObject) {
            var arr = this.eventList[type];
            if (arr != null) {
                var len = arr.length;
                for (var i = len - 1; i >= 0; i--) {
                    if (arr[i][0] == listener && arr[i][1] == thisObject) {
                        arr.splice(i, 1);
                    }
                }
            }
            if (arr && arr.length == 0) {
                this.eventList[type] = null;
                delete this.eventList[type];
            }
        };
        return EventMananger;
    }(Tpm.SingleClass));
    Tpm.EventMananger = EventMananger;
    __reflect(EventMananger.prototype, "Tpm.EventMananger");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EventMananger.js.map