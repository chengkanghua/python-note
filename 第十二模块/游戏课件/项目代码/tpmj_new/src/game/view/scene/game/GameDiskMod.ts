module Tpm {
    export class GameDiskMod extends BaseGameMod {
        private arrowDown:eui.Image;
        private arrowUp:eui.Image;
        public timeGro:eui.Group;
        public timeLab:eui.BitmapLabel;
        private curTime: number;
        public diceGro:eui.Group;

        private diskState: DiskState;
        private outTimer: DateTimer;
        private mc:egret.MovieClip;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameDiskModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
        }

        protected onRemove() {
            this.stopTimer();
        }

        /**
         * 设置状态、倒计时时间,并更新相关UI
         */
        public setState(state: DiskState, time: number = 15, diceList: Array<number> = []) {
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
        }

        /**
         * 启动倒计时
         */
        private startTimer(limitTime: number = 15) {
            this.curTime = limitTime;
            this.timeLab.text = NumberTool.formatTime(this.curTime);

            this.outTimer && this.outTimer.stop() && (this.outTimer.removeEventListener(egret.TimerEvent.TIMER, this.onOutTime, this));
            this.outTimer = new DateTimer(1000, this.curTime);
            this.outTimer.addEventListener(egret.TimerEvent.TIMER, this.onOutTime, this);
            this.outTimer.reset();
            this.outTimer.start();
        }

        private onOutTime() {
            if (Number(this.curTime) < 1) {
                this.timeLab.text = "00";
                this.stopTimer();
                return;
            }
            this.curTime--;
            this.timeLab.text = NumberTool.formatTime(this.curTime);
        }

        /**
         * 停止倒计时
         */
        private stopTimer() {
            this.outTimer && this.outTimer.stop();
        }

        /**初始化序列帧 */
        private initMovieClip() {
            this.mc && this.mc.parent && this.mc.parent.removeChild(this.mc);
            var resName = "tpm_shaizi"
            var data = RES.getRes(resName+"_mc_json");
            var img = RES.getRes(resName+"_tex_png");
            var mcFactory:egret.MovieClipDataFactory = new egret.MovieClipDataFactory(data, img);
            this.mc = new egret.MovieClip( mcFactory.generateMovieClipData("shaizi") );
            this.mc.x = 75+24;
            this.mc.y = 49+45;
            this.addChild(this.mc);
        }

        /**播放色子序列帧 */
        public playAnimation(list: Array<number>) {
            if (list.length < 2) {
                console.error("dice number error");
                return;
            }
            var times = 4;
            this.initMovieClip();
            this.mc.gotoAndPlay(0, times);
            this.diceGro.visible = false;

            setTimeout(()=>{
                this.mc.stop();
                this.mc.parent && this.mc.parent.removeChild(this.mc);
                this.diceGro.alpha = 1;
                this.diceGro.scaleX = 0.6;
                this.diceGro.scaleY = 0.6;
                this.diceGro.visible = true;
                ( <eui.Image>(this.diceGro.getChildAt(0)) ).texture = RES.getRes("tpm_s"+list[0]+"_png");
                ( <eui.Image>(this.diceGro.getChildAt(1)) ).texture = RES.getRes("tpm_s"+list[1]+"_png");
                this.diceGro.visible = true;
                egret.Tween.get(this.diceGro)
                .wait(300)
                .to({scaleX:1, scaleY:1}, 200)
                .wait(700)
                .to({alpha:0}, 200)
                .set({visible: false})
                .call( ()=>{
                    // 显示定庄结果
                    this.gameScene.headDown.reZhuangFlag(UserPosition.Down);
                    this.gameScene.headUp.reZhuangFlag(UserPosition.Up);
                },this);

                // 与色子播放完后回调同步
                setTimeout(()=>{
                    // 发牌
                    App.DataCenter.MsgCache.exeMsg(ProtocolHeadRev.R_101005);
                }, 300+200+700+200);
            }, times*330);
        }
    }

    /**
     * 风盘状态
     */
    export enum DiskState {
        normal,
        down,
        up,
        dice
    }
}