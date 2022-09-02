module Tpm {
    /**
     * 平台交互类
     */
    export class PlatformBridge extends SingleClass {
        /**用户信息 */
        public userInfo:any;
        /**平台端实现的监听函数 */
        public platformCallback:Function;
        /**游戏版本号*/
        private _gameVersion = "1.0.0";
        /**设计分辨率 */
        private _ContentSize = {contentWidth:750, contentHeight:1334};

        /**
         * 初始化监听函数前接收登录信息
         */
        public setUserInfo(data) {
            this.userInfo = data;
        }

        /**
         * 获取游戏版本号
         */
        public get gameVersion() {
            return this._gameVersion;
        }
        /**
         * 获取游戏设计分辨率
         */
        public get ContentSize() {
            return this._ContentSize;
        }

        /**
         * 平台传递事件时调用函数,监听函数
         */
        public linstenPlatformEvent(eventName:string, data:any = null) {
            switch (eventName) {
                case PlatFormEventConst.gameStart:
                    break;
                case PlatFormEventConst.payEnd:
                    break;
                case PlatFormEventConst.shareEnd:
                    break;
                default:
                    break;
            }
        }

        /**
         * 游戏发送事件
         */
        public sendPlatformEvent(eventName:string, data:any = null):any {
            if (!this.platformCallback) {
                console.error("platformCallback is null");
                return;
            }
            return this.platformCallback(eventName, data);
        }
    }
}