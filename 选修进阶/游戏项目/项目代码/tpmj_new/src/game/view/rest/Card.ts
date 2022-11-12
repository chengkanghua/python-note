module Tpm {
    /**
     * 麻将牌
     */
    export class Card extends egret.DisplayObjectContainer {
        public static NAME: string = "Card";
        private _cardValue: number;
        private cardBg: eui.Image;
        private cardImg: eui.Image;
        private _arrowState: boolean;
        private cardArrow: eui.Image;
        private cardMask: eui.Rect;
        private cardBack: eui.Image;
        private _userPos: UserPosition;

        private _bUp: boolean;
        private upDist: number = 20;
        private initPosY: number = 0;

        public constructor() {
            super();
            this.cardBg = new eui.Image();
            this.cardImg = new eui.Image();
            this.addChild(this.cardBg);
            this.addChild(this.cardImg);

            this.touchChildren = false;
            this.touchEnabled = false;

            this._bUp = false;
        }

        /**
         * 获取牌值
         */
        public get cardValue() {
            return this._cardValue;
        }

        /**
         * 牌所属玩家的位置
         */
        public get userPos() {
            return this._userPos;
        }

        /**
         * 是否抬起
         */
        public get bUp() {
            return this._bUp;
        }

        /**
         * 获取手牌初始Y坐标
         */
        public get initY() {
            return this.initPosY;
        }

        /**
         * 是否显示箭头
         */
        public get arrowState():boolean {
            return this._arrowState;
        }

        /**
         * 设置箭头状态
         */
        public setArrow(show: boolean = false) {
            if (this._userPos != UserPosition.Down) {
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
        }

        /**
         * 设置置灰状态
         */
        public setGray(gray: boolean = false) {
            if (this._userPos != UserPosition.Down) {
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
        }

        /**
         * 设置下家手牌是否显示背面状态
         */
        public setBack(back: boolean = false) {
            if (this._userPos != UserPosition.Down) {
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
        }

        /**设置牌值和牌值显示
         * 此方法不推荐在牌桌内使用
         */
        public setCardValueAndSHow(cardValue) {
            this._cardValue = cardValue;
            this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
        }

        public setCardValueAndShowOut(cardValue) {
            this._cardValue = cardValue;
            this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
        }

        /**
         * 设置手牌皮肤
         */
        public setHandSkin(cardValue: number, userPos: UserPosition, tingState: boolean = false) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == UserPosition.Down) {
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
            } else if (userPos == UserPosition.Up) {
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
        }

        /**
         * 设置出牌皮肤
         */
        public setOutSkin(cardValue: number, userPos: UserPosition) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_7_png");
                this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
                this.cardImg.x = 12;
                this.cardImg.y = 8;
            } else if (userPos == UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_7_png");
                this.cardImg.source = RES.getRes("tpm_card_small_" + cardValue + "_png");
                this.cardImg.x = 11;
                this.cardImg.y = 8;
                this.cardBg.scaleX = 0.94;
                this.cardBg.scaleY = 0.94;
            }
        }

        /**
         * 设置吃碰牌皮肤
         */
        public setEatSkin(cardValue: number, userPos: UserPosition) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_4_png");
                this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                this.cardBg.scaleX = 1.1;
                this.cardImg.x = 7;
                this.cardImg.y = -10;
                this.cardImg.scaleX = 0.8;
                this.cardImg.scaleY = 0.8;
            } else if (userPos == UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_8_png");
                this.cardImg.source = RES.getRes("tpm_card_big_" + cardValue + "_png");
                this.cardBg.scaleX = 0.98;
                this.cardBg.scaleY = 0.98;
                this.cardImg.x = 3;
                this.cardImg.y = -14;
                this.cardImg.scaleX = 0.79;
                this.cardImg.scaleY = 0.79;
            }
        }

        /**
         * 设置暗杠皮肤
         */
        public setAnGangSkin(cardValue: number, userPos: UserPosition) {
            this._cardValue = cardValue;
            this._userPos = userPos;
            if (userPos == UserPosition.Down) {
                this.cardBg.source = RES.getRes("tpm_cardbg_6_png");
                this.cardImg.source = null;
                this.cardBg.scaleX = 1.08;
            } else if (userPos == UserPosition.Up) {
                this.cardBg.source = RES.getRes("tpm_cardbg_6_png");
                this.cardImg.source = null;
                this.cardBg.scaleX = 0.9;
                this.cardBg.scaleY = 0.9;
            }
        }

        /**弹起*/
        public toUp() {
            if (this.bUp == false) {
                this.y = this.initPosY - this.upDist;
                this._bUp = true;
            }
        }

        /**放下*/
        public toDown() {
            if (this.bUp == true) {
                this.y = this.initPosY;
                this._bUp = false;
            }
        }

        //回收到对象池
        public recycle() {
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

            ObjectPool.getPool(Card.NAME).returnObject(this);
        }
    }
}