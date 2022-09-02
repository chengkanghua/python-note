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
    var HttpSender = (function (_super) {
        __extends(HttpSender, _super);
        function HttpSender() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        /**
         * 发送http请求
         * @param dataToSend 发送的Json数据
         * @param cb 回调函数
         * @param obj thisObject
         */
        HttpSender.prototype.send = function (paramObj, cb, obj, lock) {
            if (lock === void 0) { lock = true; }
            var dataObj = this.extendObj(Tpm.ProtocolHttp.httpHead, paramObj);
            var dataToSend = JSON.stringify(dataObj);
            var url = Tpm.App.DataCenter.ServerInfo.WEB_URL + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            console.log("send url:" + url);
            var request = new egret.HttpRequest();
            request.open(url, egret.HttpMethod.GET);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = e.currentTarget;
                console.log("requet.response:" + request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tpm.Tips.showTop("返回数据有误");
                    return;
                }
                if (re.code == 505) {
                    Tpm.App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
                }
                cb.call(obj, re);
            }, this);
            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("error : event=" + e);
                Tpm.App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
            }, this);
            request.send();
        };
        /**测试获取房间信息用 */
        HttpSender.prototype.sendTest = function (paramObj, cb, obj, lock) {
            if (lock === void 0) { lock = true; }
            var dataObj = this.extendObj(Tpm.ProtocolHttp.httpHead, paramObj);
            var dataToSend = JSON.stringify(dataObj);
            // var url = "http://192.168.1.168:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            var url = "http://oldboy.iespoir.com:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            var url = "http://127.0.0.1:8889/mj/" + paramObj["action"].toLowerCase() + '?base=' + dataToSend;
            console.log("send url:" + url);
            var request = new egret.HttpRequest();
            request.open(url, egret.HttpMethod.GET);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = e.currentTarget;
                console.log("requet.response:" + request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tpm.Tips.showTop("返回数据有误");
                    return;
                }
                if (re.code == 505) {
                    Tpm.App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
                }
                cb.call(obj, re);
            }, this);
            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("error : event=" + e);
                Tpm.App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
            }, this);
            request.send();
        };
        /**
         * 发送post登录请求
         */
        HttpSender.prototype.post = function (paramObj, cb, obj) {
            var dataObj = this.extendObj(Tpm.ProtocolHttp.httpHead, paramObj);
            var dataToSend = JSON.stringify(paramObj["param"]);
            var url = Tpm.App.DataCenter.ServerInfo.WEB_URL + paramObj["action"].toLowerCase();
            console.log("post url:" + url);
            var request = new egret.HttpRequest();
            request.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            request.open(url, egret.HttpMethod.POST);
            request.once(egret.Event.COMPLETE, function (e) {
                var request = e.currentTarget;
                console.log("requet.response:" + request.response);
                try {
                    var re = JSON.parse(request.response);
                }
                catch (err) {
                    Tpm.Tips.showTop("返回数据有误");
                    return;
                }
                cb.call(obj, re);
            }, this);
            request.once(egret.IOErrorEvent.IO_ERROR, function (e) {
                console.log("post error");
                Tpm.App.LoadingLock.minusLock();
                Tpm.App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
            }, this);
            console.log("loginsend:", dataToSend);
            request.send(dataToSend);
        };
        /**
         * 合并请求头和参数
         * @param obj1 请求头
         * @param obj2  参数
         */
        HttpSender.prototype.extendObj = function (obj1, obj2) {
            var obj3 = new Object;
            for (var key in obj2) {
                if (obj3.hasOwnProperty(key) || key == "action")
                    continue;
                obj3[key] = obj2[key];
                if (key == "skey") {
                    if (Tpm.App.DataCenter.UserInfo.myUserUid) {
                        obj3[key] = Tpm.App.DataCenter.UserInfo.myUserInfo.skey;
                    }
                }
                if (key == "uid") {
                    if (Tpm.App.DataCenter.UserInfo.myUserUid) {
                        obj3[key] = Tpm.App.DataCenter.UserInfo.myUserInfo.userID;
                    }
                }
                if (Tpm.App.DataCenter.UserInfo.myUserUid)
                    console.log("skey:::", Tpm.App.DataCenter.UserInfo.myUserInfo.skey);
                if (key == "param") {
                    for (var key1 in obj3[key]) {
                        if (key1 == "playerID") {
                            if (Tpm.App.DataCenter.UserInfo.myUserUid) {
                                obj3[key][key1] = Tpm.App.DataCenter.UserInfo.myUserInfo.userID;
                            }
                        }
                    }
                }
            }
            return obj3;
        };
        return HttpSender;
    }(Tpm.SingleClass));
    Tpm.HttpSender = HttpSender;
    __reflect(HttpSender.prototype, "Tpm.HttpSender");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HttpSender.js.map