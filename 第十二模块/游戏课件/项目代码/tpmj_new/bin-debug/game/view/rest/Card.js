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
     * 麻将牌
     */
    var Card = (function (_super) {
        __extends(Card, _super);
        function Card() {
            var _this = _super.call(this) || this;
            _this.upDist = 20;
            _this.initPosY = 0;
            _this.cardBg = new eui.Image();
            _this.cardImg = new eui.Image();
            _this.addChild(_this.cardBg);
            _this.addChild(_this.cardImg);
            _this.touchChildren = false;
            _this.touchEnabled = false;
            _this._bUp = false;
            return _this;
        }
        Object.defineProperty(Card.prototype, "cardValue", {
            /**
             * 获取牌值
             */
            get: function () {
                return this._cardValue;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(Card.prototype, "userPos", {
            /**
             * 牌所属玩家的位置
             */
            get: function () {
                return this._userPos;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(Card.prototype, "bUp", {
            /**
             * 是否抬起
             */
            get: function () {
                return this._bUp;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(Card.prototype, "initY", {
            /**
             * 获取手牌初始Y坐标
             */
            get: function () {
                return this.initPosY;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(Card.prototype, "arrowState", {
            /**
             * 是否显示箭头
             */
            get: function () {
                return this._arrowState;
            },
            enumerable: true,
            configurable: true
        });
        /**
         * 设置箭头状态
         */
        Card.prototype.setArrow = function (show) {
            if (show === void 0) { show = false; }
            if (this._userPos != Tpm.UserPosition.Down) {
                console.error("not yourself card");
                return;
            }
            this._arrowState = show;
            this.cardArrow && this.cardArrow.parent && this.cardArrow.parent.removeChild(this.cardArrow);
            if (show) {
                this.cardArrow = new eui.Image();
                this.cardArrow.source = RES.getRes("tpm_card_arrow_png");
                this.cardArrow.x = 24;
                this.cardArrow.y = -41;
                this.addChild(this.cardArrow);
            }
        };
        /**
         * 设置置灰状态
         */
        Card.prototype.setGray = function (gray) {
            if (gray === void 0) { gray = false; }
            if (this._userPos != Tpm.UserPosition.Down) {
                console.error("not yourself card");
                return;
            }
            if (gray) {
                this.cardMask.visible = true;
                this.touchEnabled = false;
            }
            else {
                this.cardMask.visible = false;
                this.touchEnabled = true;
            }
        };
        /**
         * 设置下家手牌是否显示背面状态
         */
        Card.prototype.setBack = function (back) {
            if (back === void 0) { back = false; }
            if (this._userPos != Tpm.UserPosition.Down) {
                console.error("not yourself card");
                return;
            }
            if (back) {
                this.cardBack.visible = true;
                this.touchEnabled = false;
            }
            else {
                this.cardBack.visible = false;
                this.touchEnabled = true;
            }
        };
        /**设置牌值和牌值显示
         * 此方法不推荐在牌桌内使用
         */
        Card.prototype.setCardValueAndSHow = function (cardValue) {
            this._cardValue = cardValue;
            this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
        };
        Card.prototype.setCardValueAndShowOut = function (cardValue) {
            this._cardValue = cardValue;
            this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
        };
        /**
         * 设置手牌皮肤
         */
        Card.prototype.setHandSkin = function (cardValue, userPos, tingState) {
            if (tingState === void 0) { tingState = false; }
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == Tpm.UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_5_png");
                this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                this.cardImg.x = 5;
                this.initPosY = 624;
                this.cardBack = new eui.Image();
                this.cardBack.source = RES.getRes("tpm_cardbg_6_png");
                this.cardBack.width = 86;
                this.cardBack.height = 120;
                this.addChild(this.cardBack);
                this.cardBack.visible = false;
                this.cardMask = new eui.Rect();
                this.cardMask.width = 83;
                this.cardMask.height = 118;
                this.cardMask.alpha = 0.5;
                this.cardMask.x = 1;
                this.addChild(this.cardMask);
                this.cardMask.visible = false;
            }
            else if (userPos == Tpm.UserPosition.Up) {
                if (!tingState) {
                    this.cardBg.source = RES.getRes("tpm_cardbg_1_png");
                    this.cardImg.source = null;
                }
                else {
                    this.cardBg.source = RES.getRes("tpm_cardbg_5_png");
                    this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                    this.cardImg.x = 3;
                    this.cardImg.y = 2;
                    this.cardBg.scaleX = 0.8;
                    this.cardBg.scaleY = 0.75;
                    this.cardImg.scaleX = 0.8;
                    this.cardImg.scaleY = 0.75;
                }
                this.initPosY = 19;
            }
        };
        /**
         * 设置出牌皮肤
         */
        Card.prototype.setOutSkin = function (cardValue, userPos) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == Tpm.UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_7_png");
                this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
                this.cardImg.x = 12;
                this.cardImg.y = 8;
            }
            else if (userPos == Tpm.UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_7_png");
                this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
                this.cardImg.x = 11;
                this.cardImg.y = 8;
                this.cardBg.scaleX = 0.94;
                this.cardBg.scaleY = 0.94;
            }
        };
        /**
         * 设置吃碰牌皮肤
         */
        Card.prototype.setEatSkin = function (cardValue, userPos) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == Tpm.UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_4_png");
                this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                this.cardBg.scaleX = 1.1;
                this.cardImg.x = 7;
                this.cardImg.y = -10;
                this.cardImg.scaleX = 0.8;
                this.cardImg.scaleY = 0.8;
            }
            else if (userPos == Tpm.UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_8_png");
                this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                this.cardBg.scaleX = 0.98;
                this.cardBg.scaleY = 0.98;
                this.cardImg.x = 3;
                this.cardImg.y = -14;
                this.cardImg.scaleX = 0.79;
                this.cardImg.scaleY = 0.79;
            }
        };
        /**
         * 设置暗杠皮肤
         */
        Card.prototype.setAnGangSkin = function (cardValue, userPos) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == Tpm.UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_6_png");
                this.cardImg.source = null;
                this.cardBg.scaleX = 1.08;
            }
            else if (userPos == Tpm.UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_6_png");
                this.cardImg.source = null;
                this.cardBg.scaleX = 0.9;
                this.cardBg.scaleY = 0.9;
            }
        };
        /**弹起*/
        Card.prototype.toUp = function () {
            if (this.bUp == false) {
                this.y = this.initPosY - this.upDist;
                this._bUp = true;
            }
        };
        /**放下*/
        Card.prototype.toDown = function () {
            if (this.bUp == true) {
                this.y = this.initPosY;
                this._bUp = false;
            }
        };
        //回收到对象池
        Card.prototype.recycle = function () {
            this._bUp = false;
            this._userPos = 0;
            this._cardValue = 0;
            this.touchEnabled = false;
            this.touchChildren = false;
            this.cardBg.source = null;
            this.cardImg.source = null;
            this.x = 0;
            this.y = 0;
            this.cardBg.x = 0;
            this.cardBg.y = 0;
            this.cardImg.x = 0;
            this.cardImg.y = 0;
            this.scaleX = 1;
            this.scaleY = 1;
            this.cardImg.scaleX = 1;
            this.cardImg.scaleY = 1;
            this.cardBg.scaleX = 1;
            this.cardBg.scaleY = 1;
            this.parent && this.parent.removeChild(this);
            this.alpha = 1;
            this.cardArrow && this.cardArrow.parent && this.cardArrow.parent.removeChild(this.cardArrow);
            this.cardMask && this.cardMask.parent && this.cardMask.parent.removeChild(this.cardMask);
            this.cardBack && this.cardBack.parent && this.cardBack.parent.removeChild(this.cardBack);
            Tpm.ObjectPool.getPool(Card.NAME).returnObject(this);
        };
        return Card;
    }(egret.DisplayObjectContainer));
    Card.NAME = "Card";
    Tpm.Card = Card;
    __reflect(Card.prototype, "Tpm.Card");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=Card.js.map