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
    var ShopMallPanel = (function (_super) {
        __extends(ShopMallPanel, _super);
        function ShopMallPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.ShopMallPanelSkin";
            return _this;
        }
        /**添加到场景中*/
        ShopMallPanel.prototype.onEnable = function () {
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        ShopMallPanel.prototype.recDataFun = function (data) {
            var ac = new eui.ArrayCollection();
            var arr = [];
            var revData = Tpm.ProtocolHttpData.GoodsListData.data;
            revData = data;
            var len = revData.length;
            for (var i = 0; i < len; i++) {
                var itemData = Tpm.ArrayTool.deepCopy(Tpm.ProtocolHttpData.GoodsListItemData);
                itemData.icon = revData[i].icon;
                itemData.id = revData[i].id;
                itemData.selling_price = revData[i].selling_price;
                itemData.rmb_price = revData[i].rmb_price;
                itemData.title = revData[i].title;
                arr.push(itemData);
            }
            ac.source = arr;
            this.mallList.itemRenderer = Tpm.ShopMallItem;
            this.mallList.dataProvider = ac;
        };
        /**从场景中移除*/
        ShopMallPanel.prototype.onRemove = function () {
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        return ShopMallPanel;
    }(Tpm.BasePanel));
    Tpm.ShopMallPanel = ShopMallPanel;
    __reflect(ShopMallPanel.prototype, "Tpm.ShopMallPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ShopMallPanel.js.map