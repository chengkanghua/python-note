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
     * 平台交互类
     */
    var PlatformBridge = (function (_super) {
        __extends(PlatformBridge, _super);
        function PlatformBridge() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            /**游戏版本号*/
            _this._gameVersion = "1.0.0";
            /**设计分辨率 */
            _this._ContentSize = { contentWidth: 750, contentHeight: 1334 };
            return _this;
        }
        /**
         * 初始化监听函数前接收登录信息
         */
        PlatformBridge.prototype.setUserInfo = function (data) {
            this.userInfo = data;
        };
        Object.defineProperty(PlatformBridge.prototype, "gameVersion", {
            /**
             * 获取游戏版本号
             */
            get: function () {
                return this._gameVersion;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(PlatformBridge.prototype, "ContentSize", {
            /**
             * 获取游戏设计分辨率
             */
            get: function () {
                return this._ContentSize;
            },
            enumerable: true,
            configurable: true
        });
        /**
         * 平台传递事件时调用函数,监听函数
         */
        PlatformBridge.prototype.linstenPlatformEvent = function (eventName, data) {
            if (data === void 0) { data = null; }
            switch (eventName) {
                case Tpm.PlatFormEventConst.gameStart:
                    break;
                case Tpm.PlatFormEventConst.payEnd:
                    break;
                case Tpm.PlatFormEventConst.shareEnd:
                    break;
                default:
                    break;
            }
        };
        /**
         * 游戏发送事件
         */
        PlatformBridge.prototype.sendPlatformEvent = function (eventName, data) {
            if (data === void 0) { data = null; }
            if (!this.platformCallback) {
                console.error("platformCallback is null");
                return;
            }
            return this.platformCallback(eventName, data);
        };
        return PlatformBridge;
    }(Tpm.SingleClass));
    Tpm.PlatformBridge = PlatformBridge;
    __reflect(PlatformBridge.prototype, "Tpm.PlatformBridge");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PlatformBridge.js.map