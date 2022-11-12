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
    var GameOutShowMod = (function (_super) {
        __extends(GameOutShowMod, _super);
        function GameOutShowMod() {
            var _this = _super.call(this) || this;
            _this.durationTime = 2000;
            _this.skinName = TpmSkin.GameOutShowModSkin;
            return _this;
        }
        GameOutShowMod.prototype.childrenCreated = function () {
        };
        GameOutShowMod.prototype.onEnable = function () {
            this.upGro.visible = false;
            this.downGro.visible = false;
        };
        GameOutShowMod.prototype.onRemove = function () {
            egret.Tween.removeTweens(this);
        };
        GameOutShowMod.prototype.showOutCard = function (cardValue, pos) {
            Tpm.App.DataCenter.runingData.latelyCardValue = cardValue;
            if (!this.upCard) {
                this.initCard();
            }
            if (pos == Tpm.UserPosition.Down) {
                this.upGro.visible = false;
                this.downGro.visible = true;
                this.startHide(this.downGro);
                this.downCard.setCardValueAndSHow(cardValue);
            }
            else {
                this.upGro.visible = true;
                this.downGro.visible = false;
                this.startHide(this.upGro);
                this.upCard.setCardValueAndSHow(cardValue);
            }
        };
        GameOutShowMod.prototype.initCard = function () {
            var origX = 20;
            var origY = 17;
            var cardFactory = Tpm.CardFactory.getInstance();
            this.upCard = cardFactory.getHandCard(0, Tpm.UserPosition.Down);
            this.upGro.addChild(this.upCard);
            this.upCard.x = origX;
            this.upCard.y = origY;
            this.downCard = cardFactory.getHandCard(0, Tpm.UserPosition.Down);
            this.downGro.addChild(this.downCard);
            this.downCard.x = origX;
            this.downCard.y = origY;
        };
        GameOutShowMod.prototype.startHide = function (gro) {
            egret.Tween.get(this)
                .wait(this.durationTime)
                .call(function () {
                gro.visible = false;
            });
        };
        return GameOutShowMod;
    }(Tpm.BaseUI));
    Tpm.GameOutShowMod = GameOutShowMod;
    __reflect(GameOutShowMod.prototype, "Tpm.GameOutShowMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameOutShowMod.js.map