var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 接收数据结构定义
     */
    var ProtocolDataRev = (function () {
        function ProtocolDataRev() {
        }
        return ProtocolDataRev;
    }());
    /**失败消息的统一数据结构 */
    ProtocolDataRev.R_Fail = {
        "code": 110,
        "desc": "fail desc"
    };
    ProtocolDataRev.R_100002 = {
        code: 200,
        info: {
            room: null,
            old_session: null,
            reconnect: false
        }
    };
    ProtocolDataRev.R_100010 = {
        code: 200,
        info: {
            game_data: {
                desk_info: {
                    bank_seat_id: 0,
                    desk_id: 0,
                    remain_count: 0,
                    room_type: 0,
                    status: 0
                },
                player_info: [
                    {
                        seat_id: 0,
                        bu_hua_num: 0,
                        guo_hu_num: 0,
                        is_ting: 0,
                        last_card: 0,
                        hand_card_by_order: [[], [], []],
                        out_card: []
                    }
                ],
                wait_task: {
                    command_id: 0,
                    end_time: 1,
                    params: {
                        seat_id: 0,
                        end_time: 0,
                        act_info: {}
                    }
                }
            },
            user_info: []
        }
    };
    ProtocolDataRev.R_100100 = {
        code: 200,
        info: {
            ready: 0
        }
    };
    ProtocolDataRev.R_100104 = {
        code: 200,
        info: {
            "desk_id": 100000,
            room_type: 1,
            "seat_info": {
                "0": {
                    "status": 1,
                    "nick": "11",
                    "seat_id": 0,
                    "user_id": 1,
                    "point": 4000
                }
            }
        }
    };
    ProtocolDataRev.R_100105 = {
        code: 200,
        info: {
            desk_id: 0,
            seat_info: {
                "0": {
                    "status": 1,
                    "nick": "11",
                    "seat_id": 0,
                    "user_id": 1,
                    "point": 4000
                }
            }
        }
    };
    ProtocolDataRev.R_101001 = {
        code: 200,
        info: {
            seat_id: 0,
            act_info: {}
        }
    };
    ProtocolDataRev.R_101002 = {
        code: 200,
        info: {
            seat_id: 0,
            remain_count: 0,
            card_list: []
        }
    };
    ProtocolDataRev.R_101003 = {
        code: 200,
        info: {
            player_info: {
                "0": {
                    hand_card: [[], []]
                },
                "1": {
                    hand_card: [[], []]
                }
            }
        }
    };
    ProtocolDataRev.R_101004 = {
        code: 200,
        info: {
            bank_seat_id: 0,
            dice: []
        }
    };
    ProtocolDataRev.R_101005 = {
        code: 200,
        info: {
            card_list: [
                {
                    seat_id: 0,
                    card_list: [] // 具体牌的数据 如果 当前任务seat_id=0 则能看见该数组数据
                },
                {
                    seat_id: 0,
                    card_list: [] // 具体牌的数据 如果 当前任务seat_id=1 则能看见该数组数据
                }
            ]
        }
    };
    ProtocolDataRev.R_101006 = {
        code: 200,
        info: {
            total_points: [],
            detail: [{
                    params: {
                        guo_hu_count: 0,
                        hand_card_for_settle_show: [],
                        hu_fan_count: 0,
                        hu_seat_id: 0,
                        source_seat_id: 0,
                        type_list: []
                    },
                    points: [],
                    type: 1
                }]
        }
    };
    ProtocolDataRev.R_101008 = {
        code: 200,
        info: {
            seat_id: 0,
            hua_card: [],
            bu_cards: []
        }
    };
    ProtocolDataRev.R_101100 = {
        code: 200,
        info: {
            user_id: 0,
            seat_id: 0,
            point: 0
        }
    };
    ProtocolDataRev.R_101101 = {
        code: 200,
        info: {
            code: 0,
            desc: []
        }
    };
    ProtocolDataRev.R_101105 = {
        code: 200,
        info: {
            user_id: 0,
            nick: ""
        }
    };
    ProtocolDataRev.R_101106 = {
        code: 200,
        info: {
            user_id: 0,
            nick: "",
            ready: 0
        }
    };
    ProtocolDataRev.R_101107 = {
        code: 200,
        info: {
            status: 0,
            nick: "",
            seat_id: 0,
            user_id: 0,
            point: 0
        }
    };
    ProtocolDataRev.R_101109 = {
        code: 200,
        info: {
            user_id: 0,
            nick: ""
        }
    };
    ProtocolDataRev.R_101110 = {
        code: 200,
        info: {
            user_id: 0,
            nick: "",
            status: 0
        }
    };
    ProtocolDataRev.R_101112 = {
        code: 200,
        info: {
            card_list: [97],
            seat_id: 0,
            all_hand_cards: {
                "0": {
                    an_gang_cards: [],
                    hand_card: []
                },
                "1": {
                    an_gang_cards: [],
                    hand_card: []
                }
            },
            act_type: 10 // 执行动作类型
        }
    };
    ProtocolDataRev.R_101007 = {
        code: 200,
        info: {
            hua_card_list: [],
            seat_id: 0
        }
    };
    ProtocolDataRev.R_100999 = {
        code: 200,
        info: {
            test_type: 0,
            hand_card: [],
            cards: []
        }
    };
    Tpm.ProtocolDataRev = ProtocolDataRev;
    __reflect(ProtocolDataRev.prototype, "Tpm.ProtocolDataRev");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ProtocolDataRev.js.map