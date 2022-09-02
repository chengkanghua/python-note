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
    var ResultPanel = (function (_super) {
        __extends(ResultPanel, _super);
        function ResultPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.ResultPanelSkin";
            return _this;
        }
        Object.defineProperty(ResultPanel.prototype, "cardFactory", {
            get: function () {
                return Tpm.CardFactory.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        ResultPanel.prototype.childrenCreated = function () {
        };
        ResultPanel.prototype.onEnable = function () {
            this.showResult();
            this.changeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onChange, this);
            this.changeBtnT.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onChange, this);
            this.continueBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onContinue, this);
            this.continueBtnT.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onContinue, this);
            this.backBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
        };
        ResultPanel.prototype.onRemove = function () {
            this.cardGro.removeChildren();
            this.changeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onChange, this);
            this.changeBtnT.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onChange, this);
            this.continueBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onContinue, this);
            this.continueBtnT.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onContinue, this);
            this.backBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
        };
        /**换对手 */
        ResultPanel.prototype.onChange = function () {
            Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene).clearDesk(false);
            Tpm.App.getController(Tpm.GameController.NAME).sendMod.sendReady();
            this.hide();
        };
        /**继续 */
        ResultPanel.prototype.onContinue = function () {
            Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene).clearDesk(false);
            Tpm.App.getController(Tpm.GameController.NAME).sendMod.sendReady();
            this.hide();
        };
        /**退出 */
        ResultPanel.prototype.onBack = function () {
            var readyMod = Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene).readyMod;
            readyMod.visible = true;
            readyMod.setState(Tpm.ReadyState.ready_00);
            this.hide();
        };
        ResultPanel.prototype.showResult = function () {
            var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101006);
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101006.info;
            revData = data.info;
            var result;
            if (revData.detail[0].params.hu_seat_id == Tpm.App.DataCenter.UserInfo.myUserInfo.seatID) {
                result = ResultType.win;
            }
            else if (revData.detail[0].params.hu_seat_id == -1) {
                result = ResultType.liu;
                this.showResultType(result);
                return;
            }
            else {
                result = ResultType.lose;
            }
            this.showResultType(result);
            var cardList = Tpm.ArrayTool.deepCopy(revData.detail[0].params.hand_card_for_settle_show);
            this.showCardList(cardList);
            this.fanNumLab.text = revData.detail[0].params.hu_fan_count + "";
            if (Tpm.App.DataCenter.runingData.curentRoomType != Tpm.RoomType.noob) {
                this.guoGro.visible = true;
                this.guoTimesLab.text = revData.detail[0].params.guo_hu_count + "";
            }
            else {
                this.guoGro.visible = false;
            }
            var symbol = "+";
            this.goldLab.font = "tpm_result_win_fnt";
            if (revData.detail[0].points[Tpm.App.DataCenter.UserInfo.myUserInfo.seatID] < 0) {
                symbol = "";
                this.goldLab.font = "tpm_result_lose_fnt";
            }
            this.goldLab.text = symbol + revData.detail[0].points[Tpm.App.DataCenter.UserInfo.myUserInfo.seatID] + "";
            this.showFanType(revData.detail[0].params.type_list);
        };
        ResultPanel.prototype.showResultType = function (type) {
            switch (type) {
                case ResultType.liu:
                    this.liuGro.visible = true;
                    this.huGro.visible = false;
                    break;
                case ResultType.lose:
                    this.liuGro.visible = false;
                    this.huGro.visible = true;
                    this.loseBgGro.visible = true;
                    this.winBgGro.visible = false;
                    break;
                case ResultType.win:
                    this.liuGro.visible = false;
                    this.huGro.visible = true;
                    this.loseBgGro.visible = false;
                    this.winBgGro.visible = true;
                    break;
                default:
                    console.error("result type error");
                    break;
            }
        };
        ResultPanel.prototype.showFanType = function (data) {
            var arr = [];
            for (var i = 0; i < data.length; i++) {
                var item = {
                    name: "",
                    fan: 0
                };
                item.name = Tpm.HuType.HuTypeName[data[i]];
                item.fan = Tpm.HuType.getHuTypeFan(data[i]);
                arr.push(item);
            }
            var ac = new eui.ArrayCollection();
            ac.source = arr;
            this.fanList.itemRenderer = Tpm.ResultFanItem;
            this.fanList.dataProvider = ac;
        };
        /**
         * @param [[17,17,17], [17,17,17,17], [17,0,0,0], [1,1,1], [17]]
         * 数组含义：吃碰，明杠，暗杠，手牌，胡牌
         */
        ResultPanel.prototype.showCardList = function (cardValueList) {
            var eatLen = 0;
            var beginPos = 70;
            var pos = Tpm.UserPosition.Down;
            for (var j = 0; j < cardValueList.length; j++) {
                var item = cardValueList[j];
                if (j == cardValueList.length - 1) {
                    var card = this.cardFactory.getHandCard(item[0], pos);
                    card.x = Tpm.CardPos.moCardPosXList[pos];
                    card.y = 14;
                    this.cardGro.addChild(card);
                }
                else if (j == cardValueList.length - 2) {
                    var handLen = 0;
                    for (var i = 0; i < item.length; i++) {
                        var card = this.cardFactory.getHandCard(item[i], pos);
                        card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * (3 * eatLen + handLen);
                        card.y = 14;
                        this.cardGro.addChild(card);
                        handLen++;
                    }
                }
                else if (item.length == 3) {
                    for (var i = 0; i < 3; i++) {
                        var card = this.cardFactory.getEatCard(item[i], pos);
                        card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * 3 * eatLen + Tpm.CardPos.eatCardGapList[pos] * i;
                        card.y = 37;
                        this.cardGro.addChild(card);
                    }
                    eatLen++;
                }
                else if (item.length == 4 && item[1] != 0) {
                    for (var i = 0; i < 4; i++) {
                        var card = this.cardFactory.getEatCard(item[i], pos);
                        if (i < 3) {
                            card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * 3 * eatLen + Tpm.CardPos.eatCardGapList[pos] * i;
                            card.y = 37;
                        }
                        else {
                            card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * 3 * eatLen + Tpm.CardPos.eatCardGapList[pos] * 1;
                            card.y = 37 - 22;
                        }
                        this.cardGro.addChild(card);
                    }
                    eatLen++;
                }
                else if (item.length == 4 && item[1] == 0) {
                    item[3] = item[0];
                    item[0] = 0;
                    for (var i = 0; i < 4; i++) {
                        if (i < 3) {
                            var card = this.cardFactory.getAnGangCard(item[i], pos);
                            card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * 3 * eatLen + Tpm.CardPos.eatCardGapList[pos] * i;
                            card.y = 37;
                            this.cardGro.addChild(card);
                        }
                        else {
                            var card = this.cardFactory.getEatCard(item[i], pos);
                            card.x = beginPos + Tpm.CardPos.handCardGapList[pos] * 3 * eatLen + Tpm.CardPos.eatCardGapList[pos] * 1;
                            card.y = 37 - 22;
                            this.cardGro.addChild(card);
                        }
                    }
                    eatLen++;
                }
            }
        };
        return ResultPanel;
    }(Tpm.BasePanel));
    Tpm.ResultPanel = ResultPanel;
    __reflect(ResultPanel.prototype, "Tpm.ResultPanel");
    var ResultType;
    (function (ResultType) {
        ResultType[ResultType["win"] = 0] = "win";
        ResultType[ResultType["lose"] = 1] = "lose";
        ResultType[ResultType["liu"] = 2] = "liu";
    })(ResultType || (ResultType = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ResultPanel.js.map