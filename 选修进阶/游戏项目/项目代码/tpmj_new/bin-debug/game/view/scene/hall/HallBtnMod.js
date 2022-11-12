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
    var HallBtnMsg;
    (function (HallBtnMsg) {
        HallBtnMsg[HallBtnMsg["playMethod"] = 0] = "playMethod";
        HallBtnMsg[HallBtnMsg["email"] = 1] = "email";
        HallBtnMsg[HallBtnMsg["share"] = 2] = "share";
        HallBtnMsg[HallBtnMsg["shop"] = 3] = "shop";
        HallBtnMsg[HallBtnMsg["set"] = 4] = "set";
    })(HallBtnMsg = Tpm.HallBtnMsg || (Tpm.HallBtnMsg = {}));
    var HallBtnMod = (function (_super) {
        __extends(HallBtnMod, _super);
        function HallBtnMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.HallBtnModSkin;
            return _this;
        }
        HallBtnMod.prototype.childrenCreated = function () {
        };
        HallBtnMod.prototype.onEnable = function () {
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        HallBtnMod.prototype.onRemove = function () {
        };
        HallBtnMod.prototype.onTouch = function (e) {
            if (!this.listener) {
                console.error("按钮未设置监听");
                return;
            }
            var target = e.target;
            var message;
            switch (target) {
                case this.hall_playMethod:
                    message = HallBtnMsg.playMethod;
                    break;
                case this.hall_email:
                    message = HallBtnMsg.email;
                    break;
                case this.hall_share:
                    message = HallBtnMsg.share;
                    break;
                case this.hall_shop:
                    message = HallBtnMsg.shop;
                    break;
                case this.hall_set:
                    message = HallBtnMsg.set;
                    break;
                default:
                    break;
            }
            if (message || message == 0) {
                this.listener(message);
            }
        };
        return HallBtnMod;
    }(Tpm.BaseUI));
    Tpm.HallBtnMod = HallBtnMod;
    __reflect(HallBtnMod.prototype, "Tpm.HallBtnMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallBtnMod.js.map