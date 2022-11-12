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
    var ShopMallItem = (function (_super) {
        __extends(ShopMallItem, _super);
        function ShopMallItem() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.ShopMallItemSkin;
            return _this;
        }
        ShopMallItem.prototype.dataChanged = function () {
            var goodsListItemData = Tpm.ProtocolHttpData.GoodsListItemData;
            goodsListItemData = this.data;
            this.moneyIcon.source = "tpm_moneyIcon" + goodsListItemData.icon + "_png";
            this.moneyText.text = goodsListItemData.title; //NumberTool.sperateMoney(goodsListItemData.title);
            this.priceText.text = "价值" + goodsListItemData.rmb_price + "元";
            this.buyBtn.getChildAt(2).text = goodsListItemData.selling_price + "";
            this.id = goodsListItemData.id;
        };
        ShopMallItem.prototype.childrenCreated = function () {
            this.buyBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBuy, this);
        };
        ShopMallItem.prototype.onBuy = function (e) {
            Tpm.HallHttpDataSend.sendBuyProp(this.id);
        };
        return ShopMallItem;
    }(eui.ItemRenderer));
    Tpm.ShopMallItem = ShopMallItem;
    __reflect(ShopMallItem.prototype, "Tpm.ShopMallItem");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ShopMallItem.js.map