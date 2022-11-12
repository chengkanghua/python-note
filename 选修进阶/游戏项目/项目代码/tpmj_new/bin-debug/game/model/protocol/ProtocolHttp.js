var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var ProtocolHttp = (function () {
        function ProtocolHttp() {
        }
        return ProtocolHttp;
    }());
    /**http 头*/
    ProtocolHttp.httpHead = {
        ver: "1.6.1",
        AssetID: 1,
        mainID: 100
    };
    /**接收登录*/
    ProtocolHttp.rev_z_login = {
        ret: 0,
        desc: "",
        action: "",
        mainID: 0,
        AssetID: 0,
        data: {
            hadinvited: 1,
            deskTime: "",
            user: "",
            name: "",
            sex: -1,
            skey: "",
            avater_url: "",
            password: "",
            is_overtime: 0,
            last_ip: "",
            uid: 0,
            ip: "",
            port: "",
            prushport: "",
            excluroom_name: "",
            excluroom_code: "",
            round_card_num: 0,
            login_days: 0,
            payment: "",
            point: 0,
            is_visitor: 0
        }
    };
    /**获取商城列表*/
    ProtocolHttp.GetGoodsList = {
        action: "getgood",
        skey: "",
        uid: 0,
        param: { type: 0 }
    };
    /**购买道具*/
    ProtocolHttp.BuyProp = {
        action: "BuyProp",
        skey: "",
        uid: 0,
        param: { goodid: 0 }
    };
    /**确认支付接口 */
    ProtocolHttp.send_z_buySure = {
        action: "PlaceOrder",
        skey: "",
        uid: 0,
        param: { goodsid: 1, pay_type: 1, independent: 0, platform: 1 }
    };
    /**邮件列表*/
    ProtocolHttp.GetEmailList = {
        action: "GetEmail",
        skey: "",
        uid: 0,
        param: []
    };
    /**邮件详情*/
    ProtocolHttp.ReadEmail = {
        action: "ReadEmail",
        skey: "",
        uid: 0,
        param: { id: 0 }
    };
    /**获取邮件物品*/
    ProtocolHttp.GetReward = {
        action: "confirmemail",
        skey: "",
        uid: 0,
        param: { id: 0 }
    };
    /**获取救济金信息*/
    ProtocolHttp.GetIncomeSupportMsg = {
        action: "getincomesupport",
        skey: "",
        uid: 0,
        param: []
    };
    /**领取救济金*/
    ProtocolHttp.GetIncomeSupport = {
        action: "receiveincomesupport",
        skey: "",
        uid: 0,
        param: []
    };
    /**
     * 个人信息
     */
    ProtocolHttp.getUserInfo = {
        action: "getpersonal",
        skey: "",
        uid: 0,
        param: {}
    };
    /**
     * 钻石金币信息
     */
    ProtocolHttp.getMoneyMsg = {
        action: "getcurrency",
        skey: "",
        uid: 0,
        param: {}
    };
    /**
     * 分享记录
     */
    ProtocolHttp.getShareRecord = {
        action: "CombatGainsShare",
        skey: "",
        uid: 0,
        param: {
            deskBuildDate: "0",
            deskCode: "0"
        }
    };
    /**
     * 获取二维码
     */
    ProtocolHttp.getQrCodeImg = {
        action: "ShareByQrcode",
        skey: "",
        uid: 0,
        param: {}
    };
    /**
     * 获取房间信息
     */
    ProtocolHttp.getRoomInfo = {
        action: "get_hall_room_info",
        skey: "",
        uid: 0,
        param: {}
    };
    /**
     * 获取房间人数
     */
    ProtocolHttp.getRoomNum = {
        action: "get_hall_room_people_count",
        skey: "",
        uid: 0,
        param: {}
    };
    /**
     * 获取头像信息
     */
    ProtocolHttp.getHeadInfo = {
        action: "get_userinfo",
        skey: "",
        uid: 0,
        param: {
            base: {
                uid: 0
            }
        }
    };
    Tpm.ProtocolHttp = ProtocolHttp;
    __reflect(ProtocolHttp.prototype, "Tpm.ProtocolHttp");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolHttp.js.map