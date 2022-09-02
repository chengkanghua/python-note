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
    var GameEatChooseMod = (function (_super) {
        __extends(GameEatChooseMod, _super);
        function GameEatChooseMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameEatChooseModSkin;
            return _this;
        }
        GameEatChooseMod.prototype.childrenCreated = function () {
            this.initRectList();
            this.twoCardList = [[], []];
            this.threeCardList = [[], [], []];
        };
        GameEatChooseMod.prototype.onEnable = function () {
            for (var i = 0; i < this.rectList.length; i++) {
                this.rectList[i].addEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            }
            this.cancleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        };
        GameEatChooseMod.prototype.onRemove = function () {
            for (var i = 0; i < this.rectList.length; i++) {
                this.rectList[i].removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            }
            this.cancleBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        };
        GameEatChooseMod.prototype.initRectList = function () {
            this.rectList = [];
            for (var i = 0; i < 2; i++) {
                this.rectList.push(this.twoGro.getChildAt(i + 2));
            }
            for (var i = 0; i < 3; i++) {
                this.rectList.push(this.threeGro.getChildAt(i + 3));
            }
        };
        /**选择 */
        GameEatChooseMod.prototype.onChoose = function (e) {
            var target = e.target;
            var chooseList;
            switch (target) {
                case this.rectList[0]:
                    chooseList = this.tValueList[0];
                    break;
                case this.rectList[1]:
                    chooseList = this.tValueList[1];
                    break;
                case this.rectList[2]:
                    chooseList = this.tValueList[0];
                    break;
                case this.rectList[3]:
                    chooseList = this.tValueList[1];
                    break;
                case this.rectList[4]:
                    chooseList = this.tValueList[2];
                    break;
                default:
                    console.error("eat choose error");
                    break;
            }
            if (!chooseList || chooseList.length < 3) {
                console.error("eat choose list error");
                return;
            }
            console.log("chooseList===", chooseList);
            this.hideCombo();
            this.dispatchEventWith("selectComboEvent", false, chooseList);
        };
        /**取消 */
        GameEatChooseMod.prototype.onCancle = function () {
            this.hideCombo();
            this.gameScene.selectBtnMod.reShow();
        };
        GameEatChooseMod.prototype.showCombo = function (valueList) {
            if (!valueList || valueList.length < 2 || valueList[0].length < 3) {
                console.error("param error");
                return;
            }
            this.tValueList = valueList;
            if (this.twoCardList[0].length < 1) {
                this.initCard();
            }
            var eatLen = 3;
            var curentCardList;
            if (valueList.length == 2) {
                this.twoGro.visible = true;
                this.threeGro.visible = false;
                curentCardList = this.twoCardList;
            }
            else if (valueList.length == 3) {
                this.twoGro.visible = false;
                this.threeGro.visible = true;
                curentCardList = this.threeCardList;
            }
            valueList.sort(function (a, b) {
                return a[0] - b[0];
            });
            for (var i = 0; i < valueList.length; i++) {
                for (var j = 0; j < eatLen; j++) {
                    valueList[i].sort(function (a, b) {
                        return a - b;
                    });
                    curentCardList[i][j].setCardValueAndSHow(valueList[i][j]);
                }
            }
            this.visible = true;
        };
        /**隐藏 */
        GameEatChooseMod.prototype.hideCombo = function () {
            this.visible = false;
        };
        GameEatChooseMod.prototype.initCard = function () {
            var eatLen = 3;
            var xGap = 60;
            var origX = 10;
            var origY = 10;
            var scaleAll = 0.65;
            var cardFactory = Tpm.CardFactory.getInstance();
            for (var i = 0; i < this.twoCardList.length; i++) {
                for (var j = 0; j < eatLen; j++) {
                    var tCard = cardFactory.getHandCard(0, Tpm.UserPosition.Down);
                    this.twoGro.getChildAt(i).addChild(tCard);
                    tCard.x = origX + xGap * j;
                    tCard.y = origY;
                    tCard.scaleX = tCard.scaleY = scaleAll;
                    this.twoCardList[i].push(tCard);
                }
            }
            for (var i = 0; i < this.threeCardList.length; i++) {
                for (var j = 0; j < eatLen; j++) {
                    var tCard = cardFactory.getHandCard(0, Tpm.UserPosition.Down);
                    this.threeGro.getChildAt(i).addChild(tCard);
                    tCard.x = origX + xGap * j;
                    tCard.y = origY;
                    tCard.scaleX = tCard.scaleY = scaleAll;
                    this.threeCardList[i].push(tCard);
                }
            }
        };
        return GameEatChooseMod;
    }(Tpm.BaseGameMod));
    Tpm.GameEatChooseMod = GameEatChooseMod;
    __reflect(GameEatChooseMod.prototype, "Tpm.GameEatChooseMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameEatChooseMod.js.map