module Tpm {
    /**
     * 麻将牌工厂
     */
    export class CardFactory {
        private cardPool: ObjectPool;

        public constructor() {
            this.cardPool = ObjectPool.getPool(Card.NAME);
        }

        private static instance: CardFactory;
        public static getInstance(): CardFactory {
            if (this.instance == null) {
                this.instance = new CardFactory();
            }
            return this.instance;
        }

        /**
         * 获取手牌
         */
        public getHandCard(cardValue: number, userPos: UserPosition, tingState: boolean = false): Card {
            var card: Card = this.cardPool.getObject();
            if (App.DataCenter.runingData.curentRoomType != RoomType.noob) {
                card.setHandSkin(cardValue, userPos, tingState);
            }
            else {
                 card.setHandSkin(cardValue, userPos);
            }
           
            //设置鼠标点击事件
            card.touchEnabled = (userPos == UserPosition.Down) ? true : false;
            return card;
        }

        /**
         * 获取出牌
         */
        public getOutCard(cardValue: number, userPos: UserPosition): Card {
            var card: Card = this.cardPool.getObject();
            card.setOutSkin(cardValue, userPos);
            return card;
        }

        /**
         * 获取吃牌
         */
        public getEatCard(cardValue: number, userPos: UserPosition): Card {
            var card: Card = this.cardPool.getObject();
            card.setEatSkin(cardValue, userPos);
            return card;
        }

        /**
         * 获取暗杠牌
         */
        public getAnGangCard(cardValue: number, userPos: UserPosition) {
            var card: Card = this.cardPool.getObject();
            card.setAnGangSkin(cardValue, userPos);
            return card;
        }
    }
}
