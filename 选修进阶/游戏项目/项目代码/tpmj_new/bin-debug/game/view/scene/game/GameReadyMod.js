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
    var GameReadyMod = (function (_super) {
        __extends(GameReadyMod, _super);
        function GameReadyMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameReadyModSkin;
            return _this;
        }
        GameReadyMod.prototype.childrenCreated = function () {
        };
        GameReadyMod.prototype.onEnable = function () {
            this.beginBtn.touchEnabled = true;
            this.beginBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBegin, this);
        };
        GameReadyMod.prototype.onRemove = function () {
            this.stopTimer();
            this.beginBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBegin, this);
        };
        /**
         * @param force 锤子需求，某些情况本家已准备，不显示准备中
         */
        GameReadyMod.prototype.setState = function (state, force) {
            if (force === void 0) { force = false; }
            this.readyState = state;
            this.stopTimer();
            switch (this.readyState) {
                case ReadyState.normal:
                    this.upReady.visible = false;
                    this.downReady.visible = false;
                    this.beginBtn.visible = false;
                    break;
                case ReadyState.ready_00:
                    this.upReady.visible = false;
                    this.downReady.visible = false;
                    this.beginBtn.visible = true;
                    this.startTimer();
                    break;
                case ReadyState.ready_10:
                    this.upReady.visible = true;
                    this.downReady.visible = false;
                    this.beginBtn.visible = true;
                    this.startTimer();
                    break;
                case ReadyState.ready_01:
                    this.upReady.visible = false;
                    this.downReady.visible = true;
                    this.beginBtn.visible = false;
                    break;
                case ReadyState.ready_11:
                    this.upReady.visible = true;
                    this.downReady.visible = true;
                    this.beginBtn.visible = false;
                    break;
                default:
                    this.upReady.visible = false;
                    this.downReady.visible = false;
                    this.beginBtn.visible = false;
                    break;
            }
            if (force) {
                this.downReady.visible = false;
            }
        };
        /**
         * 隐藏开始游戏按钮,测试
         */
        GameReadyMod.prototype.hideBeginBtn = function () {
            this.beginBtn.visible = false;
        };
        /**开始游戏 */
        GameReadyMod.prototype.onBegin = function () {
            var _this = this;
            this.beginBtn.touchEnabled = false;
            setTimeout(function () {
                _this.beginBtn.touchEnabled = true;
            }, 1000);
            this.ctrl.sendMod.sendReady();
            this.gameScene.clearDesk(false);
        };
        /**
         * 启动倒计时
         */
        GameReadyMod.prototype.startTimer = function (limitTime) {
            if (limitTime === void 0) { limitTime = 120; }
            this.remainTime = limitTime;
            this.backTimer && this.backTimer.stop() && (this.backTimer.removeEventListener(egret.TimerEvent.TIMER, this.onOutTime, this));
            this.backTimer = new Tpm.DateTimer(1000, limitTime);
            this.backTimer.addEventListener(egret.TimerEvent.TIMER, this.onOutTime, this);
            this.backTimer.reset();
            this.backTimer.start();
        };
        GameReadyMod.prototype.onOutTime = function () {
            if (this.remainTime < 1) {
                this.stopTimer();
                // 匹配界面停留过长处理
                return;
            }
            this.remainTime--;
        };
        /**
         * 停止倒计时
         */
        GameReadyMod.prototype.stopTimer = function () {
            this.backTimer && this.backTimer.stop();
        };
        return GameReadyMod;
    }(Tpm.BaseGameMod));
    Tpm.GameReadyMod = GameReadyMod;
    __reflect(GameReadyMod.prototype, "Tpm.GameReadyMod");
    var ReadyState;
    (function (ReadyState) {
        ReadyState[ReadyState["normal"] = 0] = "normal";
        ReadyState[ReadyState["ready_00"] = 1] = "ready_00";
        ReadyState[ReadyState["ready_10"] = 2] = "ready_10";
        ReadyState[ReadyState["ready_01"] = 3] = "ready_01";
        ReadyState[ReadyState["ready_11"] = 4] = "ready_11";
    })(ReadyState = Tpm.ReadyState || (Tpm.ReadyState = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameReadyMod.js.map