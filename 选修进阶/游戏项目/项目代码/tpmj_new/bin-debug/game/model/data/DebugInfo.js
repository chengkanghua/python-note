var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 测试环境配置
     */
    var DebugInfo = (function () {
        function DebugInfo() {
            /**测试密码*/
            this.password = "123456";
        }
        Object.defineProperty(DebugInfo.prototype, "isDebug", {
            /**是否调试模式*/
            get: function () {
                return (egret.getOption("debug") != null && egret.getOption("debug") != "");
            },
            enumerable: true,
            configurable: true
        });
        ;
        Object.defineProperty(DebugInfo.prototype, "isLocalPhp", {
            /**是否访问本地php，用于php访问地址设置*/
            get: function () {
                return parseInt(egret.getOption("local"));
            },
            enumerable: true,
            configurable: true
        });
        ;
        Object.defineProperty(DebugInfo.prototype, "Sever", {
            /**
             * gamesocket地址
             */
            get: function () {
                return Number(egret.getOption("server"));
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "account", {
            /**测试账号*/
            get: function () {
                var debug = egret.getOption("debug");
                if (typeof Number(debug.substr(0, 1) == "number")) {
                    return "oldboy1" + egret.getOption("debug");
                }
                else {
                    this.password = egret.getOption("password");
                    return egret.getOption("debug");
                }
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "skipHall", {
            /**是否跳过大厅 */
            get: function () {
                return false;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "skipNet", {
            /**是否跳过Http登录*/
            get: function () {
                return false;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "skipGameServer", {
            /**是否跳过游戏服登录 */
            get: function () {
                return false;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "testState", {
            /**是否是测试环境 */
            get: function () {
                return true;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(DebugInfo.prototype, "autoReady", {
            /**自动准备 */
            get: function () {
                return false;
            },
            enumerable: true,
            configurable: true
        });
        return DebugInfo;
    }());
    Tpm.DebugInfo = DebugInfo;
    __reflect(DebugInfo.prototype, "Tpm.DebugInfo");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=DebugInfo.js.map