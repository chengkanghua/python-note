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
    var EmailDetailPanel = (function (_super) {
        __extends(EmailDetailPanel, _super);
        function EmailDetailPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.EmailDetailPanelSkin";
            return _this;
        }
        /**添加到场景中*/
        EmailDetailPanel.prototype.onEnable = function () {
            this.NcloseBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.HcloseBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.getGiftBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.sureBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        EmailDetailPanel.prototype.recDataFun = function (data) {
            var emailDeatilData = Tpm.ProtocolHttpData.emailDeatilData.data;
            emailDeatilData = data;
            var len = emailDeatilData.reward.length;
            if (len == 0) {
                this.hasGiftGroup.visible = false;
                this.noGiftGroup.visible = true;
                this.NemailDetailtitle.text = emailDeatilData.title;
                this.NemailDetailcontent.text = emailDeatilData.content;
            }
            else {
                this.hasGiftGroup.visible = true;
                this.noGiftGroup.visible = false;
                var rewardItem = Tpm.ProtocolHttpData.RewardItem;
                rewardItem = emailDeatilData.reward[0];
                // this.gitIcon.source=rewardItem.reward_icon+"";
                this.giftNum.text = "×" + rewardItem.reward_quantity;
                this.HemailDetailtitle.text = emailDeatilData.title;
                this.HemailDetailcontent.text = emailDeatilData.content;
            }
        };
        EmailDetailPanel.prototype.getReward = function () {
        };
        /**从场景中移除*/
        EmailDetailPanel.prototype.onRemove = function () {
            this.HcloseBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.NcloseBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
            this.getGiftBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.getReward, this);
            this.sureBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        return EmailDetailPanel;
    }(Tpm.BasePanel));
    Tpm.EmailDetailPanel = EmailDetailPanel;
    __reflect(EmailDetailPanel.prototype, "Tpm.EmailDetailPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=EmailDetailPanel.js.map