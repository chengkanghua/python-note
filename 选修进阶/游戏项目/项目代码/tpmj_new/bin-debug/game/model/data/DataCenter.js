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
    var DataCenter = (function (_super) {
        __extends(DataCenter, _super);
        function DataCenter() {
            var _this = _super.call(this) || this;
            _this.UserInfo = new Tpm.UserInfo();
            _this.ServerInfo = new Tpm.ServerInfo();
            _this.deskInfo = new Tpm.DeskInfo();
            _this.runingData = new Tpm.RuningData();
            _this.debugInfo = new Tpm.DebugInfo();
            _this.MsgCache = new Tpm.MsgCache();
            _this.roomInfo = new Tpm.RoomInfo();
            return _this;
        }
        return DataCenter;
    }(Tpm.SingleClass));
    Tpm.DataCenter = DataCenter;
    __reflect(DataCenter.prototype, "Tpm.DataCenter");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=DataCenter.js.map