module Tpm {
    export class GameOutShowMod extends BaseUI {
        private upGro:eui.Group;
        private downGro:eui.Group;

        private upCard: Card;
        private downCard: Card;
        private durationTime: number = 2000;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameOutShowModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.upGro.visible = false;
            this.downGro.visible = false;
        }

        protected onRemove() {
            egret.Tween.removeTweens(this);
        }

        public showOutCard(cardValue: number, pos: UserPosition) {
            App.DataCenter.runingData.latelyCardValue = cardValue;
            if (!this.upCard) {
                this.initCard();
            }

            if (pos == UserPosition.Down) {
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
        }

        private initCard() {
            var origX = 20;
            var origY = 17;
            var cardFactory: CardFactory = CardFactory.getInstance();
            this.upCard = cardFactory.getHandCard(0, UserPosition.Down);
            this.upGro.addChild(this.upCard);
            this.upCard.x = origX;
            this.upCard.y = origY;

            this.downCard = cardFactory.getHandCard(0, UserPosition.Down);
            this.downGro.addChild(this.downCard);
            this.downCard.x = origX;
            this.downCard.y = origY;
        }

        private startHide(gro: eui.Group) {
            egret.Tween.get(this)
            .wait(this.durationTime)
            .call(()=>{
                gro.visible = false;
            })
        }
    }
}