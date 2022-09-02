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
    /**发送WEB请求*/
    var HallHttpDataSend = (function (_super) {
        __extends(HallHttpDataSend, _super);
        function HallHttpDataSend() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        /**
         * 获取商品列表
         * @goodType  商品类型(1:房卡类)
         */
        HallHttpDataSend.sendGetGoodsList = function (goodType) {
            if (goodType === void 0) { goodType = 1; }
            var data = Tpm.ProtocolHttp.GetGoodsList;
            data.param.type = goodType;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revGoodsList, this);
        };
        /**
         * 购买道具
         * @goodid    商品id
         */
        HallHttpDataSend.sendBuyProp = function (goodId) {
            if (goodId === void 0) { goodId = 1; }
            var data = Tpm.ProtocolHttp.BuyProp;
            data.param.goodid = goodId;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revBuyProp, this);
        };
        /**
         * 获取邮件列表
         */
        HallHttpDataSend.sendGetEmailList = function () {
            var data = Tpm.ProtocolHttp.GetEmailList;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revEmailList, this);
        };
        /**
         * 获取邮件详情
         * @eid 邮件ID
         */
        HallHttpDataSend.sendReadEmail = function (eid) {
            var data = Tpm.ProtocolHttp.ReadEmail;
            data.param.id = eid;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revEmailDetail, this);
        };
        /**
         * 获取玩家信息
         */
        HallHttpDataSend.sendGetUserInfo = function () {
            var data = Tpm.ProtocolHttp.getUserInfo;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revUserInfo, this);
        };
        /**
         * 获取钻石和金币
         */
        HallHttpDataSend.sendGetDiamondAndGold = function () {
            var data = Tpm.ProtocolHttp.getMoneyMsg;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revMoneyMsg, this);
        };
        /**
         * 获取取救济金信息
         */
        HallHttpDataSend.sendGetIncomeSupportMsg = function () {
            var data = Tpm.ProtocolHttp.GetIncomeSupportMsg;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revIncomeSupportMsg, this);
        };
        /**
         * 领取救济金
         */
        HallHttpDataSend.sendGetIncomeSupport = function () {
            var data = Tpm.ProtocolHttp.GetIncomeSupport;
            Tpm.App.httpSender.send(data, Tpm.HallHttpDataReceive.revIncomeSupport, this);
        };
        return HallHttpDataSend;
    }(Tpm.SingleClass));
    Tpm.HallHttpDataSend = HallHttpDataSend;
    __reflect(HallHttpDataSend.prototype, "Tpm.HallHttpDataSend");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallHttpDataSend.js.map