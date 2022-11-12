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
    var GameGangChooseMod = (function (_super) {
        __extends(GameGangChooseMod, _super);
        function GameGangChooseMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameGangChooseModSkin;
            return _this;
        }
        GameGangChooseMod.prototype.childrenCreated = function () {
            this.initRectList();
            this.twoCardList = [[], []];
            this.threeCardList = [[], [], []];
        };
        GameGangChooseMod.prototype.onEnable = function () {
            for (var i = 0; i < this.rectList.length; i++) {
                this.rectList[i].addEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            }
            this.cancleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        };
        GameGangChooseMod.prototype.onRemove = function () {
            for (var i = 0; i < this.rectList.length; i++) {
                this.rectList[i].removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onChoose, this);
            }
            this.cancleBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        };
        GameGangChooseMod.prototype.initRectList = function () {
            this.rectList = [];
            for (var i = 0; i < 2; i++) {
                this.rectList.push(this.twoGro.getChildAt(i + 2));
            }
            for (var i = 0; i < 3; i++) {
                this.rectList.push(this.threeGro.getChildAt(i + 3));
            }
        };
        /**选择 */
        GameGangChooseMod.prototype.onChoose = function (e) {
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
                    console.error("gang choose error");
                    break;
            }
            if (!chooseList || chooseList.length < 3) {
                console.error("gang choose list error");
            }
            console.log("chooseList===", chooseList);
            this.hideCombo();
            this.dispatchEventWith("selectComboEvent", false, chooseList);
        };
        /**取消 */
        GameGangChooseMod.prototype.onCancle = function () {
            this.hideCombo();
            this.gameScene.selectBtnMod.reShow();
        };
        GameGangChooseMod.prototype.showCombo = function (valueList) {
            if (!valueList || valueList.length < 2 || valueList[0].length < 3) {
                console.error("param error");
                return;
            }
            this.tValueList = valueList;
            if (this.twoCardList[0].length < 1) {
                this.initCard();
            }
            var eatLen = 4;
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
            for (var i = 0; i < valueList.length; i++) {
                for (var j = 0; j < eatLen; j++) {
                    curentCardList[i][j].setCardValueAndSHow(valueList[i][j]);
                }
            }
            this.visible = true;
        };
        /**隐藏 */
        GameGangChooseMod.prototype.hideCombo = function () {
            this.visible = false;
        };
        GameGangChooseMod.prototype.initCard = function () {
            var eatLen = 4;
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
        return GameGangChooseMod;
    }(Tpm.BaseGameMod));
    Tpm.GameGangChooseMod = GameGangChooseMod;
    __reflect(GameGangChooseMod.prototype, "Tpm.GameGangChooseMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameGangChooseMod.js.map