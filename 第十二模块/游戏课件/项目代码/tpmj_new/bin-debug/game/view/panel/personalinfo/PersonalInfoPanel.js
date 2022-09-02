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
    var PersonalInfoPanel = (function (_super) {
        __extends(PersonalInfoPanel, _super);
        function PersonalInfoPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.PersonalInfoPanelSkin;
            return _this;
        }
        /**添加到场景中*/
        PersonalInfoPanel.prototype.onEnable = function () {
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        PersonalInfoPanel.prototype.recDataFun = function (data) {
            var personalinfodata = Tpm.ProtocolHttpData.PersonalInfoData.data;
            personalinfodata = data;
            this.headImg.source = personalinfodata.avater_url;
            this.nick.text = Tpm.StringTool.formatNickName(personalinfodata.nick_name, 12);
            this.id.text = personalinfodata.uid + "";
            this.golds.text = Tpm.NumberTool.sperateMoney(personalinfodata.money);
            this.diamonds.text = personalinfodata.diamond + ""; //NumberTool.sperateMoney(personalinfodata.diamond);
            this.totalCount.text = personalinfodata.total + "";
            this.highestWinCount.text = personalinfodata.highest_winning_streak + "场";
            this.winRate.text = personalinfodata.winning_rate;
        };
        /**从场景中移除*/
        PersonalInfoPanel.prototype.onRemove = function () {
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        return PersonalInfoPanel;
    }(Tpm.BasePanel));
    Tpm.PersonalInfoPanel = PersonalInfoPanel;
    __reflect(PersonalInfoPanel.prototype, "Tpm.PersonalInfoPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PersonalInfoPanel.js.map