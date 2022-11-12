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
    var SharePanel = (function (_super) {
        __extends(SharePanel, _super);
        function SharePanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.SharePanelSkin";
            return _this;
        }
        /** 添加到场景*/
        SharePanel.prototype.onEnable = function () {
            this.wxShareBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.wxShareFriendBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.qqShareBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**从场景中移除*/
        SharePanel.prototype.onRemove = function () {
            this.wxShareBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.wxShareFriendBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.qqShareBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.setShareType, this);
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        SharePanel.prototype.setShareType = function (e) {
            var shareType = 0;
            switch (e.target) {
                case this.wxShareBtn:
                    shareType = 0;
                    break;
                case this.wxShareFriendBtn:
                    shareType = 1;
                    break;
                case this.qqShareBtn:
                    shareType = 2;
                    break;
            }
            this.onShare(shareType);
        };
        SharePanel.prototype.onShare = function (shareType) {
            var data;
            switch (shareType) {
                case 0:
                    data = Tpm.ShareData.wxShareData;
                    data.type = 0;
                    break;
                case 1:
                    data = Tpm.ShareData.wxShareData;
                    data.type = 1;
                    break;
                case 2:
                    data = Tpm.ShareData.qqShareData;
                    break;
            }
            Tpm.App.PlatformBridge.sendPlatformEvent(Tpm.PlatFormEventConst.shareStart, data);
            Tpm.Tips.showTop("分享请求已发送！");
        };
        return SharePanel;
    }(Tpm.BasePanel));
    Tpm.SharePanel = SharePanel;
    __reflect(SharePanel.prototype, "Tpm.SharePanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=SharePanel.js.map