module Tpm {
    /**
     * 作弊模块 
     */
    export class GameCheatMod extends BaseGameMod {
        private allGro: eui.Group;
        private ruleBtn: eui.Button;
        private changeBtn: eui.Button;
        private changeToBtn: eui.Button;
        private nextBtn: eui.Button;
        private huBtn: eui.Button;
        private closeBtn: eui.Button;
        private btnBro: eui.Group;
        private lastBtn: eui.Button;
        private fanGro: eui.Group;
        private cardList: eui.List;
        public jiesanBtn:eui.Button;

        private state: boolean;
        private selectGroup: eui.Group;
        private curSelcet: number;
        private tipsLabel: eui.Label;

        public selectValue0: number;
        public selectValue1: number;
        private card_s0: Card;
        private card_s1: Card;
        private card_s2: Card;
        public card_s3: Card;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameCheatModSkin;
        }

        protected childrenCreated() {
            this.selectGroup = new eui.Group();
        }

        protected onEnable() {
            this.state = false;
            this.reShowState(this.state);
            this.setFanGro(false);
            this.setFanData();

            if (App.DataCenter.debugInfo.testState) {
                this.init();
            }
            else {
                this.visible = false;
            }
            this.fanGro.addEventListener(egret.TouchEvent.TOUCH_TAP, ()=>{
                this.setFanGro(false);
            }, this);
        }

        protected onRemove() {
        }

        private init() {
            this.ruleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRule, this);

            this.changeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.curSelcet = 0;
                this.showSwapCard();
            }, this);
            this.changeToBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.curSelcet = 1;
                this.showSwapCard();
            }, this);
            this.nextBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.curSelcet = 2;
                this.showSwapCard();
            }, this);
            this.lastBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                // 最后一张
                var json = ProtocolDataSend.S_100999;
                json.user_id = App.DataCenter.UserInfo.myUserUid;
                json.test_type = 3;
                var param = {
                    source_card: [],
                    target_card: []
                }
                json.test_params = JSON.stringify(param);
                App.gameSocket.send(ProtocolHeadSend.S_100999, json);
            }, this);
            this.huBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.selectGroup.parent && this.removeChild(this.selectGroup);
                // 牌型
                this.setFanGro(true);
            }, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.selectGroup.parent && this.removeChild(this.selectGroup);
                // 断线
                App.gameSocket.close();
                App.EventManager.sendEvent(EventConst.SocketClose, App.gameSocket);
            }, this);
            this.jiesanBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.selectGroup.parent && this.removeChild(this.selectGroup);
                this.ctrl.sendMod.sendJieSanTest();
            }, this);

            this.card_s0 = this.cardFactory.getOutCard(0, 0);
            this.card_s0.x = 145;
            this.card_s0.y = 10;
            this.card_s0.scaleX = this.card_s0.scaleY = 0.6;
            this.btnBro.addChild(this.card_s0);

            this.card_s1 = this.cardFactory.getOutCard(0, 0);
            this.card_s1.x = 145;
            this.card_s1.y = 10 + 60;
            this.card_s1.scaleX = this.card_s1.scaleY = 0.6;
            this.btnBro.addChild(this.card_s1);

            this.card_s2 = this.cardFactory.getOutCard(0, 0);
            this.card_s2.x = 145;
            this.card_s2.y = 10 + 60 * 2;
            this.card_s2.scaleX = this.card_s2.scaleY = 0.6;
            this.btnBro.addChild(this.card_s2);

            this.card_s3 = this.cardFactory.getOutCard(0, 0);
            this.card_s3.x = 145;
            this.card_s3.y = 10 + 60 * 3;
            this.card_s3.scaleX = this.card_s3.scaleY = 0.6;
            this.btnBro.addChild(this.card_s3);

        }

        private get cardFactory() {
            return CardFactory.getInstance();
        }

        private onRule() {
            this.state = !this.state;
            this.reShowState(this.state);
        }

        private reShowState(show: boolean) {
            if (show) {
                this.allGro.x = 0;
            }
            else {
                this.allGro.x = -200;
            }
        }

        private showSwapCard() {
            this.selectGroup.parent && this.removeChild(this.selectGroup);
            if (this.selectGroup.numChildren > 15) {
                this.addChild(this.selectGroup);
                var tips = "";
                if (this.curSelcet == 0) {
                    tips = "换牌前";
                }
                else if (this.curSelcet == 1) {
                    tips = "换牌后";
                }
                else if (this.curSelcet == 2) {
                    tips = "下一张";
                }
                this.tipsLabel.text = tips;
                return;
            }
            else {
                this.selectGroup.removeChildren();
            }
            var cardWidth = 58;
            var cardHeight = 81;
            var groupWidth = cardWidth * 9;
            var groupHeight = cardHeight * 3;
            this.selectGroup.width = groupWidth;
            this.selectGroup.height = groupHeight;
            this.selectGroup.x = 200;
            this.selectGroup.y = 130;
            var sp: egret.Sprite = new egret.Sprite();
            sp.graphics.beginFill(0, 0.5);
            sp.graphics.drawRect(0, 0, groupWidth, groupHeight);
            sp.touchEnabled = true;
            sp.addEventListener(egret.TouchEvent.TOUCH_TAP, () => {
                this.selectGroup.parent && this.removeChild(this.selectGroup);
            }, this);
            this.selectGroup.addChild(sp);
            this.addChild(this.selectGroup);

            var card: Card;

            for (var i = 0; i < 9; i++) {
                card = this.cardFactory.getOutCard(17 + i, 0);
                card.x = cardWidth * i;
                card.y = 0 + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            for (var i = 0; i < 4; i++) {
                card = this.cardFactory.getOutCard(65 + i, 0);
                card.x = cardWidth * i;
                card.y = cardHeight + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }

            for (var i = 4; i < 7; i++) {
                card = this.cardFactory.getOutCard(77 + i, 0);
                card.x = cardWidth * i;
                card.y = cardHeight + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            this.tipsLabel = new eui.Label();
            this.tipsLabel.x = cardWidth * 7 + 10;
            this.tipsLabel.y = cardHeight + 10 + 10;
            this.tipsLabel.textColor = App.ArtConfig.getColor(ColorConst.white);
            this.tipsLabel.touchEnabled = false;
            this.selectGroup.addChild(this.tipsLabel);
            var tips = "";
            if (this.curSelcet == 0) {
                tips = "换牌前";
            }
            else if (this.curSelcet == 1) {
                tips = "换牌后";
            }
            else if (this.curSelcet == 2) {
                tips = "下一张";
            }
            this.tipsLabel.text = tips;

            for (var i = 0; i < 8; i++) {
                card = this.cardFactory.getOutCard(97 + i, 0);
                card.x = cardWidth * i;
                card.y = cardHeight * 2 + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }

            this.selectGroup.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSelect, this);
        }

        private onSelect(e: egret.TouchEvent) {
            if (e.target instanceof Card) {
                var card: Card = e.target;
                if (this.curSelcet == 0) {
                    this.selectValue0 = card.cardValue;
                    this.card_s0.setCardValueAndShowOut(this.selectValue0);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                } else if (this.curSelcet == 1) {
                    this.selectValue1 = card.cardValue;
                    var json = ProtocolDataSend.S_100999;
                    json.user_id = App.DataCenter.UserInfo.myUserUid;
                    json.test_type = 1;
                    var param = {
                        source_card: [],
                        target_card: []
                    }
                    param.source_card.push(this.selectValue0);
                    param.target_card.push(this.selectValue1);
                    json.test_params = JSON.stringify(param);
                    App.gameSocket.send(ProtocolHeadSend.S_100999, json);
                    console.log("发送换牌:", this.selectValue0, this.selectValue1);
                    this.card_s1.setCardValueAndShowOut(this.selectValue1);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                } else if (this.curSelcet == 2) {
                    var nextCardJson = ProtocolDataSend.S_100999;
                    nextCardJson.user_id = App.DataCenter.UserInfo.myUserUid;
                    nextCardJson.test_type = 2;
                    var param = {
                        source_card: [],
                        target_card: []
                    }
                    param.target_card.push(card.cardValue);
                    nextCardJson.test_params = JSON.stringify(param);
                    App.gameSocket.send(ProtocolHeadSend.S_100999, nextCardJson);
                    console.log("发送确认下一张牌，牌值", card.cardValue);
                    this.card_s2.setCardValueAndShowOut(card.cardValue);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                }
            }
        }

        public clearSelect() {
            this.selectValue0 = 0;
            this.selectValue1 = 0;

            this.card_s0.setCardValueAndShowOut(0);
            this.card_s1.setCardValueAndShowOut(0);
        }

        public setFanGro(show: boolean) {
            this.fanGro.visible = show;
        }

        private setFanData() {
            let ac = new eui.ArrayCollection();
            let arr = [];
            arr.push({ "cardList": [17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 22, 98], "hulabel": "补一花" })
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 18, 20, 21, 21, 22, 22, 97, 98], "hulabel": "起手杠" })
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 18, 20, 20, 20, 20, 22, 97, 98], "hulabel": "起手杠2" })
            arr.push({ "cardList": [18, 18, 18, 19, 19, 19, 20, 20, 20, 23, 24, 25, 82, 82], "hulabel": "三暗刻" })
            arr.push({ "cardList": [17, 17, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25], "hulabel": "九莲宝灯" })
            arr.push({ "cardList": [17, 18, 19, 21, 21, 21, 23, 23, 23, 81, 81, 81, 65, 65], "hulabel": "混一色" })
            arr.push({ "cardList": [17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 18, 19, 82, 82], "hulabel": "清龙" })
            arr.push({ "cardList": [19, 20, 21, 20, 21, 22, 21, 22, 23, 20, 21, 22, 82, 82], "hulabel": "一色三步高" })
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 17, 18, 19, 20, 21, 22, 82, 82], "hulabel": "一色三同顺" })
            arr.push({ "cardList": [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 25, 81, 81], "hulabel": "一色三节高" })
            arr.push({ "cardList": [18, 19, 20, 19, 20, 21, 20, 21, 22, 21, 22, 23, 68, 68], "hulabel": "一色四步高" })
            arr.push({ "cardList": [17, 17, 22, 22, 23, 23, 24, 24, 25, 25, 66, 66, 82, 82], "hulabel": "七对" })
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 17], "hulabel": "清一色" })
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 25, 25], "hulabel": "一色四同顺" })
            arr.push({ "cardList": [17, 17, 17, 25, 25, 25, 67, 67, 67, 83, 83, 83, 65, 65], "hulabel": "混幺九" })
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 68, 68, 23, 23, 23], "hulabel": "小四喜" })
            arr.push({ "cardList": [81, 81, 81, 82, 82, 82, 83, 83, 17, 17, 17, 18, 19, 20], "hulabel": "小三元" })
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 82, 82, 82, 83, 83], "hulabel": "字一色" })
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 21, 21, 23, 24, 25, 23, 24, 25], "hulabel": "一色双龙会" })
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 68, 68, 68, 23, 23], "hulabel": "大四喜" })
            arr.push({ "cardList": [81, 81, 81, 82, 82, 82, 83, 83, 83, 17, 17, 18, 19, 20], "hulabel": "大三元" })
            arr.push({ "cardList": [17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23], "hulabel": "七连对" })

            ac.source = arr;
            this.cardList.dataProvider = ac;
            this.cardList.itemRenderer = HuTypeItem;
        }
    }
}