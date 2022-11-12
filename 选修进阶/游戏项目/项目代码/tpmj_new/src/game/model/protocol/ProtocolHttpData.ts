module Tpm {
	/**WEB数据结构  
	 * 返回的数据中  ret为消息码 0为正常  其他值非正常
	 * desc为消息描述 出现错误时会有相应的描述
	 * action为相应动作
	 * data为需要接收的主体数据
	*/
	export class ProtocolHttpData {

		/**登录返回 */
		public static LoginData = {
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
		}
		
		/**注册返回 */
		public static RegisterData = {
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
		}

		/**商城列表数据*/
		public static GoodsListData = {
			ret: -1,
			action: "",
			data: [],                  //单条数据为GoodsListItemData
			desc: ""
		}

		/**商城列表单条数据*/
		public static GoodsListItemData = {
			icon:"",
			title: "",               //商品描述
			rmb_price:0,             //商品价格（RMB）
			selling_price: 0,       //商品价格（钻石）
			id: 0,                  //商品ID
		}

		/**邮件列表数据*/
		public static EmailListData = {
			ret: -1,
			action: "",
			data: [],               //单条数据为Good
			desc: ""
		}

		/**邮件列表单条数据*/
		public static EmailListItemData = {
			icon:"",                 //使用的图标 
			// is_read: "0",           //该邮件是否已读
			time_desc: "",          //邮件发送时间
			id: 0,                //邮件ID
			title: "",               //邮件标题
			content:""               //邮件内容
		}

		/**邮件详情数据 */
		public static emailDeatilData = {
			data: {
				content: "",
				reward: [],        //单条数据为RewardItem
				is_receive: "0",   //是否已领取奖励
				eid: 0,            //邮件ID
				title: ""          //邮件标题
			},
			ret: -1,
			desc: "success"
		}

		/**奖品单个数据 */
		public static RewardItem = {
			reward_name: "局数卡",     //奖品名称
			reward_quantity: "0",     //奖品数量
			reward_icon: 0            //奖品类型
		}

		/**玩家个人信息*/
		public static PersonalInfoData = {
			data: {
				point: 0,                //玩家总积分
				accid: -1,               //玩家平台ID
				uid: 0,                  //玩家游戏ID
				winning_rate: "0",        //玩家胜率
				avater_url: "",          //玩家头像地址
				total: 0,           //玩家总游戏场数
				sex: 0,                  //玩家性别
				highest_winning_streak: 0,//玩家最高连胜 
				nick_name: "",                  //玩家昵称  
				diamond:0,                //钻石数
				money:0                    //金币数
			},
			ret: 0,
			desc: ""
		}

		/**金币不足*/
		public static MoneyNotEnoughData = {
			lowestmoney:8000,       //最低要求金币数
			type:"高",             //房间类型
			selling_price: 10,     //商品价格
			quantity: 5000,     //商品数量
		}

		/**破产补助*/
		public static GiveMoneyData = {
			ret: 0,
			desc: "success",
			data: {
				income_support_times:0,          //领取次数
				allcount: "三",      //总共可领取次数
				money: 80000,     //赠送金币数量
			}
		}

		/**获取房间信息 */
		public static RoomInfoData = {
			ret: 0,
			desc: "success",
			data: {
				room_cfg_info:[
					{
						max_enter_gold: 0,  	//  进入上限
						recommend_pay_num: 0,  //  推荐支付金额  元
						draw_card_time: 0,  	//  动作间隔时间
						id: 1,               	//  房间配置ID
						service_charge: 0,  	//  台费
						base_bet: 0,        	//  底注
						max_hu_fan: 0,       	//  最大胡牌番数
						min_hu_fan: 6,       	//  最小胡牌番数
						name: "初级场",       		//  场次名字
						cur_player_count: 0, 	//  该场次当前人数
						min_play_gold: 0,  	//  玩牌下限
						special_rule: "{}",      //  特殊规则
						min_enter_gold: 0,    // 最小进入金币
						room_type: 0            // 0初级场,1中级场,2高级场
					}
				]
			}
		}
	}
}