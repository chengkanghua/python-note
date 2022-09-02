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
    var HuTipsItem = (function (_super) {
        __extends(HuTipsItem, _super);
        function HuTipsItem() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.HuTipsItemSkin;
            return _this;
        }
        HuTipsItem.prototype.childrenCreated = function () {
            this.posImg.visible = false;
        };
        HuTipsItem.prototype.dataChanged = function () {
            this.itemCard && this.itemCard.parent && this.removeChild(this.itemCard);
            var cardFactory = Tpm.CardFactory.getInstance();
            this.itemCard = cardFactory.getHandCard(this.data.outCardValue, Tpm.UserPosition.Down);
            this.itemCard.scaleX = this.itemCard.scaleY = 0.6;
            this.itemCard.x = 8;
            this.itemCard.y = 5;
            this.addChild(this.itemCard);
            this.fanLab.text = this.data.fanNum + "";
            this.sheetLab.text = this.data.residueNum + "";
        };
        return HuTipsItem;
    }(eui.ItemRenderer));
    Tpm.HuTipsItem = HuTipsItem;
    __reflect(HuTipsItem.prototype, "Tpm.HuTipsItem");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HuTipsItem.js.map