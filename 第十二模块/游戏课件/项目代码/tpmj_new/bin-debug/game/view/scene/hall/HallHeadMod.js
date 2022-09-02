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
    var HallHeadMod = (function (_super) {
        __extends(HallHeadMod, _super);
        function HallHeadMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.HallHeadModSkin;
            return _this;
        }
        HallHeadMod.prototype.childrenCreated = function () {
            this.headImg.mask = this.headMask;
        };
        HallHeadMod.prototype.onEnable = function () {
            // 初始化钻石UI显示状态
            this.setDiamondVisible();
            this.headGro.addEventListener(egret.TouchEvent.TOUCH_TAP, this.showPersonalInfo, this);
            this.arrowGro.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onArrow, this);
            this.addBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
        };
        HallHeadMod.prototype.onRemove = function () {
            this.headGro.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.showPersonalInfo, this);
            this.arrowGro.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onArrow, this);
            this.addBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
        };
        /**
         * 设置钻石UI显示状态
         */
        HallHeadMod.prototype.setDiamondVisible = function (visible) {
            if (visible === void 0) { visible = false; }
            if (visible) {
                this.arrowGro.visible = false;
                this.diamondGro.visible = true;
            }
            else {
                this.arrowGro.visible = true;
                this.diamondGro.visible = false;
            }
        };
        Object.defineProperty(HallHeadMod.prototype, "arrowGroup", {
            /**
             * 获取Arrow区域
             */
            get: function () {
                return this.arrowGro;
            },
            enumerable: true,
            configurable: true
        });
        /**
         * 点击向上箭头区域
         */
        HallHeadMod.prototype.onArrow = function () {
            var _this = this;
            this.setDiamondVisible(true);
            this.timeOut = setTimeout(function () {
                _this.setDiamondVisible(false);
                clearTimeout(_this.timeOut);
            }, 3000, this);
            Tpm.HallHttpDataSend.sendGetDiamondAndGold();
        };
        /**
         * 显示个人信息
         */
        HallHeadMod.prototype.showPersonalInfo = function () {
            Tpm.HallHttpDataSend.sendGetUserInfo();
        };
        /**
         * 点击+
         */
        HallHeadMod.prototype.onAdd = function () {
            Tpm.HallHttpDataSend.sendGetGoodsList();
            // App.PanelManager.open(PanelConst.ShopMallPanel);
        };
        /**
        * 更新钻石金币
        */
        HallHeadMod.prototype.updateDiamondAndGold = function (diamond, gold) {
            this.diamondLab.text = diamond + ""; //NumberTool.sperateMoney(diamond);
            this.goldLab.text = Tpm.NumberTool.formatMoney(gold);
        };
        /**
         * 更新个人信息
         */
        HallHeadMod.prototype.updatePersonalInfo = function () {
            this.nameLab.text = Tpm.StringTool.formatNickName(Tpm.App.DataCenter.UserInfo.myUserInfo.nickName, 12); //StringTool.formatNickName("tese1tese11411",12);
            this.idLab.text = "ID:" + Tpm.App.DataCenter.UserInfo.myUserInfo.userID + "";
            this.diamondLab.text = Tpm.App.DataCenter.UserInfo.myUserInfo.diamond + "";
            this.goldLab.text = Tpm.NumberTool.formatMoney(Tpm.App.DataCenter.UserInfo.myUserInfo.gold);
            this.headImg.source = Tpm.App.DataCenter.UserInfo.myUserInfo.headUrl;
        };
        return HallHeadMod;
    }(Tpm.BaseUI));
    Tpm.HallHeadMod = HallHeadMod;
    __reflect(HallHeadMod.prototype, "Tpm.HallHeadMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallHeadMod.js.map