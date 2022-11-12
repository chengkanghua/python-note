module Tpm {
    /**
     * 发送数据结构定义
     */
    export class ProtocolDataSend {
        /**空参数 */
        public static S_common = {

        }

        public static S_100002 = {
            user_id: 0,     //用户id
            passwd: ""      //密码 md5
        }

        public static S_100010 = {
            user_id: 0
        }

        public static S_100100 = {
            user_id: 0,
            ready: 0        //0：未准备  1：准备
        }

        public static S_100103 = {
            user_id: 0
        }

        public static S_100104 = {
            user_id: 0
        }

        public static S_100105 = {
            user_id: 0,
            room_type: 0
        }

        public static S_100130 = {
            user_id: 0
        }

        public static S_100140 = {
            user_id: 0,
            act: 0,
            act_params: null
        }

        public static S_100112 = {
            user_id: 0
        }

        public static S_100999 = {
            user_id: 0,
            test_type: 0, //1:换牌, 2:确定接下来的牌, 3:查看最后一张
            test_params: "{}"
        }
    }
}