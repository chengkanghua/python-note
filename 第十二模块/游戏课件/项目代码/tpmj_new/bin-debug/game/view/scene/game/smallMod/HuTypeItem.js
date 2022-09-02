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
    var HuTypeItem = (function (_super) {
        __extends(HuTypeItem, _super);
        function HuTypeItem() {
            var _this = _super.call(this) || this;
            _this.cardList = [];
            _this.skinName = TpmSkin.huTypeItemSkin;
            _this.touchEnabled = true;
            return _this;
        }
        HuTypeItem.prototype.dataChanged = function () {
            this.cardList = this.data.cardList;
            this.huLabel.text = this.data.hulabel;
            this.setCardList(this.cardList);
        };
        HuTypeItem.prototype.childrenCreated = function () {
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        HuTypeItem.prototype.onTouch = function () {
            var json = Tpm.ProtocolDataSend.S_100999;
            json.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
            json.test_type = 4;
            var param = {
                source_card: [],
                target_card: []
            };
            param.target_card = this.cardList;
            json.test_params = JSON.stringify(param);
            Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100999, json);
            Tpm.Tips.showTop("发送成功");
            Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene).cheatMod.setFanGro(false);
        };
        HuTypeItem.prototype.setCardList = function (cardList) {
            var len = cardList.length;
            var card;
            var cardFactory = Tpm.CardFactory.getInstance();
            for (var i = 0; i < len; i++) {
                card = cardFactory.getOutCard(cardList[i], Tpm.UserPosition.Up);
                card.x = 46 * i;
                card.y = 0;
                this.cardListGroup.addChild(card);
            }
        };
        return HuTypeItem;
    }(eui.ItemRenderer));
    Tpm.HuTypeItem = HuTypeItem;
    __reflect(HuTypeItem.prototype, "Tpm.HuTypeItem");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HuTypeItem.js.map