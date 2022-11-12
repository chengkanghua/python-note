var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 发送数据结构定义
     */
    var ProtocolDataSend = (function () {
        function ProtocolDataSend() {
        }
        return ProtocolDataSend;
    }());
    /**空参数 */
    ProtocolDataSend.S_common = {};
    ProtocolDataSend.S_100002 = {
        user_id: 0,
        passwd: "" //密码 md5
    };
    ProtocolDataSend.S_100010 = {
        user_id: 0
    };
    ProtocolDataSend.S_100100 = {
        user_id: 0,
        ready: 0 //0：未准备  1：准备
    };
    ProtocolDataSend.S_100103 = {
        user_id: 0
    };
    ProtocolDataSend.S_100104 = {
        user_id: 0
    };
    ProtocolDataSend.S_100105 = {
        user_id: 0,
        room_type: 0
    };
    ProtocolDataSend.S_100130 = {
        user_id: 0
    };
    ProtocolDataSend.S_100140 = {
        user_id: 0,
        act: 0,
        act_params: null
    };
    ProtocolDataSend.S_100112 = {
        user_id: 0
    };
    ProtocolDataSend.S_100999 = {
        user_id: 0,
        test_type: 0,
        test_params: "{}"
    };
    Tpm.ProtocolDataSend = ProtocolDataSend;
    __reflect(ProtocolDataSend.prototype, "Tpm.ProtocolDataSend");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolDataSend.js.map