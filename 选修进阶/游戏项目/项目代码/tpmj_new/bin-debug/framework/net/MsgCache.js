var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 消息暂存
     * 保存收到的后端消息，延时处理
     */
    var MsgCache = (function () {
        function MsgCache() {
            this.dataList = {};
            this.callBackList = {};
            this.objList = {};
        }
        /**
         * 添加消息数据、处理函数
         */
        MsgCache.prototype.addMsg = function (proto, data, callback, obj) {
            this.dataList[proto] = data;
            this.callBackList[proto] = callback;
            this.objList[proto] = obj;
        };
        /**
         * 删除
         */
        MsgCache.prototype.minusMsg = function (proto) {
            delete this.dataList[proto];
            delete this.callBackList[proto];
            delete this.objList[proto];
        };
        /**
         * 执行指定处理函数
         */
        MsgCache.prototype.exeMsg = function (proto, deleteFlag) {
            if (deleteFlag === void 0) { deleteFlag = true; }
            var callBack = this.callBackList[proto];
            var thisObject = this.objList[proto];
            var data = this.dataList[proto];
            if (callBack && thisObject) {
                callBack.call(thisObject, data);
            }
            deleteFlag && this.minusMsg(proto);
        };
        /**
         * 添加数据
         * @param arrayFlag 是否需要用数组存
         */
        MsgCache.prototype.addMsgData = function (proto, data, arrayFlag) {
            if (data === void 0) { data = null; }
            if (arrayFlag === void 0) { arrayFlag = false; }
            if (arrayFlag) {
                if (!this.dataList[proto]) {
                    this.dataList[proto] = [];
                }
                this.dataList[proto].push(data);
            }
            else {
                this.dataList[proto] = data;
            }
        };
        /**
         * 获取指定数据
         * @param deleteFlag 获取后是否清除msgCache中的数据
         */
        MsgCache.prototype.getMsgData = function (proto, deleteFlag) {
            if (deleteFlag === void 0) { deleteFlag = true; }
            var data = Tpm.ArrayTool.deepCopy(this.dataList[proto]);
            deleteFlag && this.minusMsg(proto);
            return data;
        };
        return MsgCache;
    }());
    Tpm.MsgCache = MsgCache;
    __reflect(MsgCache.prototype, "Tpm.MsgCache");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=MsgCache.js.map