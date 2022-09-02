var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var EventConst = (function () {
        function EventConst() {
        }
        return EventConst;
    }());
    /**Socket连接成功*/
    EventConst.SocketConnect = "SocketConnect";
    /**socket开始重连*/
    EventConst.StartReconnect = "StartReconnect";
    /**send数据时，socket未连接*/
    EventConst.SocketNotConnect = "SocketNotConnect";
    /**socket 连接错误*/
    EventConst.SocketIOError = "SocketIOError";
    /**socket 关闭*/
    EventConst.SocketClose = "SocketClose";
    Tpm.EventConst = EventConst;
    __reflect(EventConst.prototype, "Tpm.EventConst");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EventConst.js.map