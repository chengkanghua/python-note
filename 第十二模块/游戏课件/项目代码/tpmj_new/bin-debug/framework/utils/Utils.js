var Tpm;
(function (Tpm) {
    /**
     * 其他的通用方法
     */
    var Utils;
    (function (Utils) {
        /**
         * 自定义延时函数
         * @param precision 计时精度
         */
        function setTimeOut(callBack, delay, thisObj, precision) {
            if (thisObj === void 0) { thisObj = null; }
            if (precision === void 0) { precision = 100; }
            var times = Math.round(delay / precision);
            if (times <= 0) {
                callBack && callBack.call(thisObj);
                return;
            }
            var tTimer = new Tpm.DateTimer(precision, times);
            var tTimes = 0;
            tTimer.addEventListener(egret.TimerEvent.TIMER, function () {
                tTimes++;
                if (tTimes == times) {
                    tTimer.stop();
                    callBack && callBack.call(thisObj);
                }
            }, this);
            tTimer.start();
        }
        Utils.setTimeOut = setTimeOut;
    })(Utils = Tpm.Utils || (Tpm.Utils = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=Utils.js.map