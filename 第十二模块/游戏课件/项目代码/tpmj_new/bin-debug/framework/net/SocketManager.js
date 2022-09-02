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
    var GameSocket = (function (_super) {
        __extends(GameSocket, _super);
        function GameSocket() {
            var _this = _super.call(this) || this;
            _this.gameSocket = new Tpm.ClientSocket();
            _this.gameSocket.name = "gameSocket";
            return _this;
        }
        return GameSocket;
    }(Tpm.SingleClass));
    Tpm.GameSocket = GameSocket;
    __reflect(GameSocket.prototype, "Tpm.GameSocket");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=SocketManager.js.map