module Tpm {
    /**
     * 游戏数据
     */
    export class GameInfo {

    }

    /**
     * 动作状态值
     */
    export enum ACT_state {   //00000001    0pass  1hu 二进制
        Act_Cancle = -1,        //取消
        Act_Pass = 0,           //过
        Act_Out = 10,           //出牌
        Act_Chi = 20,           //吃
        Act_Peng = 30,          //碰
        Act_Gang = 40,          //杠
        Act_BuGang = 50,        //补杠
        Act_AnGang = 60,        //暗杠
        Act_Ting = 70,          //听
        Act_DianHu = 80,        //胡
        Act_Zimo = 90,          //自摸
        Act_Fa = 100,           //首次发牌
        Act_Guohu = 104,        //过胡
        Act_ZuheGang = 101,     //前端自定义
        Act_Buhua = 103         //补花
    };

    /**
     * 动作
     */
    export enum ACT_act {
        Act_cancle = -3,    // 取消
        Act_ChangeCard = -2,// 换牌， 回放用
        Act_GetCard = -1,//摸牌,回放用
        Act_Pass = 0,   //不吃、碰、杠、胡等
        Act_NormalDo,   //出牌
        Act_Ting,       //听
        Act_Chi,        //吃
        Act_Peng,       //碰
        Act_Gang,       //杠
        Act_AnGang,     //暗杠
        Act_Hu,         //胡
        Act_Buhua,       //补花
        Act_zimo,        //自摸,额外添加
        Act_Guohu,       //过胡
    };


    //游戏状态
    export enum GS_GAME_STATION {
        GS_WAIT_SETGAME = 0,    // 等待设置游戏
        GS_WAIT_ARGEE,			// 等待玩家同意游戏
        GS_GAME_PLAYING,		// 游戏中
        GS_GAME_FINSHED,		// 游戏结束
    };

    //玩家状态  1111二进制表示，可多种状态叠加
    export enum PLAYER_STATE {
        TRSHIP = 1,	// 托管
        ESC = 2,	// 逃跑
        READY = 4,	// 准备
        SETTLE = 8,	// 结算
    };

    //人物坐的实际位置，上下左右
    export enum UserPosition {
        NULL = -1,
        Down = 0,
        Up = 1,
        R = 2,
        L = 3,
    }

    /**性别类型*/
    export enum SEX_TYPE {
        boy = 1,
        girl = 2,
        unknow = 3
    }

    /**游戏状态*/
    export enum GameState {
        Free,        //空闲
        Ready,       //准备阶段
        DealCard,    //发牌阶段
        Playing,     //游戏阶段
        Over         //游戏结束
    }

    /**服务端用户状态 */
    export enum UserState {
        UNREADY = 1,    // 待准备
        READY = 2,      // 准备中
        PLAYING = 3,    // 游戏中
        ESCAPE = 4,     // 逃跑
        OFFLINE = 5,    // 离线
    }

    /**
     * 牌名称
     */
    export class CardName {
        public static Name = {
            "17": "一万",
            "18": "二万",
            "19": "三万",
            "20": "四万",
            "21": "五万",
            "22": "六万",
            "23": "七万",
            "24": "八万",
            "25": "九万",

            "65": "东",
            "66": "南",
            "67": "西",
            "68": "北",

            "81": "中",
            "82": "发",
            "83": "白"
        }
    }

    /**
     * 胡牌类型
     */
    export class HuType {
        public static HuTypeName = {
            "1000": "屁胡",
            "1001": "一般高",
            "1002": "连六",
            "1003": "老少妇",
            "1004": "幺九刻",
            "1005": "明杠",
            "1006": "边张",
            "1007": "坎张",
            "1008": "单钓将",
            "1009": "自摸",

            "1021": "箭刻",
            "1022": "门前清",
            "1023": "平胡",
            "1024": "四归一",
            "1025": "双暗刻",
            "1026": "暗杠",
            "1027": "断幺",
            "1028": "报听",

            "1041": "全带幺",
            "1042": "不求人",
            "1043": "双明杠",
            "1044": "胡绝张",

            "1061": "碰碰胡",
            "1062": "混一色",
            "1063": "全球人",
            "1064": "双箭刻",
            
            "1081": "妙手回春",
            "1082": "海底捞月",
            "1083": "杠上开花",
            "1084": "抢杠胡",
            "1085": "双暗杠",

            "1121": "三风刻",
            "1161": "清龙",
            "1162": "一色三步高",
            "1163": "三暗刻",

            "1242": "清一色",
            "1243": "一色三同顺",
            "1244": "一色三节高",

            "1321": "一色四步高",
            "1322": "三杠",
            "1323": "混幺九",
            "1324": "天听",

            "1481": "一色四同顺",
            "1482": "一色四节高",

            "1641": "小四喜",
            "1642": "小三元",
            "1643": "四暗刻",
            "1644": "字一色",
            "1645": "一色双龙会",
            "1646": "人胡",

            "1881": "大四喜",
            "1882": "大三元",
            "1883": "九莲宝灯",
            "1884": "四杠",
            "1886": "天胡",
            "1887": "地胡",

            "2000": "七对",
            "2885": "七连对",

            "3000": "十三幺"
        }

        /**
         * 获取牌型番数
         */
        public static getHuTypeFan(huType: number) {
            return Math.floor((huType%1000)/10) || 1;
        }
    }
}