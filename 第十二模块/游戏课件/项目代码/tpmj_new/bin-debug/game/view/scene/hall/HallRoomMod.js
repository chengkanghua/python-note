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
    var HallRoomMod = (function (_super) {
        __extends(HallRoomMod, _super);
        function HallRoomMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.HallRoomModSkin;
            return _this;
        }
        HallRoomMod.prototype.childrenCreated = function () {
            this.initList();
        };
        HallRoomMod.prototype.onEnable = function () {
            this.lowBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            this.middleBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            this.highBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        HallRoomMod.prototype.onRemove = function () {
            this.lowBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            this.middleBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            this.highBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        HallRoomMod.prototype.initList = function () {
            this.betLabList = [];
            this.minGoldLabList = [];
            this.playerLabList = [];
            this.betLabList.push(this.lowBtn.getChildByName("lowGro").getChildByName("baseLab"));
            this.betLabList.push(this.middleBtn.getChildByName("middleGro").getChildByName("baseLabM"));
            this.betLabList.push(this.highBtn.getChildByName("highGro").getChildByName("baseLabH"));
            this.minGoldLabList.push(this.lowBtn.getChildByName("lowGro").getChildByName("mininumLab"));
            this.minGoldLabList.push(this.middleBtn.getChildByName("middleGro").getChildByName("mininumLabM"));
            this.minGoldLabList.push(this.highBtn.getChildByName("highGro").getChildByName("mininumLabH"));
            this.playerLabList.push(this.lowBtn.getChildByName("lowGro").getChildByName("playLab"));
            this.playerLabList.push(this.middleBtn.getChildByName("middleGro").getChildByName("playLabM"));
            this.playerLabList.push(this.highBtn.getChildByName("highGro").getChildByName("playLabH"));
        };
        HallRoomMod.prototype.initRoomUI = function (data) {
            for (var i = 0; i < data.length; i++) {
                this.betLabList[i].text = data[i].baseBet + "";
                this.minGoldLabList[i].text = Tpm.NumberTool.formatMoney(data[i].minEnterGold, 2) + "金币以上";
                this.playerLabList[i].text = data[i].curPlayerCount + "人在玩";
            }
        };
        HallRoomMod.prototype.reRoomNum = function (data) {
            for (var i = 0; i < data.length; i++) {
                this.playerLabList[i].text = data[i].curPlayerCount + "人在玩";
            }
        };
        /**
         * 点击房间处理
         */
        HallRoomMod.prototype.onTouch = function (evt) {
            var target = evt.target;
            var roomType;
            switch (target) {
                case this.lowBtn:
                    roomType = Tpm.RoomType.noob;
                    break;
                case this.middleBtn:
                    roomType = Tpm.RoomType.middle;
                    break;
                case this.highBtn:
                    roomType = Tpm.RoomType.high;
                    break;
                default:
                    roomType = Tpm.RoomType.noob;
                    break;
            }
            Tpm.App.getController(Tpm.HallController.NAME).sendChooseRoom(roomType);
        };
        return HallRoomMod;
    }(Tpm.BaseUI));
    Tpm.HallRoomMod = HallRoomMod;
    __reflect(HallRoomMod.prototype, "Tpm.HallRoomMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallRoomMod.js.map