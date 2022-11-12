var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var StringTool = (function () {
        function StringTool() {
        }
        /**
         * 删除左右两端的空格.   " abc " - > "abc"
         * @str 待处理字符串
         * @return 处理后字符串
         */
        StringTool.trim = function (str) {
            return str.replace(/(^\s*)|(\s*$)/g, "");
        };
        /**
         * 将字符串截取到指定字符数，多余的用"..."表示
         * @str 昵称字符串
         * @charMax 字符限制(中文、大写字母占2， 其余占1)
         */
        StringTool.formatNickName = function (str, charMax) {
            if (charMax === void 0) { charMax = 10; }
            if (!str) {
                // console.error("nickname error");
                return;
            }
            var msg = this.getStrLength(str, charMax);
            var len = msg[0];
            if (len > charMax) {
                return str.substr(0, msg[1]) + "...";
            }
            return str;
        };
        /**
         * 获取字符串长度，中文、大写字母占2， 其他占1 (Egret中文英文字符都是占1)
         * @str 字符串
         * @reutrn 长度
         */
        StringTool.getStrLength = function (str, charMax) {
            if (charMax === void 0) { charMax = 10; }
            var len = 0;
            var charCode = 0;
            var count = 0;
            for (var i = 0; i < str.length; i++) {
                charCode = str.charCodeAt(i);
                if (charCode > 127 || (charCode >= 65 && charCode <= 90)) {
                    len += 2;
                    if (len <= charMax)
                        count++;
                }
                else {
                    len++;
                    if (len <= charMax)
                        count++;
                }
            }
            return [len, count];
        };
        return StringTool;
    }());
    Tpm.StringTool = StringTool;
    __reflect(StringTool.prototype, "Tpm.StringTool");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=StringTool.js.map