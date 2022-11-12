# echecs


一、 消息ID 定义
```
HEART_BEAT = 10000
USER_LOGIN = 100002                 # 登录
USER_RECONNECT = 100010             # 断线重连
USER_READY = 100162                 # 玩家准备
CREATE_FRIEND_DESK = 101000         # 创建好友房
JOIN_FRIEND_DESK = 101001           # 加入好友房
DISSOLVE_FRIEND_DESK = 100151       # 解散房间
DISSOLVE_DESK_ANSWER = 100156       # 解散房间应答
USER_EXIT_DESK = 100157             # 玩家退出桌子
USER_SET_CONFIG = 100158            # 自定义配置

USER_CANCEL_READY = 100164

PUSH_CALL_CARD = 101001        # 推送玩家叫牌
PUSH_DRAW_CARD = 101002        # 推送玩家摸牌
PUSH_GAME_OVER = 101003        # 推送游戏结束
PUSH_GEN_BANK  = 101004        # 推送定庄信息
PUSH_DEAL_CARD = 101005        # 推送发牌信息
PUSH_GAME_SETTLE = 101006      # 推送游戏结算


PUSH_USER_POINT = 101100                # 推送玩家点数发生变化
PUSH_USER_OTHER_LOGIN = 101101          # 推送玩家在其他地方登录
PUSH_DESK_DISSOLVE_RESULT = 101102      # 推送桌子解散结果
PUSH_DESK_DISSOLVE = 101103             # 推送有玩家请求解散桌子
PUSH_DESK_DISSOLVE_ANSWER = 101104      # 推送玩家对解散桌子的响应
PUSH_USER_EXIT = 101105                 # 推送玩家退出桌子
PUSH_USER_READY = 101106                # 推送玩家准备/取消准备
PUSH_USER_JOIN_DESK = 101107            # 推送玩家加入房间
PUSH_USER_SET_CONFIG = 101108           # 推送玩家更改了配置
PUSH_USER_RECONNECT = 101109            # 推送玩家断线重连
```

二、 错误编码定义
```
USER_ID_REQUIRED = 900
COMMAND_NOT_FOUND = 901
USER_NOT_FOUND_ON_DESK = 902
DESK_NOT_EXIST = 903
USER_IN_OTHER_DESK = 904
DESK_IS_FULL = 905
DESK_IS_PLAYING = 906
DESK_CONFIG_ERROR = 907

SESSION_NOT_EXIST = 997
REPEAT_REQUEST = 998
INVALID_REQUEST = 999

ERROR_CODE_DESC = {
    USER_ID_REQUIRED: u"缺少userid",
    COMMAND_NOT_FOUND: u"消息未注册",
    USER_NOT_FOUND_ON_DESK: u"桌子中没有该用户",
    DESK_NOT_EXIST: u"桌子不存在",
    USER_IN_OTHER_DESK: u"用户在其他桌子中",
    DESK_IS_FULL: u"桌子已满",
    DESK_IS_PLAYING: u"桌子处于游戏中",
    DESK_CONFIG_ERROR: u"桌子自定义配置错误",

    SESSION_NOT_EXIST: u"会话不存在",
    REPEAT_REQUEST: u"重复请求",
    INVALID_REQUEST: u"非法请求"
}
```

三、 请求接口定义
#####1. 登录(100002)
登录需要先请求web端，获取后续玩家进入的房间名称；
再向游戏服发送登录请求
请求参数如下：
```
{
"user_id": user_id,
"passwd": 32md5,
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"room":"",           # 之后进入的房间名
		"old_session": None/string,
	}
}
```
失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```

####2. 断线重连(100010)
请求参数如下：
{
}
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"user_info":{},           # 用户个人详细信息
		"game_data": {},		  # 当局游戏信息
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```

####3. 玩家准备(100162)
请求参数如下：
```
{
	"ready": 0/1,  # 0:取消准备, 1:准备
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```

####4. 创建好友房(101000)
请求参数如下：
```
{
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"desk_id": int,
		"seat_id": 0
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```

####5. 加入好友房(101001)
请求参数如下：
```
{
	"desk_id": int
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"desk_id": int,
		"seat_info": {}            # 当前游戏桌子座位信息
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```

####6. 解散房间(100151)
房间解散成功有独立的推送房间解散成功的消息
请求参数如下：
```
{
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"need_agree": 0/1,        # 0:解散桌子需要征求其他人同意， 1：不需要征求同意，直接退出
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```


####7. 解散房间应答(100156)
请求参数如下：
```
{
	"agree": 0/1,    # 是否同意解散房间  0: 拒绝, 1:同意
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```


####8. 请求退出桌子(100157)
请求参数如下：
```
{
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```


####9. 自定义配置(100158)
请求参数如下：
```
{
	"custom_config": {}       #自定义的配置
}
```
返回参数
成功时
```
{
	"code": 200,
	"info": {
		"config": {}          # 当前桌子配置
	}
}
```

失败时：
```
{
	"code": int,
	"desc": "错误内容"
}
```


###四、 推送接口定义
####1. 推送玩家叫牌(101001)
推送参数
```
{
	"seat_id": int,       # 玩家座位序号
	"act": [],            # 可进行的操作列表
	"card": int,          # 针对哪一张牌
	"is_against": 0/1,    # 该动作是否为针对特定牌
}
```

####2. 推送玩家摸牌(101002)
推送参数
```
{
	"seat_id": int,       # 玩家座位序号
	"card_list": [],      # 摸到的牌
}
```

####3. 推送游戏结束(101003)
推送参数
```
{
}
```
####4. 推送定庄信息(101004)
推送参数
```
{
	"bank_seat_id": int,       # 庄家座位序号
	"dice": [],      		   # 骰子值(一般是两个骰子)
}
```
####5. 推送发牌信息(101005)
推送参数
```
{
	"seat_id": int,       # 玩家座位序号
	"card_list": [],      # 摸到的牌
}
```
####6. 推送游戏结算(101006)
推送参数
```
{
	"total_points": [],	  # 当次结算输赢积分总情况
	"detail": [{}, ...]   # 结算详情
}
```

####7. 推送玩家点数发生变化(101100)
推送参数
```
{
	"user_id": int,    # 发生变化的玩家id
	"seat_id": int,    # 发生变化玩家座位序号
	"point": int,      # 玩家点数
}
```
####8. 推送玩家在其他地方登陆(101101)
推送参数
```
{
	"code": int,       # desk_id
	"desc": [],        # 详情
}
```
####9. 推送桌子解散结果(101102)
推送参数
```
{
	"user_id": int,       # 发出响应的玩家id
	"nick": string,       # 玩家昵称
	"agree": 0/1,         # 是否同意解散房间
	"success": 0/1,       # 解散房间失败/成功
}
```
####10. 推送有玩家请求解散桌子(101103)
推送参数
```
{
	"user_id": int,       # 请求解散的玩家id
	"nick": string,       # 玩家昵称
}
```
####11. 推送玩家对解散桌子的响应(101104)
推送参数
```
{
	"user_id": int,       # 发出响应的玩家id
	"nick": string,       # 玩家昵称
	"agree": 0/1,         # 是否同意解散房间
}
```
####12. 推送玩家退出桌子(101105)
推送参数
```
{
	"user_id": int,       # 发出响应的玩家id
	"nick": string,       # 玩家昵称
}
```
####13. 推送玩家准备/取消准备(101106)
推送参数
```
{
	"user_id": int,       # 发出响应的玩家id
	"nick": string,       # 玩家昵称
	"ready": 0/1,
}
```
####14. 推送玩家加入房间(101107)

####15. 推送玩家更改了配置(101108)
推送参数
```
{
	"user_id": int,       # 玩家id
	"nick": string,       # 玩家昵称
    "config": {}          # 桌子自定义配置
}
```
####16. 推送玩家断线重连(101109)
推送参数
```
{
	"user_id": self.user_id,
	"nick": self.nick_name,
}
```



