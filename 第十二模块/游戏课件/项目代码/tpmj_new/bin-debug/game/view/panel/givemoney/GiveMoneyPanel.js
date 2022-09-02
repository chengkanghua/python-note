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
    var GiveMoneyPanel = (function (_super) {
        __extends(GiveMoneyPanel, _super);
        function GiveMoneyPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.GiveMoneyPanelSkin";
            return _this;
        }
        /**添加到场景中*/
        GiveMoneyPanel.prototype.onEnable = function () {
            this.getMoneyBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**从场景中移除*/
        GiveMoneyPanel.prototype.onRemove = function () {
            this.getMoneyBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**接收参数 */
        GiveMoneyPanel.prototype.recDataFun = function (data) {
            this.recData = data;
            var giveMoneyData = Tpm.ProtocolHttpData.GiveMoneyData.data;
            giveMoneyData = data;
            var money = Tpm.NumberTool.sperateMoney(giveMoneyData.money);
            this.contentText.text = "您的金币不足！系统赠送您" + money + "金币，今天第" + Tpm.NumberTool.formatCapital(giveMoneyData.income_support_times) + "次领取，一共可领取三次";
            this.moneyText.text = money;
        };
        GiveMoneyPanel.prototype.onSure = function (e) {
            Tpm.HallHttpDataSend.sendGetIncomeSupport();
        };
        return GiveMoneyPanel;
    }(Tpm.BasePanel));
    Tpm.GiveMoneyPanel = GiveMoneyPanel;
    __reflect(GiveMoneyPanel.prototype, "Tpm.GiveMoneyPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GiveMoneyPanel.js.map