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
    var MoneyNotEnoughPanel = (function (_super) {
        __extends(MoneyNotEnoughPanel, _super);
        function MoneyNotEnoughPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.MoneyNotEnoughPanelSkin;
            return _this;
        }
        /**添加到场景中*/
        MoneyNotEnoughPanel.prototype.onEnable = function () {
            this.buyMoneyBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**从场景中移除*/
        MoneyNotEnoughPanel.prototype.onRemove = function () {
            this.buyMoneyBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onSure, this);
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**接收参数 */
        MoneyNotEnoughPanel.prototype.recDataFun = function (data) {
            this.recData = data;
            var moneyNotEnoughData = Tpm.ProtocolHttpData.MoneyNotEnoughData;
            var lowestmoney = Tpm.NumberTool.sperateMoney(moneyNotEnoughData.lowestmoney);
            var money = Tpm.NumberTool.sperateMoney(moneyNotEnoughData.quantity);
            var type = moneyNotEnoughData.type;
            //"fontFamily":"楷体"
            var tetleTextStyleJson = { "size": 28, "textColor": 0xFCEFDC, "fontFamily": "Microsoft YaHei" };
            var contentTextStyleJson = { "size": 28, "textColor": 0xFFEB00, "fontFamily": "SimHei", "bold": "true" };
            this.tipsText.textFlow = [{ text: "您需要拥有  ", style: tetleTextStyleJson },
                { text: lowestmoney + "金币", style: contentTextStyleJson },
                { text: "才能进入" + type + "级场", style: tetleTextStyleJson }];
            this.moneyText.text = money;
            this.priceText.text = "价值" + moneyNotEnoughData.selling_price + "元";
        };
        /**更新推荐商品 */
        MoneyNotEnoughPanel.prototype.updateRecommendGood = function (data) {
            var recommendGood = Tpm.ProtocolHttpData.MoneyNotEnoughData;
            recommendGood = data;
            this.moneyText.text = recommendGood.quantity + "";
            this.priceText.text = "价值" + recommendGood.selling_price + "元";
        };
        MoneyNotEnoughPanel.prototype.onSure = function (e) {
        };
        return MoneyNotEnoughPanel;
    }(Tpm.BasePanel));
    Tpm.MoneyNotEnoughPanel = MoneyNotEnoughPanel;
    __reflect(MoneyNotEnoughPanel.prototype, "Tpm.MoneyNotEnoughPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=MoneyNotEnoughPanel.js.map