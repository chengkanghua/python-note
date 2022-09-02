1. gate节点流程
start_up.py -- > controller.py  
forwarding_game ->

GlobalObject().root.callChildByName    @RemoteServiceHandle 配套使用
gate节点转发game|room节点的策略:
优先转发之前一样的room节点
如果第一次进入,则随机选择,需要考哪些节点可用 (策略参考proxy选择gate节点)

echecs/db  数据操作模块


gate 里面
根据消息id, login请求会调用web server求的结果, 登录成功后踢掉之前登录的设备

消息推送
gate/controller.py rpc 调用proxy下的push_object方法   remoteserver.py


2. game节点|room 节点
controller.py  --> forwarding_game    (所有的gate节点消息都会过来)

events  --> game/room/handlers/basehandler.py(RegisterEvent(object))

RegisterEvent  --> 类注册 , 事件注册|消息注册
返回的时是一个延迟对象(defer)


--- 项目理解的第一大步: 走完整个消息的处理流程(proxy入口 ---...--- game返回(出口))

3. 选择一个具体的消息进行跟踪, 选择快速加入房间    -- 理解项目代码的第二大步
比如选择快速加入匹配场
快速定位的方式:
消息定义的常量全局搜索  JoinMatchDeskHandler(game/room/handlers/match_desk/join_desk.py)  

介绍项目每层目录是干啥:
game:
	mahjong: 麻将游戏内部的所有逻辑
		constants/      游戏内部的常量定义
		controls/     游戏内部控制模块
		models/      模型定义

	room: 房间和桌子的逻辑
		handlers/    房间消息的实际处理
		models 模型定义
		validators/   参数验证器 (wtforms模块对参数进行校验)   

		common_define.py  常量定义
		notifybridge.py  所有房间需要通知游戏内部的消息接口封装到此处, 文件内部在调用bridgecontroller


	bridgecontroller.py   桥接器(房间和游戏内部双向交互)
	controller.py 节点消息处理
	push_service.py 推送接口相关
	session_gate_rel.py   会话和gate关系相关
	start_up.py 启动相关

 
面试时加班相关问题回答:
最初几年, 加班很多, 年轻人就应该多做事
17年初  业余生活没有安排的时候加加班
19年初 没有工作和生活的区别

