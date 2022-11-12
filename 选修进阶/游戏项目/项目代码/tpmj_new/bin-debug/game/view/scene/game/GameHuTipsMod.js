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
    var GameHuTipsMod = (function (_super) {
        __extends(GameHuTipsMod, _super);
        function GameHuTipsMod() {
            var _this = _super.call(this) || this;
            _this.itemWidth = 129;
            _this.itemHeight = 83;
            _this.frameMaxWidth = 536;
            _this.frameMaxHeight = 320;
            _this.skinName = TpmSkin.GameHuTipsModSkin;
            return _this;
        }
        GameHuTipsMod.prototype.childrenCreated = function () {
        };
        GameHuTipsMod.prototype.onEnable = function () {
            this.cancleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onCancle, this);
        };
        GameHuTipsMod.prototype.onRemove = function () {
            this.hideTips();
        };
        /**显示胡牌提示 */
        GameHuTipsMod.prototype.showHuTips = function (cardValueList, outCardValue) {
            if (this.curValue == outCardValue || this.curList == cardValueList) {
                // console.log("不用更新UI");
                return;
            }
            this.curList = cardValueList;
            this.curValue = outCardValue;
            // console.log("showHuTips=cardValueList==", cardValueList);
            var listLen = cardValueList.length;
            if (listLen < 1) {
                console.error("valuelist error");
                return;
            }
            var realWidth = this.frameMaxWidth;
            var realHeight = this.frameMaxHeight;
            if (listLen < 7 && listLen > 3) {
                realHeight = realHeight - (this.itemHeight + 6);
            }
            else if (listLen < 4) {
                realHeight = realHeight - 2 * (this.itemHeight + 6);
            }
            if (listLen == 2) {
                realWidth = realWidth - this.itemWidth;
            }
            else if (listLen == 1) {
                realWidth = realWidth - 2 * this.itemWidth;
            }
            this.framGro.width = realWidth;
            this.framGro.height = realHeight;
            this.validateNow();
            var ac = new eui.ArrayCollection();
            ac.source = cardValueList;
            this.fanList.dataProvider = ac;
            this.fanList.itemRenderer = Tpm.HuTipsItem;
            this.framGro.visible = true;
        };
        /**显示听牌取消按钮 */
        GameHuTipsMod.prototype.showCancle = function () {
            this.visible = true;
            this.framGro.visible = false;
        };
        /**隐藏胡牌提示 */
        GameHuTipsMod.prototype.hideTips = function () {
            this.curValue = null;
            this.visible = false;
        };
        /**取消响应 */
        GameHuTipsMod.prototype.onCancle = function () {
            this.hideTips();
            this.gameScene.selectBtnMod.reShow();
            this.gameScene.cardMod.tingCancleShow();
        };
        return GameHuTipsMod;
    }(Tpm.BaseGameMod));
    Tpm.GameHuTipsMod = GameHuTipsMod;
    __reflect(GameHuTipsMod.prototype, "Tpm.GameHuTipsMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameHuTipsMod.js.map