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
    var SetPanel = (function (_super) {
        __extends(SetPanel, _super);
        function SetPanel() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.SetPanelSkin";
            return _this;
        }
        SetPanel.prototype.childrenCreated = function () {
            this.hallSetGroup.visible = false;
            this.bgMusic_hallBtn.selected = !Tpm.App.LocalStorageUtil.allowMusic;
            this.effectMusic_hallBtn.selected = !Tpm.App.LocalStorageUtil.allowEffect;
        };
        /** 添加到场景*/
        SetPanel.prototype.onEnable = function () {
            this.hallSetGroup.visible = false;
            if (this.gameBool) {
                this.hallSetGroup.visible = false;
            }
            else {
                this.hallSetGroup.visible = true;
                this.bgMusic_Btn = this.bgMusic_hallBtn;
                this.effectMusic_Btn = this.effectMusic_hallBtn;
                this.closeBtn = this.closeBtnHall;
            }
            this.bgMusic_Btn.selected = !Tpm.App.LocalStorageUtil.allowMusic;
            this.effectMusic_Btn.selected = !Tpm.App.LocalStorageUtil.allowEffect;
            this.hallSetGroup.visible = true;
            this.bgMusic_Btn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.setToggleSwitchTouch, this);
            this.effectMusic_Btn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.setToggleSwitchTouch, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onClose, this);
        };
        /** 从场景中移除*/
        SetPanel.prototype.onRemove = function () {
            this.bgMusic_Btn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.setToggleSwitchTouch, this);
            this.effectMusic_Btn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.setToggleSwitchTouch, this);
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onClose, this);
            this.gameBool = false;
        };
        SetPanel.prototype.onClose = function () {
            this.hide();
        };
        SetPanel.prototype.setToggleSwitchTouch = function (e) {
            var toogle = !e.target.selected;
            switch (e.target) {
                case this.bgMusic_Btn:
                    Tpm.App.LocalStorageUtil.allowMusic = Tpm.App.SoundManager.allowPlayBGM = toogle;
                    //游戏中开关背景音乐
                    if (Tpm.App.SoundManager.allowPlayBGM && Tpm.App.SceneManager.getCurScene() instanceof Tpm.GameScene) {
                    }
                    else {
                        Tpm.App.SoundManager.stopBGM();
                    }
                    break;
                case this.effectMusic_Btn:
                    Tpm.App.LocalStorageUtil.allowEffect = Tpm.App.SoundManager.allowPlayEffect = toogle;
                    //游戏中加载音效
                    break;
            }
        };
        return SetPanel;
    }(Tpm.BasePanel));
    Tpm.SetPanel = SetPanel;
    __reflect(SetPanel.prototype, "Tpm.SetPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=SetPanel.js.map