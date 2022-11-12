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
    var GameTingMod = (function (_super) {
        __extends(GameTingMod, _super);
        function GameTingMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameTingModSkin;
            return _this;
        }
        GameTingMod.prototype.childrenCreated = function () {
        };
        GameTingMod.prototype.onEnable = function () {
            this.setState(TingState.normal);
        };
        GameTingMod.prototype.onRemove = function () {
        };
        /**
         * 设置状态、过胡次数,并改变UI
         */
        GameTingMod.prototype.setState = function (state, num, addFlag) {
            if (num === void 0) { num = 1; }
            if (addFlag === void 0) { addFlag = false; }
            this.tingState = state;
            switch (this.tingState) {
                case TingState.normal:
                    this.tingImg.visible = false;
                    this.guoGro.visible = false;
                    this.timesLab.text = "0";
                    break;
                case TingState.guo:
                    this.tingImg.visible = false;
                    this.guoGro.visible = true;
                    if (addFlag) {
                        this.timesLab.text = Number(this.timesLab.text) + num + "";
                    }
                    else {
                        this.timesLab.text = num.toString();
                    }
                    break;
                case TingState.ting:
                    this.tingImg.visible = true;
                    this.guoGro.visible = false;
                    break;
                default:
                    this.tingImg.visible = false;
                    this.guoGro.visible = false;
                    break;
            }
        };
        return GameTingMod;
    }(Tpm.BaseUI));
    Tpm.GameTingMod = GameTingMod;
    __reflect(GameTingMod.prototype, "Tpm.GameTingMod");
    /**
     * 听牌，过胡状态
     */
    var TingState;
    (function (TingState) {
        TingState[TingState["normal"] = 0] = "normal";
        TingState[TingState["ting"] = 1] = "ting";
        TingState[TingState["guo"] = 2] = "guo";
    })(TingState = Tpm.TingState || (Tpm.TingState = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameTingMod.js.map