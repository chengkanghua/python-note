var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 单个场的相关配置
     */
    var RoomData = (function () {
        function RoomData() {
        }
        /**初始化数据 */
        RoomData.prototype.initData = function (data) {
            this.roomType = data.room_type;
            this.roomName = data.name;
            this.minEnterGold = data.min_enter_gold;
            this.maxEnterGold = data.max_enter_gold;
            this.minPlayGold = data.min_play_gold;
            this.recommendPayNum = data.recommend_pay_num;
            this.outCardTime = data.draw_card_time;
            this.serviceCharge = data.service_charge;
            this.baseBet = data.base_bet;
            this.minHuFan = data.min_hu_fan;
            this.maxHuFan = data.max_hu_fan;
            this.specialRule = data.special_rule;
            this.curPlayerCount = data.cur_player_count;
        };
        return RoomData;
    }());
    Tpm.RoomData = RoomData;
    __reflect(RoomData.prototype, "Tpm.RoomData");
    /**房间场类型 */
    var RoomType;
    (function (RoomType) {
        RoomType[RoomType["noob"] = 0] = "noob";
        RoomType[RoomType["middle"] = 1] = "middle";
        RoomType[RoomType["high"] = 2] = "high";
    })(RoomType = Tpm.RoomType || (Tpm.RoomType = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=RoomData.js.map