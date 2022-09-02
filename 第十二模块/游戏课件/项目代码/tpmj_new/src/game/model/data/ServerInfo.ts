module Tpm {
    /**
     * 服务器信息
     */
    export class ServerInfo {
        /**是否是测试服 */
        public HTTP_FLAG_TEST: Boolean = true;
        /**Python地址 */
        private _SERVER_URL: string;
        /**密码MD5码*/
        public MD5PASS: string;

        /**php地址*/
        public get WEB_URL() {
            // 判断是否本地测试php地址 
            var web_url = "";
            switch (App.DataCenter.debugInfo.isLocalPhp) {
                case 1:
                    web_url = "http://" + "39.108.10.161:50006" + "/majapi/";
                    break;
                case 2:
                    web_url = "http://" + App.DataCenter.ServerInfo.HTTP_LOGIN_IP + "/majapi/";
                    break;
                default:
                    web_url = "http://" + App.DataCenter.ServerInfo.HTTP_LOGIN_IP + "/majapi/";
                    break;
            }
            return web_url;
        }

        /**
         * http请求地址
        */
        public get HTTP_LOGIN_IP() {
            //var url = "oldboy.iespoir.com:8889";
            var url = "127.0.0.1:8889";
            // if (!App.DataCenter.ServerInfo.HTTP_FLAG_TEST) {
            //     url = "127.0.0.1:50002"
            // }
            return url;
        }

        /**Python地址 */
        public set SERVER_URL(url: string) {
            this._SERVER_URL = url;
        }

        /**Python地址 */
        public get SERVER_URL(): string {
            if (this._SERVER_URL && !App.DataCenter.debugInfo.Sever) {
                return this._SERVER_URL;
            }

            var serverCfg = App.DataCenter.debugInfo.Sever;
            return "ws://" + "127.0.0.1" + ":" + "10000";
            // switch (serverCfg) {
                // case 1:
                    // return "ws://" + "192.168.1.168" + ":" + "10000";
                    // return "ws://" + "oldboy.iespoir.com" + ":" + "10000";
                // default:
                    // return "ws://" + "192.168.1.168" + ":" + "10000";
                    // return "ws://" + "oldboy.iespoir.com" + ":" + "10000";
            // }
        }
    }
}
