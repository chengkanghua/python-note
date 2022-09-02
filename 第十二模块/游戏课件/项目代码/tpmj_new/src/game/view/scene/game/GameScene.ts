module Tpm {
    export class GameScene extends BaseScene {
        /**游戏场景控制类*/
        protected ctrl: GameController;

        private residueGro: eui.Group; 
        private residueLab: eui.Label;
        private descLab: eui.Label;
        private headGro: eui.Group;
        private btnGro: eui.Group;
        private hallBackBtn: eui.Button;

        /**本家头像模块 */
        public headDown: Tpm.GameHeadMod;
        /**对家头像模块 */
        public headUp: Tpm.GameHeadMod;
        /**补花模块 */
        public flowerMod:Tpm.GameFlowerMod;
        /**本家听牌过胡模块 */
        public tingDown: Tpm.GameTingMod;
        /**对家听牌过胡模块 */
        public tingUp: Tpm.GameTingMod;
        /**风盘模块 */
        public diskMod: Tpm.GameDiskMod;
        /**牌相关模块 */
        public cardMod: Tpm.GameCardMod;
        /**动作按钮模块 */
        public selectBtnMod: Tpm.GameSelectBtnMod;
        /**动作特效模块 */
        public dbMod: Tpm.GameDbMod;
        /**匹配模块 */
        public matchMod: Tpm.GameMatchMod;
        /**准备模块 */
        public readyMod: Tpm.GameReadyMod;
        /**菜单模块 */
        public MenuMod: Tpm.GameMenuMod;
        /**托管模块 */
        public tuoMod: Tpm.GameTuogMod;
        /**吃牌选择模块 */
        public eatChooseMod: Tpm.GameEatChooseMod;
        /**杠牌选择模块 */
        public gangChooseMod:Tpm.GameGangChooseMod;
        /**出牌显示模块 */
        public outShowMod: Tpm.GameOutShowMod;
        /**胡牌提示模块 */
        public huTipsMod:Tpm.GameHuTipsMod;
        /**作弊模块 */
        public cheatMod:Tpm.GameCheatMod;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameSceneSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {
            this.ctrl.onRegister();
            this.initUI();

            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouchTap, this);
            this.hallBackBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onExit, this);
            this.selectBtnMod.addEventListener("sendActEvent", this.onActBtnTouch, this);
            this.headDown.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
            this.headUp.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
        }

        protected onRemove() {
            this.ctrl.onRemove();
            this.clearDesk();
        }

        /**初始化UI */
        private initUI(allFlag: boolean = true) {
            this.reResidue(false);
            this.diskMod.setState(DiskState.normal);
            this.flowerMod.initUI();
            this.selectBtnMod.hide();
            this.matchMod.setType(MatchType.common);
            this.tuoMod.setState(false);
            this.eatChooseMod.hideCombo();
            this.gangChooseMod.hideCombo();
            this.huTipsMod.hideTips();
            this.outShowMod.visible = true;
            this.tingDown.setState(TingState.normal);
            this.tingUp.setState(TingState.normal);

            if (allFlag) {
                this.reDeskDesc(RoomType.noob);
                this.readyMod.setState(ReadyState.normal);
            }
            
            if (App.DataCenter.debugInfo.testState) {
                this.cheatMod.visible = true;
            }
        }

        /**清理牌局 */
        public clearDesk(initFlag: boolean = true) {
            this.cardMod.clearCardMovieGro();
            this.cardMod.clearAllCard();
            App.DataCenter.runingData.clearData(initFlag);

            this.initUI(initFlag);
        }

        /**正常进入房间 */
        public intoRoom() {
            // 更新头像
            this.headDown.reHeadState(UserPosition.Down);
            this.headUp.reHeadState(UserPosition.Up);

            // 匹配模块显示
            if (App.DataCenter.UserInfo.getUserNum() < 2) {
                this.matchMod.setType(MatchType.match);
            }
            else {
                this.matchMod.setType(MatchType.common);
            }

            // 发送准备
            if (App.DataCenter.debugInfo.autoReady) {
                this.ctrl.sendMod.sendReady();
            }
            else {
                this.readyMod.visible = true;
                this.readyMod.setState(ReadyState.ready_00);
            }

            this.reDeskDesc(App.DataCenter.runingData.curentRoomType);
        }

        /**断线重连 */
        public reConnect(data: any) {
            console.log("scene reConnect");
            var revData = ProtocolDataRev.R_100010;
            revData = data;
            // 游戏状态
            App.DataCenter.runingData.gameState = GameState.Playing;

            //用户信息
            var userInfo = revData.info.user_info;
            for(var i = 0;i < userInfo.length;i ++) {
                if(userInfo[i].user_id == App.DataCenter.UserInfo.myUserUid) {
                    App.DataCenter.UserInfo.myUserInfo.seatID = userInfo[i].seat_id;
                    App.DataCenter.UserInfo.myUserInfo.gold = userInfo[i].point;
                }
                else {
                    var user = new UserVO();
                    user.initUserFromSocket(userInfo[i]);
                    App.DataCenter.UserInfo.addUser(user);
                }
            }

            // 桌子信息
            var deskInfo = revData.info.game_data.desk_info;
            App.DataCenter.runingData.curentRoomType = deskInfo.room_type;
            deskInfo.remain_count && this.reResidue(true, deskInfo.remain_count);
            this.reDeskDesc(App.DataCenter.runingData.curentRoomType);

            var playerInfo = revData.info.game_data.player_info;
            // 头像信息、补花、听、过胡等
            this.headDown.reHeadState(UserPosition.Down);
            this.headUp.reHeadState(UserPosition.Up);
            
            var seatDown = App.DataCenter.UserInfo.getSeatFromPos(UserPosition.Down);
            var seatUp = App.DataCenter.UserInfo.getSeatFromPos(UserPosition.Up);
            this.flowerMod.setFlowerState(UserPosition.Down, playerInfo[seatDown].bu_hua_num);
            this.flowerMod.setFlowerState(UserPosition.Up, playerInfo[seatUp].bu_hua_num);

            this.setTingState(playerInfo);

            // 风盘相关
            var endTime = Math.floor(revData.info.game_data.wait_task.end_time);
            var diskInfo = revData.info.game_data.player_info;
            if (diskInfo[seatDown].hand_card_by_order[diskInfo[seatDown].hand_card_by_order.length-2].length%3 == 2) {
                this.diskMod.setState(DiskState.down, endTime);
                App.DataCenter.runingData.bAllowOutCard = true;
            }
            else if (diskInfo[seatUp].hand_card_by_order[diskInfo[seatUp].hand_card_by_order.length-2].length%3 == 2) {
                this.diskMod.setState(DiskState.up, endTime || App.DataCenter.roomInfo.getConfigForType(App.DataCenter.runingData.curentRoomType).outCardTime);
            }
            else {
                this.diskMod.setState(DiskState.up, endTime || App.DataCenter.roomInfo.getConfigForType(App.DataCenter.runingData.curentRoomType).outCardTime);
            }

            // 牌相关
            this.cardMod.reConnectCardShow(UserPosition.Down, revData.info.game_data.player_info[seatDown].hand_card_by_order, revData.info.game_data.player_info[seatDown].last_card, revData.info.game_data.player_info[seatDown].out_card);
            this.cardMod.reConnectCardShow(UserPosition.Up, revData.info.game_data.player_info[seatUp].hand_card_by_order, revData.info.game_data.player_info[seatUp].last_card, revData.info.game_data.player_info[seatUp].out_card);

            // 动作相关
            if (revData.info.game_data.wait_task.params) {
                var actInfo = revData.info.game_data.wait_task.params;
                var pos = App.DataCenter.UserInfo.getPosFromSeat(actInfo.seat_id);
                var state = pos ? DiskState.up : DiskState.down;
                this.diskMod.setState(state,endTime);
                if (actInfo.seat_id == App.DataCenter.UserInfo.myUserInfo.seatID) {
                    console.log("动作操作数据：", actInfo);
                    App.DataCenter.MsgCache.addMsgData(ProtocolHeadRev.R_101001, actInfo);
                    var actList = CardLogic.getInstance().getActListFromKey(actInfo.act_info);
                    this.selectBtnMod.showActBtn(actList);
                }
            }
        }

        /**重连时设置听牌、过胡状态 */
        private setTingState(playerInfo: any) {
            var seatDown = App.DataCenter.UserInfo.getSeatFromPos(UserPosition.Down);
            var seatUp = App.DataCenter.UserInfo.getSeatFromPos(UserPosition.Up);
            var tingStateDown = TingState.normal;
            if (playerInfo[seatDown].is_ting) {
                App.DataCenter.runingData.ownTingState = true;

                if (playerInfo[seatDown].guo_hu_num > 0) {
                    tingStateDown = TingState.guo;
                }
                else {
                    tingStateDown = TingState.ting;
                }
                
            }
            if (tingStateDown != TingState.normal) {
                App.DataCenter.runingData.ownTingState = true;
            }
            this.tingDown.setState(tingStateDown, playerInfo[seatDown].guo_hu_num);
            App.DataCenter.runingData.ownGuoTimes = playerInfo[seatDown].guo_hu_num;

            var tingStateUp = TingState.normal;
            if (playerInfo[seatUp].is_ting) {
                if (playerInfo[seatUp].guo_hu_num > 0) {
                    tingStateUp = TingState.guo;
                }
                else {
                    tingStateUp = TingState.ting;
                }
                
            }
            this.tingUp.setState(tingStateUp, playerInfo[seatUp].guo_hu_num);
        }


        /**更新牌桌描述信息 */
        public reDeskDesc(roomType: RoomType) {
            var roomInfo = App.DataCenter.roomInfo.getConfigForType(roomType);
            if (!roomInfo) {
                console.error("roomInfo error");
                return;
            }
            this.descLab.text = roomInfo.roomName + " " + roomInfo.minHuFan + "番起胡 底分" + roomInfo.baseBet;  
        }

        /**更新剩余牌数 */
        public reResidue(show: boolean, num: number = 0) {
            this.residueGro.visible = show;
            this.residueLab.text = num.toString();
        }

        /**退出响应 */
        private onExit() {
            this.ctrl.sendMod.sendExitRoom();
        }

        /**头像响应 */
        private onHead(e: egret.Event) {
            var tUid = 0;
            if (e.target == this.headDown) {
                tUid = App.DataCenter.UserInfo.myUserUid;
            }
            else if (e.target == this.headUp) {
                tUid = App.DataCenter.UserInfo.getUserByPos(UserPosition.Up).userID;
            }
            this.ctrl.sendHeadInfo(tUid);
        }

        /**Scene点击响应 */
        private onTouchTap(e: egret.TouchEvent) {
            // 按钮测试 
            // this.selectBtnMod.showActBtn([0,20,30,40,70,80,104]);

            // 结算界面测试
            // App.PanelManager.open(PanelConst.ResultPanel);

            // 吃牌选择测试
            // this.eatChooseMod.showCombo([[17,18,19],[17,18,19]]);

            // 杠牌选择测试
            // this.gangChooseMod.showCombo([[17,17,17,17], [18,18,18,18], [19,19,19,19]]);
        }

        /**动作按钮操作响应 */
        private onActBtnTouch(e: egret.TouchEvent) {
            this.selectBtnMod.hide();

            var act:ACT_state = e.data;
            console.log("按钮动作==", act);
            var cardList = null;

            switch (act) {
                case ACT_state.Act_Chi:
                    var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
                    if (data.act_info[ACT_state.Act_Chi].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[ACT_state.Act_Chi][0]);
                    }
                    else if (data.act_info[ACT_state.Act_Chi].length > 1) {
                        this.eatChooseMod.showCombo(data.act_info[ACT_state.Act_Chi]);
                        this.eatChooseMod.addEventListener("selectComboEvent", (Evdata)=>{
                            console.log("choosedEatList==", Evdata.data);
                            this.ctrl.sendMod.sendAct(act, Evdata.data);
                        }, this);
                    }
                    else {
                        console.error("eat combo error");
                    }
                    break;
                case ACT_state.Act_AnGang:
                    var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
                    if (data.act_info[ACT_state.Act_AnGang].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[ACT_state.Act_AnGang][0]);
                    }
                    else if (data.act_info[ACT_state.Act_AnGang].length > 1) {
                        var gangList = [];
                        for (var i = 0;i < data.act_info[ACT_state.Act_AnGang].length;i ++) {
                            var list = [];
                            list.push(data.act_info[ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[ACT_state.Act_AnGang][i]);
                            gangList.push(list);
                        }
                        this.gangChooseMod.showCombo(gangList);
                        this.gangChooseMod.addEventListener("selectComboEvent", (Evdata)=>{
                            console.log("choosedAGangList==", Evdata.data);
                            this.ctrl.sendMod.sendAct(act, Evdata.data[0]);
                        }, this);
                    }
                    else {
                        console.error("angang combo error");
                    }
                    break;
                case ACT_state.Act_BuGang:
                    var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
                    if (data.act_info[ACT_state.Act_BuGang].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[ACT_state.Act_BuGang][0]);
                    }
                    else if (data.act_info[ACT_state.Act_BuGang].length > 1) {
                        var gangList = [];
                        for (var i = 0;i < data.act_info[ACT_state.Act_BuGang].length;i ++) {
                            var list = [];
                            list.push(data.act_info[ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[ACT_state.Act_BuGang][i]);
                            gangList.push(list);
                        }
                        this.gangChooseMod.showCombo(gangList);
                        this.gangChooseMod.addEventListener("selectComboEvent", (Evdata)=>{
                            console.log("choosedBGangList==", Evdata.data);
                            this.ctrl.sendMod.sendAct(act, Evdata.data[0]);
                        }, this);
                    }
                    else {
                        console.error("bugang combo error");
                    }
                    break;
                case ACT_state.Act_ZuheGang:
                    var data = App.DataCenter.MsgCache.getMsgData(ProtocolHeadRev.R_101001, false);
                    var gangList = [];
                    for (var i = 0;i < data.act_info[ACT_state.Act_AnGang].length;i ++) {
                        var list = [];
                        list.push(data.act_info[ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[ACT_state.Act_AnGang][i]);
                        gangList.push(list);
                    }
                    for (var i = 0;i < data.act_info[ACT_state.Act_BuGang].length;i ++) {
                        var list = [];
                        list.push(data.act_info[ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[ACT_state.Act_BuGang][i]);
                        gangList.push(list);
                    }
                    this.gangChooseMod.showCombo(gangList);
                    this.gangChooseMod.addEventListener("selectComboEvent", (Evdata)=>{
                        console.log("choosedZuheGangList==", Evdata.data);
                        if (Evdata.data[0] == data.act_info[ACT_state.Act_BuGang][0][0]) {
                            this.ctrl.sendMod.sendAct(ACT_state.Act_BuGang, Evdata.data[0]);
                        }
                        else {
                            this.ctrl.sendMod.sendAct(ACT_state.Act_AnGang, Evdata.data[0]);
                        }
                    }, this);
                    break;
                case ACT_state.Act_Ting:
                    App.DataCenter.runingData.bAllowOutCard = true;
                    this.huTipsMod.showCancle();
                    this.cardMod.tingCardShow();
                    break;
                case ACT_state.Act_Guohu:
                    this.ctrl.sendMod.sendAct(ACT_state.Act_Pass);
                    break;
                default:
                    this.ctrl.sendMod.sendAct(act);
                    break;
            }
        }

        /**收到某些动作后允许出牌判断 */
        private allowOutCardJudge(act: ACT_state, pos) {
            if (pos != UserPosition.Down) {
                return;
            }

            var list: Array<ACT_state> = [ACT_state.Act_Chi, ACT_state.Act_Peng, ACT_state.Act_Gang, ACT_state.Act_AnGang, ACT_state.Act_BuGang];
            if (list.indexOf(act) >= 0) {
                App.DataCenter.runingData.bAllowOutCard = true;
            }
        }

        /**动作推送响应 */
        public onActDo(doAct: ACT_state, pos: UserPosition, doCardvalueList: Array<number>, handList: any) {
            console.log("处理动作：", doAct);
            if (doAct == ACT_state.Act_Out) {
                this.outShowMod.showOutCard(doCardvalueList[0], pos);
            }
            else {
                this.dbMod.showActDb(doAct, pos);
            }

            this.allowOutCardJudge(doAct, pos);

            switch (doAct) {
                case ACT_state.Act_Pass:
                    break;
                case ACT_state.Act_Out:
                    if (pos == UserPosition.Down) {
                        App.DataCenter.runingData.bAllowOutCard = false;
                    }
                    // 更新圆盘
                    var state = pos ? DiskState.down : DiskState.up;
                    this.diskMod.setState(state, App.DataCenter.roomInfo.getConfigForType(App.DataCenter.runingData.curentRoomType).outCardTime);

                    console.log("out card===", doCardvalueList[0]);
                    this.cardMod.outCardShow(pos, doCardvalueList[0]);
                    break;
                case ACT_state.Act_Chi:
                    this.cardMod.eatCardShow(doCardvalueList, pos);
                    break;
                case ACT_state.Act_Peng:
                    doCardvalueList.push(doCardvalueList[0]);
                    doCardvalueList.push(doCardvalueList[0]);
                    this.cardMod.eatCardShow(doCardvalueList, pos, true);
                    break;
                case ACT_state.Act_AnGang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case ACT_state.Act_BuGang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case ACT_state.Act_Gang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case ACT_state.Act_Ting:
                    if (pos == UserPosition.Down) {
                        App.DataCenter.runingData.ownTingState = true;
                        this.huTipsMod.hideTips();
                        this.cardMod.tingDidShow(handList);
                        this.tingDown.setState(TingState.ting);
                    }
                    else {
                        this.tingUp.setState(TingState.ting);
                    }
                    break;
                case ACT_state.Act_DianHu:
                    this.selectBtnMod.hide();
                    this.cardMod.dianHuCardShow(doCardvalueList[0], pos);
                    break;
                case ACT_state.Act_Guohu:
                    this.selectBtnMod.hide();
                    if (pos == UserPosition.Down) {
                        this.tingDown.setState(TingState.guo, 1, true);
                        App.DataCenter.runingData.ownGuoTimes ++;
                    }
                    else {
                        this.tingUp.setState(TingState.guo, 1, true);
                    }
                    break;
                default:
                    break;
            }
        }
    }
}