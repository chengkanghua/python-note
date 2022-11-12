var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**WEB数据结构
     * 返回的数据中  ret为消息码 0为正常  其他值非正常
     * desc为消息描述 出现错误时会有相应的描述
     * action为相应动作
     * data为需要接收的主体数据
    */
    var ProtocolHttpData = (function () {
        function ProtocolHttpData() {
        }
        return ProtocolHttpData;
    }());
    /**登录返回 */
    ProtocolHttpData.LoginData = {
        ret: 0,
        action: "handler.login_handler",
        data: {
            diamond: 0,
            uid: 0,
            avater_url: "",
            ip: "",
            sex: 0,
            user: "",
            password: "",
            port: 0,
            accid: 0,
            skey: "",
            name: "",
            point: 0,
            payment: 0,
            is_visitor: 0,
            money: 0
        },
        desc: "success"
    };
    /**注册返回 */
    ProtocolHttpData.RegisterData = {
        ret: 0,
        action: "handler.register_handler",
        data: {
            diamond: 0,
            uid: 0,
            avater_url: "",
            ip: "",
            sex: 0,
            user: "",
            password: "",
            port: 0,
            accid: 0,
            skey: "",
            name: "",
            point: 0,
            payment: 0,
            is_visitor: 0,
            money: 0
        },
        desc: "success"
    };
    /**商城列表数据*/
    ProtocolHttpData.GoodsListData = {
        ret: -1,
        action: "",
        data: [],
        desc: ""
    };
    /**商城列表单条数据*/
    ProtocolHttpData.GoodsListItemData = {
        icon: "",
        title: "",
        rmb_price: 0,
        selling_price: 0,
        id: 0,
    };
    /**邮件列表数据*/
    ProtocolHttpData.EmailListData = {
        ret: -1,
        action: "",
        data: [],
        desc: ""
    };
    /**邮件列表单条数据*/
    ProtocolHttpData.EmailListItemData = {
        icon: "",
        // is_read: "0",           //该邮件是否已读
        time_desc: "",
        id: 0,
        title: "",
        content: "" //邮件内容
    };
    /**邮件详情数据 */
    ProtocolHttpData.emailDeatilData = {
        data: {
            content: "",
            reward: [],
            is_receive: "0",
            eid: 0,
            title: "" //邮件标题
        },
        ret: -1,
        desc: "success"
    };
    /**奖品单个数据 */
    ProtocolHttpData.RewardItem = {
        reward_name: "局数卡",
        reward_quantity: "0",
        reward_icon: 0 //奖品类型
    };
    /**玩家个人信息*/
    ProtocolHttpData.PersonalInfoData = {
        data: {
            point: 0,
            accid: -1,
            uid: 0,
            winning_rate: "0",
            avater_url: "",
            total: 0,
            sex: 0,
            highest_winning_streak: 0,
            nick_name: "",
            diamond: 0,
            money: 0 //金币数
        },
        ret: 0,
        desc: ""
    };
    /**金币不足*/
    ProtocolHttpData.MoneyNotEnoughData = {
        lowestmoney: 8000,
        type: "高",
        selling_price: 10,
        quantity: 5000,
    };
    /**破产补助*/
    ProtocolHttpData.GiveMoneyData = {
        ret: 0,
        desc: "success",
        data: {
            income_support_times: 0,
            allcount: "三",
            money: 80000,
        }
    };
    /**获取房间信息 */
    ProtocolHttpData.RoomInfoData = {
        ret: 0,
        desc: "success",
        data: {
            room_cfg_info: [
                {
                    max_enter_gold: 0,
                    recommend_pay_num: 0,
                    draw_card_time: 0,
                    id: 1,
                    service_charge: 0,
                    base_bet: 0,
                    max_hu_fan: 0,
                    min_hu_fan: 6,
                    name: "初级场",
                    cur_player_count: 0,
                    min_play_gold: 0,
                    special_rule: "{}",
                    min_enter_gold: 0,
                    room_type: 0 // 0初级场,1中级场,2高级场
                }
            ]
        }
    };
    Tpm.ProtocolHttpData = ProtocolHttpData;
    __reflect(ProtocolHttpData.prototype, "Tpm.ProtocolHttpData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolHttpData.js.map