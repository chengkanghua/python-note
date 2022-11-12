module Tpm {
    /**
     * 消息暂存
     * 保存收到的后端消息，延时处理
     */
    export class MsgCache {
        private dataList: any;
        private callBackList: any;
        private objList: any;

        public constructor() {
            this.dataList = {};
            this.callBackList = {};
            this.objList = {};
        }

        /**
         * 添加消息数据、处理函数
         */
        public addMsg(proto: string, data: any, callback: Function, obj: any) {
            this.dataList[proto] = data;
            this.callBackList[proto] = callback;
            this.objList[proto] = obj;
        }

        /**
         * 删除
         */
        private minusMsg(proto: string) {
            delete this.dataList[proto];
            delete this.callBackList[proto];
            delete this.objList[proto];
        }

        /**
         * 执行指定处理函数
         */
        public exeMsg(proto: string, deleteFlag: boolean = true) {
            var callBack = this.callBackList[proto];
            var thisObject = this.objList[proto];
            var data = this.dataList[proto];
            if (callBack && thisObject) {
                callBack.call(thisObject, data);
            }
            deleteFlag && this.minusMsg(proto);
        }

        /**
         * 添加数据
         * @param arrayFlag 是否需要用数组存
         */
        public addMsgData(proto: string, data: any = null, arrayFlag: boolean = false) {
            if (arrayFlag) {
                if (!this.dataList[proto]) {
                    this.dataList[proto] = [];
                }
                this.dataList[proto].push(data)
            }
            else {
                this.dataList[proto] = data;
            }
        }

        /**
         * 获取指定数据
         * @param deleteFlag 获取后是否清除msgCache中的数据
         */
        public getMsgData(proto: string, deleteFlag: boolean = true) {
            var data = ArrayTool.deepCopy(this.dataList[proto]);
            deleteFlag && this.minusMsg(proto);
            return data;
        }
    }
}