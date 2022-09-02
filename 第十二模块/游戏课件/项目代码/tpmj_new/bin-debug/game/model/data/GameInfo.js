var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 游戏数据
     */
    var GameInfo = (function () {
        function GameInfo() {
        }
        return GameInfo;
    }());
    Tpm.GameInfo = GameInfo;
    __reflect(GameInfo.prototype, "Tpm.GameInfo");
    /**
     * 动作状态值
     */
    var ACT_state;
    (function (ACT_state) {
        ACT_state[ACT_state["Act_Cancle"] = -1] = "Act_Cancle";
        ACT_state[ACT_state["Act_Pass"] = 0] = "Act_Pass";
        ACT_state[ACT_state["Act_Out"] = 10] = "Act_Out";
        ACT_state[ACT_state["Act_Chi"] = 20] = "Act_Chi";
        ACT_state[ACT_state["Act_Peng"] = 30] = "Act_Peng";
        ACT_state[ACT_state["Act_Gang"] = 40] = "Act_Gang";
        ACT_state[ACT_state["Act_BuGang"] = 50] = "Act_BuGang";
        ACT_state[ACT_state["Act_AnGang"] = 60] = "Act_AnGang";
        ACT_state[ACT_state["Act_Ting"] = 70] = "Act_Ting";
        ACT_state[ACT_state["Act_DianHu"] = 80] = "Act_DianHu";
        ACT_state[ACT_state["Act_Zimo"] = 90] = "Act_Zimo";
        ACT_state[ACT_state["Act_Fa"] = 100] = "Act_Fa";
        ACT_state[ACT_state["Act_Guohu"] = 104] = "Act_Guohu";
        ACT_state[ACT_state["Act_ZuheGang"] = 101] = "Act_ZuheGang";
        ACT_state[ACT_state["Act_Buhua"] = 103] = "Act_Buhua"; //补花
    })(ACT_state = Tpm.ACT_state || (Tpm.ACT_state = {}));
    ;
    /**
     * 动作
     */
    var ACT_act;
    (function (ACT_act) {
        ACT_act[ACT_act["Act_cancle"] = -3] = "Act_cancle";
        ACT_act[ACT_act["Act_ChangeCard"] = -2] = "Act_ChangeCard";
        ACT_act[ACT_act["Act_GetCard"] = -1] = "Act_GetCard";
        ACT_act[ACT_act["Act_Pass"] = 0] = "Act_Pass";
        ACT_act[ACT_act["Act_NormalDo"] = 1] = "Act_NormalDo";
        ACT_act[ACT_act["Act_Ting"] = 2] = "Act_Ting";
        ACT_act[ACT_act["Act_Chi"] = 3] = "Act_Chi";
        ACT_act[ACT_act["Act_Peng"] = 4] = "Act_Peng";
        ACT_act[ACT_act["Act_Gang"] = 5] = "Act_Gang";
        ACT_act[ACT_act["Act_AnGang"] = 6] = "Act_AnGang";
        ACT_act[ACT_act["Act_Hu"] = 7] = "Act_Hu";
        ACT_act[ACT_act["Act_Buhua"] = 8] = "Act_Buhua";
        ACT_act[ACT_act["Act_zimo"] = 9] = "Act_zimo";
        ACT_act[ACT_act["Act_Guohu"] = 10] = "Act_Guohu";
    })(ACT_act = Tpm.ACT_act || (Tpm.ACT_act = {}));
    ;
    //游戏状态
    var GS_GAME_STATION;
    (function (GS_GAME_STATION) {
        GS_GAME_STATION[GS_GAME_STATION["GS_WAIT_SETGAME"] = 0] = "GS_WAIT_SETGAME";
        GS_GAME_STATION[GS_GAME_STATION["GS_WAIT_ARGEE"] = 1] = "GS_WAIT_ARGEE";
        GS_GAME_STATION[GS_GAME_STATION["GS_GAME_PLAYING"] = 2] = "GS_GAME_PLAYING";
        GS_GAME_STATION[GS_GAME_STATION["GS_GAME_FINSHED"] = 3] = "GS_GAME_FINSHED";
    })(GS_GAME_STATION = Tpm.GS_GAME_STATION || (Tpm.GS_GAME_STATION = {}));
    ;
    //玩家状态  1111二进制表示，可多种状态叠加
    var PLAYER_STATE;
    (function (PLAYER_STATE) {
        PLAYER_STATE[PLAYER_STATE["TRSHIP"] = 1] = "TRSHIP";
        PLAYER_STATE[PLAYER_STATE["ESC"] = 2] = "ESC";
        PLAYER_STATE[PLAYER_STATE["READY"] = 4] = "READY";
        PLAYER_STATE[PLAYER_STATE["SETTLE"] = 8] = "SETTLE";
    })(PLAYER_STATE = Tpm.PLAYER_STATE || (Tpm.PLAYER_STATE = {}));
    ;
    //人物坐的实际位置，上下左右
    var UserPosition;
    (function (UserPosition) {
        UserPosition[UserPosition["NULL"] = -1] = "NULL";
        UserPosition[UserPosition["Down"] = 0] = "Down";
        UserPosition[UserPosition["Up"] = 1] = "Up";
        UserPosition[UserPosition["R"] = 2] = "R";
        UserPosition[UserPosition["L"] = 3] = "L";
    })(UserPosition = Tpm.UserPosition || (Tpm.UserPosition = {}));
    /**性别类型*/
    var SEX_TYPE;
    (function (SEX_TYPE) {
        SEX_TYPE[SEX_TYPE["boy"] = 1] = "boy";
        SEX_TYPE[SEX_TYPE["girl"] = 2] = "girl";
        SEX_TYPE[SEX_TYPE["unknow"] = 3] = "unknow";
    })(SEX_TYPE = Tpm.SEX_TYPE || (Tpm.SEX_TYPE = {}));
    /**游戏状态*/
    var GameState;
    (function (GameState) {
        GameState[GameState["Free"] = 0] = "Free";
        GameState[GameState["Ready"] = 1] = "Ready";
        GameState[GameState["DealCard"] = 2] = "DealCard";
        GameState[GameState["Playing"] = 3] = "Playing";
        GameState[GameState["Over"] = 4] = "Over"; //游戏结束
    })(GameState = Tpm.GameState || (Tpm.GameState = {}));
    /**服务端用户状态 */
    var UserState;
    (function (UserState) {
        UserState[UserState["UNREADY"] = 1] = "UNREADY";
        UserState[UserState["READY"] = 2] = "READY";
        UserState[UserState["PLAYING"] = 3] = "PLAYING";
        UserState[UserState["ESCAPE"] = 4] = "ESCAPE";
        UserState[UserState["OFFLINE"] = 5] = "OFFLINE";
    })(UserState = Tpm.UserState || (Tpm.UserState = {}));
    /**
     * 牌名称
     */
    var CardName = (function () {
        function CardName() {
        }
        return CardName;
    }());
    CardName.Name = {
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
    };
    Tpm.CardName = CardName;
    __reflect(CardName.prototype, "Tpm.CardName");
    /**
     * 胡牌类型
     */
    var HuType = (function () {
        function HuType() {
        }
        /**
         * 获取牌型番数
         */
        HuType.getHuTypeFan = function (huType) {
            return Math.floor((huType % 1000) / 10) || 1;
        };
        return HuType;
    }());
    HuType.HuTypeName = {
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
    };
    Tpm.HuType = HuType;
    __reflect(HuType.prototype, "Tpm.HuType");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameInfo.js.map