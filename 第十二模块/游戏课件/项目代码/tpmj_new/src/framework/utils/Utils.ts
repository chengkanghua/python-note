module Tpm {
    /**
     * 其他的通用方法
     */
    export module Utils {
        /**
         * 自定义延时函数
         * @param precision 计时精度
         */
        export function setTimeOut(callBack: Function, delay: number, thisObj: any = null, precision: number = 100) {
            var times = Math.round(delay/precision);
            if (times <= 0) {
                callBack && callBack.call(thisObj);
                return;
            }
            var tTimer: DateTimer = new DateTimer(precision, times);
            var tTimes = 0;
            tTimer.addEventListener(egret.TimerEvent.TIMER, ()=>{
                tTimes ++;
                if (tTimes == times) {
                    tTimer.stop();
                    callBack && callBack.call(thisObj);
                }
            }, this);
            tTimer.start();
        }
    }
}