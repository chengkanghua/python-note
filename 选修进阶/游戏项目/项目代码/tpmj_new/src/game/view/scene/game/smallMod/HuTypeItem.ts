module Tpm {
    export class HuTypeItem extends eui.ItemRenderer {
        public constructor() {
            super();
            this.skinName = TpmSkin.huTypeItemSkin;
            this.touchEnabled = true;
        }

        private cardListGroup: eui.Group;
        private huLabel: eui.Label;
        private cardList = [];

        public dataChanged(): void {
            this.cardList = this.data.cardList;
            this.huLabel.text = this.data.hulabel;
            this.setCardList(this.cardList);
        }


        protected childrenCreated() {
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        }


        private onTouch() {
            var json = ProtocolDataSend.S_100999;
            json.user_id = App.DataCenter.UserInfo.myUserUid;
            json.test_type = 4;
            var param = {
                source_card: [],
                target_card: []
            }
            param.target_card = this.cardList;
            json.test_params = JSON.stringify(param);
            App.gameSocket.send(ProtocolHeadSend.S_100999, json);

            Tips.showTop("发送成功");
            (<GameScene>App.SceneManager.getScene(SceneConst.GameScene)).cheatMod.setFanGro(false);
        }

        public setCardList(cardList) {
            var len = cardList.length;
            var card: Card;
            var cardFactory: CardFactory = CardFactory.getInstance();
            for (var i = 0; i < len; i++) {
                card = cardFactory.getOutCard(cardList[i], UserPosition.Up);
                card.x = 46* i;
                card.y = 0;
                this.cardListGroup.addChild(card);
            }
        }
    }
}
