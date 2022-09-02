module Tpm {
    export class HuTipsItem extends eui.ItemRenderer {
        private posImg:eui.Image;
        private fanLab:eui.Label;
        private sheetLab:eui.Label;

        private itemCard: Card;

        public constructor() {
			super();
			this.skinName = TpmSkin.HuTipsItemSkin;
		}

        protected childrenCreated() {
			this.posImg.visible = false;
		}

        public dataChanged() {
            this.itemCard && this.itemCard.parent && this.removeChild(this.itemCard);

            var cardFactory:CardFactory = CardFactory.getInstance();
            this.itemCard = cardFactory.getHandCard(this.data.outCardValue, UserPosition.Down);
            this.itemCard.scaleX = this.itemCard.scaleY = 0.6;
            this.itemCard.x = 8;
            this.itemCard.y = 5;
            this.addChild(this.itemCard);

            this.fanLab.text = this.data.fanNum+"";
            this.sheetLab.text = this.data.residueNum+"";
		}
    }
}