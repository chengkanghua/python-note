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
    var GameDiskMod = (function (_super) {
        __extends(GameDiskMod, _super);
        function GameDiskMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameDiskModSkin;
            return _this;
        }
        GameDiskMod.prototype.childrenCreated = function () {
        };
        GameDiskMod.prototype.onEnable = function () {
        };
        GameDiskMod.prototype.onRemove = function () {
            this.stopTimer();
        };
        /**
         * 设置状态、倒计时时间,并更新相关UI
         */
        GameDiskMod.prototype.setState = function (state, time, diceList) {
            if (time === void 0) { time = 15; }
            if (diceList === void 0) { diceList = []; }
            this.diskState = state;
            switch (this.diskState) {
                case DiskState.normal:
                    this.arrowDown.visible = false;
                    this.arrowUp.visible = false;
                    this.timeGro.visible = false;
                    this.diceGro.visible = false;
                    break;
                case DiskState.down:
                    this.arrowDown.visible = true;
                    this.arrowUp.visible = false;
                    this.timeGro.visible = true;
                    this.diceGro.visible = false;
                    this.startTimer(time);
                    break;
                case DiskState.up:
                    this.arrowDown.visible = false;
                    this.arrowUp.visible = true;
                    this.timeGro.visible = true;
                    this.diceGro.visible = false;
                    this.startTimer(time);
                    break;
                case DiskState.dice:
                    this.arrowDown.visible = false;
                    this.arrowUp.visible = false;
                    this.timeGro.visible = false;
                    this.diceGro.visible = false;
                    this.playAnimation(diceList);
                default:
                    this.arrowDown.visible = false;
                    this.arrowUp.visible = false;
                    this.timeGro.visible = false;
                    this.diceGro.visible = false;
                    break;
            }
        };
        /**
         * 启动倒计时
         */
        GameDiskMod.prototype.startTimer = function (limitTime) {
            if (limitTime === void 0) { limitTime = 15; }
            this.curTime = limitTime;
            this.timeLab.text = Tpm.NumberTool.formatTime(this.curTime);
            this.outTimer && this.outTimer.stop() && (this.outTimer.removeEventListener(egret.TimerEvent.TIMER, this.onOutTime, this));
            this.outTimer = new Tpm.DateTimer(1000, this.curTime);
            this.outTimer.addEventListener(egret.TimerEvent.TIMER, this.onOutTime, this);
            this.outTimer.reset();
            this.outTimer.start();
        };
        GameDiskMod.prototype.onOutTime = function () {
            if (Number(this.curTime) < 1) {
                this.timeLab.text = "00";
                this.stopTimer();
                return;
            }
            this.curTime--;
            this.timeLab.text = Tpm.NumberTool.formatTime(this.curTime);
        };
        /**
         * 停止倒计时
         */
        GameDiskMod.prototype.stopTimer = function () {
            this.outTimer && this.outTimer.stop();
        };
        /**初始化序列帧 */
        GameDiskMod.prototype.initMovieClip = function () {
            this.mc && this.mc.parent && this.mc.parent.removeChild(this.mc);
            var resName = "tpm_shaizi";
            var data = RES.getRes(resName + "_mc_json");
            var img = RES.getRes(resName + "_tex_png");
            var mcFactory = new egret.MovieClipDataFactory(data, img);
            this.mc = new egret.MovieClip(mcFactory.generateMovieClipData("shaizi"));
            this.mc.x = 75 + 24;
            this.mc.y = 49 + 45;
            this.addChild(this.mc);
        };
        /**播放色子序列帧 */
        GameDiskMod.prototype.playAnimation = function (list) {
            var _this = this;
            if (list.length < 2) {
                console.error("dice number error");
                return;
            }
            var times = 4;
            this.initMovieClip();
            this.mc.gotoAndPlay(0, times);
            this.diceGro.visible = false;
            setTimeout(function () {
                _this.mc.stop();
                _this.mc.parent && _this.mc.parent.removeChild(_this.mc);
                _this.diceGro.alpha = 1;
                _this.diceGro.scaleX = 0.6;
                _this.diceGro.scaleY = 0.6;
                _this.diceGro.visible = true;
                (_this.diceGro.getChildAt(0)).texture = RES.getRes("tpm_s" + list[0] + "_png");
                (_this.diceGro.getChildAt(1)).texture = RES.getRes("tpm_s" + list[1] + "_png");
                _this.diceGro.visible = true;
                egret.Tween.get(_this.diceGro)
                    .wait(300)
                    .to({ scaleX: 1, scaleY: 1 }, 200)
                    .wait(700)
                    .to({ alpha: 0 }, 200)
                    .set({ visible: false })
                    .call(function () {
                    // 显示定庄结果
                    _this.gameScene.headDown.reZhuangFlag(Tpm.UserPosition.Down);
                    _this.gameScene.headUp.reZhuangFlag(Tpm.UserPosition.Up);
                }, _this);
                // 与色子播放完后回调同步
                setTimeout(function () {
                    // 发牌
                    Tpm.App.DataCenter.MsgCache.exeMsg(Tpm.ProtocolHeadRev.R_101005);
                }, 300 + 200 + 700 + 200);
            }, times * 330);
        };
        return GameDiskMod;
    }(Tpm.BaseGameMod));
    Tpm.GameDiskMod = GameDiskMod;
    __reflect(GameDiskMod.prototype, "Tpm.GameDiskMod");
    /**
     * 风盘状态
     */
    var DiskState;
    (function (DiskState) {
        DiskState[DiskState["normal"] = 0] = "normal";
        DiskState[DiskState["down"] = 1] = "down";
        DiskState[DiskState["up"] = 2] = "up";
        DiskState[DiskState["dice"] = 3] = "dice";
    })(DiskState = Tpm.DiskState || (Tpm.DiskState = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameDiskMod.js.map