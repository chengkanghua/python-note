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
    /**接收WEB数据*/
    var HallHttpDataReceive = (function (_super) {
        __extends(HallHttpDataReceive, _super);
        function HallHttpDataReceive() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        /**
         * 接收商品列表
         */
        HallHttpDataReceive.revGoodsList = function (data) {
            var revData = Tpm.ProtocolHttpData.GoodsListData;
            revData = data;
            if (!revData.ret)
                Tpm.App.PanelManager.open(Tpm.PanelConst.ShopMallPanel, false, null, null, true, true, revData.data);
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 购买商品返回
         */
        HallHttpDataReceive.revBuyProp = function (data) {
            var revData = Tpm.ProtocolHttpData.GoodsListData;
            revData = data;
            if (!revData.ret) { }
            else if (revData.ret == 303) {
                Tpm.App.PlatformBridge.sendPlatformEvent(Tpm.PlatFormEventConst.payStart);
            }
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收邮件列表
         */
        HallHttpDataReceive.revEmailList = function (data) {
            var revData = Tpm.ProtocolHttpData.EmailListData;
            revData = data;
            if (!revData.ret || revData.ret == 400)
                Tpm.App.PanelManager.open(Tpm.PanelConst.EmailPanel, false, null, null, true, true, revData.data);
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收邮件详情
         */
        HallHttpDataReceive.revEmailDetail = function (data) {
            var revData = Tpm.ProtocolHttpData.emailDeatilData;
            revData = data;
            if (!revData.ret)
                Tpm.App.PanelManager.open(Tpm.PanelConst.EmailDetailPanel, false, null, null, true, true, revData.data);
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收个人信息
         */
        HallHttpDataReceive.revUserInfo = function (data) {
            var revData = Tpm.ProtocolHttpData.PersonalInfoData;
            revData = data;
            if (!revData.ret)
                Tpm.App.PanelManager.open(Tpm.PanelConst.PersonalInfoPanel, false, null, null, true, true, revData.data);
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收钻石金币信息
         */
        HallHttpDataReceive.revMoneyMsg = function (data) {
            var revData = Tpm.ProtocolHttpData.PersonalInfoData;
            revData = data;
            if (!revData.ret) {
                var hallscene = Tpm.App.SceneManager.getScene(Tpm.SceneConst.HallScene);
                hallscene && hallscene.headMod.updateDiamondAndGold(revData.data.diamond, revData.data.money);
            }
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收获取救济金信息
         */
        HallHttpDataReceive.revIncomeSupportMsg = function (data) {
            var revData = Tpm.ProtocolHttpData.GiveMoneyData;
            revData = data;
            if (!revData.ret) {
                Tpm.App.PanelManager.open(Tpm.PanelConst.GiveMoneyPanel, false, null, this, false, true, revData.data);
            }
            else
                Tpm.Tips.showTop(revData.desc);
        };
        /**
         * 接收领取救济金
         */
        HallHttpDataReceive.revIncomeSupport = function (data) {
            var revData = Tpm.ProtocolHttpData.GiveMoneyData;
            revData = data;
            if (!revData.ret) {
                var hallscene = Tpm.App.SceneManager.getScene(Tpm.SceneConst.HallScene);
            }
            else
                Tpm.Tips.showTop(revData.desc);
        };
        return HallHttpDataReceive;
    }(Tpm.SingleClass));
    Tpm.HallHttpDataReceive = HallHttpDataReceive;
    __reflect(HallHttpDataReceive.prototype, "Tpm.HallHttpDataReceive");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallHttpDataReceive.js.map