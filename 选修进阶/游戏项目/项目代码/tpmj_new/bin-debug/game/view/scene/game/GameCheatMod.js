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
    /**
     * 作弊模块
     */
    var GameCheatMod = (function (_super) {
        __extends(GameCheatMod, _super);
        function GameCheatMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameCheatModSkin;
            return _this;
        }
        GameCheatMod.prototype.childrenCreated = function () {
            this.selectGroup = new eui.Group();
        };
        GameCheatMod.prototype.onEnable = function () {
            var _this = this;
            this.state = false;
            this.reShowState(this.state);
            this.setFanGro(false);
            this.setFanData();
            if (Tpm.App.DataCenter.debugInfo.testState) {
                this.init();
            }
            else {
                this.visible = false;
            }
            this.fanGro.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.setFanGro(false);
            }, this);
        };
        GameCheatMod.prototype.onRemove = function () {
        };
        GameCheatMod.prototype.init = function () {
            var _this = this;
            this.ruleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onRule, this);
            this.changeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.curSelcet = 0;
                _this.showSwapCard();
            }, this);
            this.changeToBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.curSelcet = 1;
                _this.showSwapCard();
            }, this);
            this.nextBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.curSelcet = 2;
                _this.showSwapCard();
            }, this);
            this.lastBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                // 最后一张
                var json = Tpm.ProtocolDataSend.S_100999;
                json.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
                json.test_type = 3;
                var param = {
                    source_card: [],
                    target_card: []
                };
                json.test_params = JSON.stringify(param);
                Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100999, json);
            }, this);
            this.huBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.selectGroup.parent && _this.removeChild(_this.selectGroup);
                // 牌型
                _this.setFanGro(true);
            }, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.selectGroup.parent && _this.removeChild(_this.selectGroup);
                // 断线
                Tpm.App.gameSocket.close();
                Tpm.App.EventManager.sendEvent(Tpm.EventConst.SocketClose, Tpm.App.gameSocket);
            }, this);
            this.jiesanBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.selectGroup.parent && _this.removeChild(_this.selectGroup);
                _this.ctrl.sendMod.sendJieSanTest();
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
        };
        Object.defineProperty(GameCheatMod.prototype, "cardFactory", {
            get: function () {
                return Tpm.CardFactory.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        GameCheatMod.prototype.onRule = function () {
            this.state = !this.state;
            this.reShowState(this.state);
        };
        GameCheatMod.prototype.reShowState = function (show) {
            if (show) {
                this.allGro.x = 0;
            }
            else {
                this.allGro.x = -200;
            }
        };
        GameCheatMod.prototype.showSwapCard = function () {
            var _this = this;
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
            var sp = new egret.Sprite();
            sp.graphics.beginFill(0, 0.5);
            sp.graphics.drawRect(0, 0, groupWidth, groupHeight);
            sp.touchEnabled = true;
            sp.addEventListener(egret.TouchEvent.TOUCH_TAP, function () {
                _this.selectGroup.parent && _this.removeChild(_this.selectGroup);
            }, this);
            this.selectGroup.addChild(sp);
            this.addChild(this.selectGroup);
            var card;
            for (var i = 0; i < 9; i++) {
                card = this.cardFactory.getOutCard(17 + i, 0);
                card.x = cardWidth * i;
                card.y = 0 + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8;
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            for (var i = 0; i < 4; i++) {
                card = this.cardFactory.getOutCard(65 + i, 0);
                card.x = cardWidth * i;
                card.y = cardHeight + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8;
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            for (var i = 4; i < 7; i++) {
                card = this.cardFactory.getOutCard(77 + i, 0);
                card.x = cardWidth * i;
                card.y = cardHeight + 10;
                card.scaleX = 0.8;
                card.scaleY = 0.8;
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            this.tipsLabel = new eui.Label();
            this.tipsLabel.x = cardWidth * 7 + 10;
            this.tipsLabel.y = cardHeight + 10 + 10;
            this.tipsLabel.textColor = Tpm.App.ArtConfig.getColor(Tpm.ColorConst.white);
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
                card.scaleY = 0.8;
                card.touchEnabled = true;
                this.selectGroup.addChild(card);
            }
            this.selectGroup.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onSelect, this);
        };
        GameCheatMod.prototype.onSelect = function (e) {
            if (e.target instanceof Tpm.Card) {
                var card = e.target;
                if (this.curSelcet == 0) {
                    this.selectValue0 = card.cardValue;
                    this.card_s0.setCardValueAndShowOut(this.selectValue0);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                }
                else if (this.curSelcet == 1) {
                    this.selectValue1 = card.cardValue;
                    var json = Tpm.ProtocolDataSend.S_100999;
                    json.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
                    json.test_type = 1;
                    var param = {
                        source_card: [],
                        target_card: []
                    };
                    param.source_card.push(this.selectValue0);
                    param.target_card.push(this.selectValue1);
                    json.test_params = JSON.stringify(param);
                    Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100999, json);
                    console.log("发送换牌:", this.selectValue0, this.selectValue1);
                    this.card_s1.setCardValueAndShowOut(this.selectValue1);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                }
                else if (this.curSelcet == 2) {
                    var nextCardJson = Tpm.ProtocolDataSend.S_100999;
                    nextCardJson.user_id = Tpm.App.DataCenter.UserInfo.myUserUid;
                    nextCardJson.test_type = 2;
                    var param = {
                        source_card: [],
                        target_card: []
                    };
                    param.target_card.push(card.cardValue);
                    nextCardJson.test_params = JSON.stringify(param);
                    Tpm.App.gameSocket.send(Tpm.ProtocolHeadSend.S_100999, nextCardJson);
                    console.log("发送确认下一张牌，牌值", card.cardValue);
                    this.card_s2.setCardValueAndShowOut(card.cardValue);
                    this.selectGroup.parent && this.removeChild(this.selectGroup);
                }
            }
        };
        GameCheatMod.prototype.clearSelect = function () {
            this.selectValue0 = 0;
            this.selectValue1 = 0;
            this.card_s0.setCardValueAndShowOut(0);
            this.card_s1.setCardValueAndShowOut(0);
        };
        GameCheatMod.prototype.setFanGro = function (show) {
            this.fanGro.visible = show;
        };
        GameCheatMod.prototype.setFanData = function () {
            var ac = new eui.ArrayCollection();
            var arr = [];
            arr.push({ "cardList": [17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 22, 98], "hulabel": "补一花" });
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 18, 20, 21, 21, 22, 22, 97, 98], "hulabel": "起手杠" });
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 18, 20, 20, 20, 20, 22, 97, 98], "hulabel": "起手杠2" });
            arr.push({ "cardList": [18, 18, 18, 19, 19, 19, 20, 20, 20, 23, 24, 25, 82, 82], "hulabel": "三暗刻" });
            arr.push({ "cardList": [17, 17, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 25], "hulabel": "九莲宝灯" });
            arr.push({ "cardList": [17, 18, 19, 21, 21, 21, 23, 23, 23, 81, 81, 81, 65, 65], "hulabel": "混一色" });
            arr.push({ "cardList": [17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 18, 19, 82, 82], "hulabel": "清龙" });
            arr.push({ "cardList": [19, 20, 21, 20, 21, 22, 21, 22, 23, 20, 21, 22, 82, 82], "hulabel": "一色三步高" });
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 17, 18, 19, 20, 21, 22, 82, 82], "hulabel": "一色三同顺" });
            arr.push({ "cardList": [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 25, 81, 81], "hulabel": "一色三节高" });
            arr.push({ "cardList": [18, 19, 20, 19, 20, 21, 20, 21, 22, 21, 22, 23, 68, 68], "hulabel": "一色四步高" });
            arr.push({ "cardList": [17, 17, 22, 22, 23, 23, 24, 24, 25, 25, 66, 66, 82, 82], "hulabel": "七对" });
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 20, 21, 22, 23, 24, 25, 17, 17], "hulabel": "清一色" });
            arr.push({ "cardList": [17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 25, 25], "hulabel": "一色四同顺" });
            arr.push({ "cardList": [17, 17, 17, 25, 25, 25, 67, 67, 67, 83, 83, 83, 65, 65], "hulabel": "混幺九" });
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 68, 68, 23, 23, 23], "hulabel": "小四喜" });
            arr.push({ "cardList": [81, 81, 81, 82, 82, 82, 83, 83, 17, 17, 17, 18, 19, 20], "hulabel": "小三元" });
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 82, 82, 82, 83, 83], "hulabel": "字一色" });
            arr.push({ "cardList": [17, 18, 19, 17, 18, 19, 21, 21, 23, 24, 25, 23, 24, 25], "hulabel": "一色双龙会" });
            arr.push({ "cardList": [65, 65, 65, 66, 66, 66, 67, 67, 67, 68, 68, 68, 23, 23], "hulabel": "大四喜" });
            arr.push({ "cardList": [81, 81, 81, 82, 82, 82, 83, 83, 83, 17, 17, 18, 19, 20], "hulabel": "大三元" });
            arr.push({ "cardList": [17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23], "hulabel": "七连对" });
            ac.source = arr;
            this.cardList.dataProvider = ac;
            this.cardList.itemRenderer = Tpm.HuTypeItem;
        };
        return GameCheatMod;
    }(Tpm.BaseGameMod));
    Tpm.GameCheatMod = GameCheatMod;
    __reflect(GameCheatMod.prototype, "Tpm.GameCheatMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameCheatMod.js.map