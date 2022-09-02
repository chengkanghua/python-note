var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 麻将牌工厂
     */
    var CardFactory = (function () {
        function CardFactory() {
            this.cardPool = Tpm.ObjectPool.getPool(Tpm.Card.NAME);
        }
        CardFactory.getInstance = function () {
            if (this.instance == null) {
                this.instance = new CardFactory();
            }
            return this.instance;
        };
        /**
         * 获取手牌
         */
        CardFactory.prototype.getHandCard = function (cardValue, userPos, tingState) {
            if (tingState === void 0) { tingState = false; }
            var card = this.cardPool.getObject();
            if (Tpm.App.DataCenter.runingData.curentRoomType != Tpm.RoomType.noob) {
                card.setHandSkin(cardValue, userPos, tingState);
            }
            else {
                card.setHandSkin(cardValue, userPos);
            }
            //设置鼠标点击事件
            card.touchEnabled = (userPos == Tpm.UserPosition.Down) ? true : false;
            return card;
        };
        /**
         * 获取出牌
         */
        CardFactory.prototype.getOutCard = function (cardValue, userPos) {
            var card = this.cardPool.getObject();
            card.setOutSkin(cardValue, userPos);
            return card;
        };
        /**
         * 获取吃牌
         */
        CardFactory.prototype.getEatCard = function (cardValue, userPos) {
            var card = this.cardPool.getObject();
            card.setEatSkin(cardValue, userPos);
            return card;
        };
        /**
         * 获取暗杠牌
         */
        CardFactory.prototype.getAnGangCard = function (cardValue, userPos) {
            var card = this.cardPool.getObject();
            card.setAnGangSkin(cardValue, userPos);
            return card;
        };
        return CardFactory;
    }());
    Tpm.CardFactory = CardFactory;
    __reflect(CardFactory.prototype, "Tpm.CardFactory");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=CardFactory.js.map