module Tpm {
    export class HttpSender extends SingleClass{

        /**
         * 发送http请求
         * @param dataToSend 发送的Json数据
         * @param cb 回调函数
         * @param obj thisObject
         */
        public send(paramObj: Object, cb: Function, obj: any, lock: boolean = true): void {
            let dataObj = this.extendObj(ProtocolHttp.httpHead, paramObj);
            let dataToSend = JSON.stringify(dataObj);
            var url = App.DataCenter.ServerInfo.WEB_URL + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            console.log("send url:" + url);
            var request: egret.HttpRequest = new egret.HttpRequest();
            request.open(url, egret.HttpMethod.GET);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = <egret.HttpRequest>e.currentTarget;
                console.log("requet.response:" + request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tips.showTop("返回数据有误");
                    return;
                }
                if (re.code == 505) {
                    App.PanelManager.open(PanelConst.SocketClosePanel, false,null, null, false);
                }
                cb.call(obj, re);
            }, this);

            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("error : event=" + e);
                App.PanelManager.open(PanelConst.SocketClosePanel, false,null, null, false);
            }, this);

            request.send();
        }

        /**测试获取房间信息用 */
        public sendTest(paramObj: Object, cb: Function, obj: any, lock: boolean = true): void {
            let dataObj = this.extendObj(ProtocolHttp.httpHead, paramObj);
            let dataToSend = JSON.stringify(dataObj);
            // var url = "http://192.168.1.168:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            var url = "http://oldboy.iespoir.com:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            var url = "http://127.0.0.1:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            console.log("send url:" + url);
            var request: egret.HttpRequest = new egret.HttpRequest();
            request.open(url, egret.HttpMethod.GET);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = <egret.HttpRequest>e.currentTarget;
                console.log("requet.response:" + request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tips.showTop("返回数据有误");
                    return;
                }
                if (re.code == 505) {
                    App.PanelManager.open(PanelConst.SocketClosePanel, false,null, null, false);
                }
                cb.call(obj, re);
            }, this);

            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("error : event=" + e);
                App.PanelManager.open(PanelConst.SocketClosePanel, false,null, null, false);
            }, this);

            request.send();
        }

        /**
         * 发送post登录请求
         */
        public post(paramObj: Object, cb: Function, obj: any): void {
            let dataObj = this.extendObj(ProtocolHttp.httpHead, paramObj);
            let dataToSend = JSON.stringify(paramObj["param"]);
            var url = App.DataCenter.ServerInfo.WEB_URL + paramObj["action"].toLowerCase();
            console.log("post url:" + url);
            var request: egret.HttpRequest = new egret.HttpRequest();
            request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            request.open(url, egret.HttpMethod.POST);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = <egret.HttpRequest>e.currentTarget;
                console.log("requet.response:"+request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tips.showTop("返回数据有误");
                    return;
                }
                cb.call(obj, re);
            }, this);

            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("post error");
                Tpm.App.LoadingLock.minusLock();
                App.PanelManager.open(PanelConst.SocketClosePanel, false,null, null, false);
            }, this);
            console.log("loginsend:", dataToSend);
            request.send(dataToSend);
        }


        /**
         * 合并请求头和参数
         * @param obj1 请求头
         * @param obj2  参数
         */
        private extendObj(obj1: Object, obj2: Object) {

            var obj3 = new Object;

            for (let key in obj2) {
                if (obj3.hasOwnProperty(key) || key == "action") continue;
                obj3[key] = obj2[key];
                if (key == "skey") {
                    if (App.DataCenter.UserInfo.myUserUid) {
                        obj3[key] = App.DataCenter.UserInfo.myUserInfo.skey;
                    }
                }
                if (key == "uid") {
                    if (App.DataCenter.UserInfo.myUserUid) {
                        obj3[key] = App.DataCenter.UserInfo.myUserInfo.userID;
                    }
                } 
                if (App.DataCenter.UserInfo.myUserUid) console.log("skey:::", App.DataCenter.UserInfo.myUserInfo.skey)
                if (key == "param") {
                    for (let key1 in obj3[key]) {
                        if (key1 == "playerID") {
                            if (App.DataCenter.UserInfo.myUserUid) {
                                obj3[key][key1] = App.DataCenter.UserInfo.myUserInfo.userID;
                            }
                        }
                    }
                }
            }
            return obj3;
        }
    }
}
