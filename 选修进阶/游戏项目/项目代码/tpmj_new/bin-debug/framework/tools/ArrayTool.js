var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var ArrayTool = (function () {
        function ArrayTool() {
        }
        /**
         * 交换数组指定索引处的元素
         * @srcArr 源数组
         * @indexA 元素A索引
         * @indexB 元素B索引
         */
        ArrayTool.swap = function (srcArr, indexA, indexB) {
            var temp = srcArr[indexA];
            srcArr[indexA] = srcArr[indexB];
            srcArr[indexB] = temp;
        };
        /**
         * 随机排序数组
         * @srcArr 源数组
         */
        ArrayTool.randSort = function (srcArr) {
            var len = srcArr.length;
            for (var i = 0; i < len; i++) {
                this.swap(srcArr, i, Tpm.NumberTool.getRandInt(0, len - 1));
            }
        };
        /**
         * 时间转换,整体
         * 2017-4-6 16:46:29
         */
        ArrayTool.formatDate = function (timeS) {
            var time = new Date(parseInt(timeS) * 1000);
            return time.getFullYear() + "-" + (time.getMonth() + 1) + "-" + time.getDate() + " " + time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();
        };
        /**
         * 时间转换,日期
         * 2017-04-06
         */
        ArrayTool.formatDate1 = function (timeS) {
            var time = new Date(parseInt(timeS) * 1000);
            return ArrayTool.aze(time.getFullYear()) + "-" + ArrayTool.aze((time.getMonth() + 1)) + "-" + ArrayTool.aze(time.getDate());
        };
        /**
         * 时间转换,时，分，秒
         * 16:46:29
         */
        ArrayTool.formatDate2 = function (timeS) {
            var time = new Date(parseInt(timeS) * 1000);
            return ArrayTool.aze(time.getHours()) + ":" + ArrayTool.aze(time.getMinutes()) + ":" + ArrayTool.aze(time.getSeconds());
        };
        ArrayTool.aze = function (num) {
            if (num > 9) {
                return "" + num;
            }
            else {
                return "0" + num;
            }
        };
        /**
         * 获取object长度
         * @param obj 待判断Object
         * @returns object长度
         */
        ArrayTool.getObjectLength = function (obj) {
            var sum = 0;
            for (var key in obj) {
                sum++;
            }
            return sum;
        };
        /**
         * 对象深拷贝
         * @author huanglong
         * @obj 源对象
         */
        ArrayTool.deepCopy = function (obj) {
            var newObj;
            if (typeof obj == "object") {
                if (obj === null) {
                    newObj = null;
                }
                else if (obj == undefined) {
                    newObj = undefined;
                }
                else {
                    if (obj instanceof Array) {
                        newObj = [];
                        for (var i = 0, len = obj.length; i < len; i++) {
                            newObj.push(ArrayTool.deepCopy(obj[i]));
                        }
                    }
                    else {
                        newObj = {};
                        for (var k in obj) {
                            newObj[k] = ArrayTool.deepCopy(obj[k]);
                        }
                    }
                }
            }
            else {
                newObj = obj;
            }
            return newObj;
        };
        return ArrayTool;
    }());
    Tpm.ArrayTool = ArrayTool;
    __reflect(ArrayTool.prototype, "Tpm.ArrayTool");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ArrayTool.js.map