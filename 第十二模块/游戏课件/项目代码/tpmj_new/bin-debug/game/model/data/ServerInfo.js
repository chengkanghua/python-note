var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 服务器信息
     */
    var ServerInfo = (function () {
        function ServerInfo() {
            /**是否是测试服 */
            this.HTTP_FLAG_TEST = true;
        }
        Object.defineProperty(ServerInfo.prototype, "WEB_URL", {
            /**php地址*/
            get: function () {
                // 判断是否本地测试php地址 
                var web_url = "";
                switch (Tpm.App.DataCenter.debugInfo.isLocalPhp) {
                    case 1:
                        web_url = "http://" + "39.108.10.161:50006" + "/majapi/";
                        break;
                    case 2:
                        web_url = "http://" + Tpm.App.DataCenter.ServerInfo.HTTP_LOGIN_IP + "/majapi/";
                        break;
                    default:
                        web_url = "http://" + Tpm.App.DataCenter.ServerInfo.HTTP_LOGIN_IP + "/majapi/";
                        break;
                }
                return web_url;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(ServerInfo.prototype, "HTTP_LOGIN_IP", {
            /**
             * http请求地址
            */
            get: function () {
                //var url = "oldboy.iespoir.com:8889";
                var url = "127.0.0.1:8889";
                // if (!App.DataCenter.ServerInfo.HTTP_FLAG_TEST) {
                //     url = "127.0.0.1:50002"
                // }
                return url;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(ServerInfo.prototype, "SERVER_URL", {
            /**Python地址 */
            get: function () {
                if (this._SERVER_URL && !Tpm.App.DataCenter.debugInfo.Sever) {
                    return this._SERVER_URL;
                }
                var serverCfg = Tpm.App.DataCenter.debugInfo.Sever;
                return "ws://" + "127.0.0.1" + ":" + "10000";
                // switch (serverCfg) {
                // case 1:
                // return "ws://" + "192.168.1.168" + ":" + "10000";
                // return "ws://" + "oldboy.iespoir.com" + ":" + "10000";
                // default:
                // return "ws://" + "192.168.1.168" + ":" + "10000";
                // return "ws://" + "oldboy.iespoir.com" + ":" + "10000";
                // }
            },
            /**Python地址 */
            set: function (url) {
                this._SERVER_URL = url;
            },
            enumerable: true,
            configurable: true
        });
        return ServerInfo;
    }());
    Tpm.ServerInfo = ServerInfo;
    __reflect(ServerInfo.prototype, "Tpm.ServerInfo");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ServerInfo.js.map