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
    var KeyWord = (function (_super) {
        __extends(KeyWord, _super);
        function KeyWord() {
            var _this = _super.call(this) || this;
            _this.init();
            return _this;
        }
        //初始化
        KeyWord.prototype.init = function () {
            var data = RES.getRes("kwx_keywordConfig_json");
            this.keyWordList = data.keyword.split("|");
        };
        /**
         * 过滤字符串
         * @msg 需要检查的字符串
         * @return 处理后的字符串
         */
        KeyWord.prototype.filteString = function (msg) {
            if (this.isInit()) {
                var len = this.keyWordList.length;
                var reg;
                for (var i = 0; i < len; i++) {
                    reg = new RegExp(this.keyWordList[i], "i");
                    if (msg.search(reg) != -1) {
                        console.log("包含敏感关键词:", this.keyWordList[i]);
                        var strLen = this.keyWordList[i].length;
                        var replaceStr = "";
                        for (var j = 0; j < strLen; j++) {
                            replaceStr += "*";
                        }
                        msg = msg.replace(reg, replaceStr);
                    }
                }
                return msg;
            }
            return "***";
        };
        /**
         * 检查字符串是否包含关键词
         * @msg 待检查的字符串
         * @return 返回字符串是否合格
         */
        KeyWord.prototype.checkStringOK = function (msg) {
            if (this.isInit()) {
                var len = this.keyWordList.length;
                var reg;
                for (var i = 0; i < len; i++) {
                    reg = new RegExp(this.keyWordList[i], "i");
                    if (msg.match(reg) != null) {
                        return false;
                    }
                }
                return true;
            }
            return false;
        };
        /**是否初始化过*/
        KeyWord.prototype.isInit = function () {
            return (this.keyWordList != null);
        };
        return KeyWord;
    }(Tpm.SingleClass));
    Tpm.KeyWord = KeyWord;
    __reflect(KeyWord.prototype, "Tpm.KeyWord");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=KeyWord.js.map