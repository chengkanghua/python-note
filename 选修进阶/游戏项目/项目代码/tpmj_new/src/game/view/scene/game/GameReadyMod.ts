module Tpm {
    export class GameReadyMod extends BaseGameMod {
        private upReady:eui.Image;
        private downReady:eui.Image;
        private beginBtn:eui.Button;

        private readyState: ReadyState;
        // 退出匹配倒计时
        private backTimer: DateTimer;
        // 界面存在时间
        private remainTime: number;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameReadyModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.beginBtn.touchEnabled = true;
            this.beginBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBegin, this);
        }

        protected onRemove() {
            this.stopTimer();

            this.beginBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBegin, this);
        }

        /**
         * @param force 锤子需求，某些情况本家已准备，不显示准备中
         */
        public setState(state: ReadyState, force: boolean = false) {
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
        }

        /**
         * 隐藏开始游戏按钮,测试
         */
        public hideBeginBtn() {
            this.beginBtn.visible = false;
        }

        /**开始游戏 */
        private onBegin() {
            this.beginBtn.touchEnabled = false;
            setTimeout(()=>{
                this.beginBtn.touchEnabled = true;
            }, 1000);
            this.ctrl.sendMod.sendReady();
            this.gameScene.clearDesk(false);
        }

        /**
         * 启动倒计时
         */
        private startTimer(limitTime: number = 120) {
            this.remainTime = limitTime;

            this.backTimer && this.backTimer.stop() && (this.backTimer.removeEventListener(egret.TimerEvent.TIMER, this.onOutTime, this));
            this.backTimer = new DateTimer(1000, limitTime);
            this.backTimer.addEventListener(egret.TimerEvent.TIMER, this.onOutTime, this);
            this.backTimer.reset();
            this.backTimer.start();
        }

        private onOutTime() {
            if (this.remainTime < 1) {
                this.stopTimer();
                // 匹配界面停留过长处理
                
                return;
            }
            this.remainTime --;
        }

        /**
         * 停止倒计时
         */
        private stopTimer() {
            this.backTimer && this.backTimer.stop();
        }
    }

    export enum ReadyState {
        normal,
        ready_00,
        ready_10,   //上家准备，下家未准备
        ready_01,
        ready_11
    }
}