var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
var Tpm;
(function (Tpm) {
    var GameScene = (function (_super) {
        __extends(GameScene, _super);
        function GameScene() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameSceneSkin;
            return _this;
        }
        GameScene.prototype.childrenCreated = function () {
        };
        GameScene.prototype.onEnable = function () {
            this.ctrl.onRegister();
            this.initUI();
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouchTap, this);
            this.hallBackBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onExit, this);
            this.selectBtnMod.addEventListener("sendActEvent", this.onActBtnTouch, this);
            this.headDown.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
            this.headUp.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
        };
        GameScene.prototype.onRemove = function () {
            this.ctrl.onRemove();
            this.clearDesk();
        };
        /**初始化UI */
        GameScene.prototype.initUI = function (allFlag) {
            if (allFlag === void 0) { allFlag = true; }
            this.reResidue(false);
            this.diskMod.setState(Tpm.DiskState.normal);
            this.flowerMod.initUI();
            this.selectBtnMod.hide();
            this.matchMod.setType(Tpm.MatchType.common);
            this.tuoMod.setState(false);
            this.eatChooseMod.hideCombo();
            this.gangChooseMod.hideCombo();
            this.huTipsMod.hideTips();
            this.outShowMod.visible = true;
            this.tingDown.setState(Tpm.TingState.normal);
            this.tingUp.setState(Tpm.TingState.normal);
            if (allFlag) {
                this.reDeskDesc(Tpm.RoomType.noob);
                this.readyMod.setState(Tpm.ReadyState.normal);
            }
            if (Tpm.App.DataCenter.debugInfo.testState) {
                this.cheatMod.visible = true;
            }
        };
        /**清理牌局 */
        GameScene.prototype.clearDesk = function (initFlag) {
            if (initFlag === void 0) { initFlag = true; }
            this.cardMod.clearCardMovieGro();
            this.cardMod.clearAllCard();
            Tpm.App.DataCenter.runingData.clearData(initFlag);
            this.initUI(initFlag);
        };
        /**正常进入房间 */
        GameScene.prototype.intoRoom = function () {
            // 更新头像
            this.headDown.reHeadState(Tpm.UserPosition.Down);
            this.headUp.reHeadState(Tpm.UserPosition.Up);
            // 匹配模块显示
            if (Tpm.App.DataCenter.UserInfo.getUserNum() < 2) {
                this.matchMod.setType(Tpm.MatchType.match);
            }
            else {
                this.matchMod.setType(Tpm.MatchType.common);
            }
            // 发送准备
            if (Tpm.App.DataCenter.debugInfo.autoReady) {
                this.ctrl.sendMod.sendReady();
            }
            else {
                this.readyMod.visible = true;
                this.readyMod.setState(Tpm.ReadyState.ready_00);
            }
            this.reDeskDesc(Tpm.App.DataCenter.runingData.curentRoomType);
        };
        /**断线重连 */
        GameScene.prototype.reConnect = function (data) {
            console.log("scene reConnect");
            var revData = Tpm.ProtocolDataRev.R_100010;
            revData = data;
            // 游戏状态
            Tpm.App.DataCenter.runingData.gameState = Tpm.GameState.Playing;
            //用户信息
            var userInfo = revData.info.user_info;
            for (var i = 0; i < userInfo.length; i++) {
                if (userInfo[i].user_id == Tpm.App.DataCenter.UserInfo.myUserUid) {
                    Tpm.App.DataCenter.UserInfo.myUserInfo.seatID = userInfo[i].seat_id;
                    Tpm.App.DataCenter.UserInfo.myUserInfo.gold = userInfo[i].point;
                }
                else {
                    var user = new Tpm.UserVO();
                    user.initUserFromSocket(userInfo[i]);
                    Tpm.App.DataCenter.UserInfo.addUser(user);
                }
            }
            // 桌子信息
            var deskInfo = revData.info.game_data.desk_info;
            Tpm.App.DataCenter.runingData.curentRoomType = deskInfo.room_type;
            deskInfo.remain_count && this.reResidue(true, deskInfo.remain_count);
            this.reDeskDesc(Tpm.App.DataCenter.runingData.curentRoomType);
            var playerInfo = revData.info.game_data.player_info;
            // 头像信息、补花、听、过胡等
            this.headDown.reHeadState(Tpm.UserPosition.Down);
            this.headUp.reHeadState(Tpm.UserPosition.Up);
            var seatDown = Tpm.App.DataCenter.UserInfo.getSeatFromPos(Tpm.UserPosition.Down);
            var seatUp = Tpm.App.DataCenter.UserInfo.getSeatFromPos(Tpm.UserPosition.Up);
            this.flowerMod.setFlowerState(Tpm.UserPosition.Down, playerInfo[seatDown].bu_hua_num);
            this.flowerMod.setFlowerState(Tpm.UserPosition.Up, playerInfo[seatUp].bu_hua_num);
            this.setTingState(playerInfo);
            // 风盘相关
            var endTime = Math.floor(revData.info.game_data.wait_task.end_time);
            var diskInfo = revData.info.game_data.player_info;
            if (diskInfo[seatDown].hand_card_by_order[diskInfo[seatDown].hand_card_by_order.length - 2].length % 3 == 2) {
                this.diskMod.setState(Tpm.DiskState.down, endTime);
                Tpm.App.DataCenter.runingData.bAllowOutCard = true;
            }
            else if (diskInfo[seatUp].hand_card_by_order[diskInfo[seatUp].hand_card_by_order.length - 2].length % 3 == 2) {
                this.diskMod.setState(Tpm.DiskState.up, endTime || Tpm.App.DataCenter.roomInfo.getConfigForType(Tpm.App.DataCenter.runingData.curentRoomType).outCardTime);
            }
            else {
                this.diskMod.setState(Tpm.DiskState.up, endTime || Tpm.App.DataCenter.roomInfo.getConfigForType(Tpm.App.DataCenter.runingData.curentRoomType).outCardTime);
            }
            // 牌相关
            this.cardMod.reConnectCardShow(Tpm.UserPosition.Down, revData.info.game_data.player_info[seatDown].hand_card_by_order, revData.info.game_data.player_info[seatDown].last_card, revData.info.game_data.player_info[seatDown].out_card);
            this.cardMod.reConnectCardShow(Tpm.UserPosition.Up, revData.info.game_data.player_info[seatUp].hand_card_by_order, revData.info.game_data.player_info[seatUp].last_card, revData.info.game_data.player_info[seatUp].out_card);
            // 动作相关
            if (revData.info.game_data.wait_task.params) {
                var actInfo = revData.info.game_data.wait_task.params;
                var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(actInfo.seat_id);
                var state = pos ? Tpm.DiskState.up : Tpm.DiskState.down;
                this.diskMod.setState(state, endTime);
                if (actInfo.seat_id == Tpm.App.DataCenter.UserInfo.myUserInfo.seatID) {
                    console.log("动作操作数据：", actInfo);
                    Tpm.App.DataCenter.MsgCache.addMsgData(Tpm.ProtocolHeadRev.R_101001, actInfo);
                    var actList = Tpm.CardLogic.getInstance().getActListFromKey(actInfo.act_info);
                    this.selectBtnMod.showActBtn(actList);
                }
            }
        };
        /**重连时设置听牌、过胡状态 */
        GameScene.prototype.setTingState = function (playerInfo) {
            var seatDown = Tpm.App.DataCenter.UserInfo.getSeatFromPos(Tpm.UserPosition.Down);
            var seatUp = Tpm.App.DataCenter.UserInfo.getSeatFromPos(Tpm.UserPosition.Up);
            var tingStateDown = Tpm.TingState.normal;
            if (playerInfo[seatDown].is_ting) {
                Tpm.App.DataCenter.runingData.ownTingState = true;
                if (playerInfo[seatDown].guo_hu_num > 0) {
                    tingStateDown = Tpm.TingState.guo;
                }
                else {
                    tingStateDown = Tpm.TingState.ting;
                }
            }
            if (tingStateDown != Tpm.TingState.normal) {
                Tpm.App.DataCenter.runingData.ownTingState = true;
            }
            this.tingDown.setState(tingStateDown, playerInfo[seatDown].guo_hu_num);
            Tpm.App.DataCenter.runingData.ownGuoTimes = playerInfo[seatDown].guo_hu_num;
            var tingStateUp = Tpm.TingState.normal;
            if (playerInfo[seatUp].is_ting) {
                if (playerInfo[seatUp].guo_hu_num > 0) {
                    tingStateUp = Tpm.TingState.guo;
                }
                else {
                    tingStateUp = Tpm.TingState.ting;
                }
            }
            this.tingUp.setState(tingStateUp, playerInfo[seatUp].guo_hu_num);
        };
        /**更新牌桌描述信息 */
        GameScene.prototype.reDeskDesc = function (roomType) {
            var roomInfo = Tpm.App.DataCenter.roomInfo.getConfigForType(roomType);
            if (!roomInfo) {
                console.error("roomInfo error");
                return;
            }
            this.descLab.text = roomInfo.roomName + " " + roomInfo.minHuFan + "番起胡 底分" + roomInfo.baseBet;
        };
        /**更新剩余牌数 */
        GameScene.prototype.reResidue = function (show, num) {
            if (num === void 0) { num = 0; }
            this.residueGro.visible = show;
            this.residueLab.text = num.toString();
        };
        /**退出响应 */
        GameScene.prototype.onExit = function () {
            this.ctrl.sendMod.sendExitRoom();
        };
        /**头像响应 */
        GameScene.prototype.onHead = function (e) {
            var tUid = 0;
            if (e.target == this.headDown) {
                tUid = Tpm.App.DataCenter.UserInfo.myUserUid;
            }
            else if (e.target == this.headUp) {
                tUid = Tpm.App.DataCenter.UserInfo.getUserByPos(Tpm.UserPosition.Up).userID;
            }
            this.ctrl.sendHeadInfo(tUid);
        };
        /**Scene点击响应 */
        GameScene.prototype.onTouchTap = function (e) {
            // 按钮测试 
            // this.selectBtnMod.showActBtn([0,20,30,40,70,80,104]);
            // 结算界面测试
            // App.PanelManager.open(PanelConst.ResultPanel);
            // 吃牌选择测试
            // this.eatChooseMod.showCombo([[17,18,19],[17,18,19]]);
            // 杠牌选择测试
            // this.gangChooseMod.showCombo([[17,17,17,17], [18,18,18,18], [19,19,19,19]]);
        };
        /**动作按钮操作响应 */
        GameScene.prototype.onActBtnTouch = function (e) {
            var _this = this;
            this.selectBtnMod.hide();
            var act = e.data;
            console.log("按钮动作==", act);
            var cardList = null;
            switch (act) {
                case Tpm.ACT_state.Act_Chi:
                    var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
                    if (data.act_info[Tpm.ACT_state.Act_Chi].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[Tpm.ACT_state.Act_Chi][0]);
                    }
                    else if (data.act_info[Tpm.ACT_state.Act_Chi].length > 1) {
                        this.eatChooseMod.showCombo(data.act_info[Tpm.ACT_state.Act_Chi]);
                        this.eatChooseMod.addEventListener("selectComboEvent", function (Evdata) {
                            console.log("choosedEatList==", Evdata.data);
                            _this.ctrl.sendMod.sendAct(act, Evdata.data);
                        }, this);
                    }
                    else {
                        console.error("eat combo error");
                    }
                    break;
                case Tpm.ACT_state.Act_AnGang:
                    var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
                    if (data.act_info[Tpm.ACT_state.Act_AnGang].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[Tpm.ACT_state.Act_AnGang][0]);
                    }
                    else if (data.act_info[Tpm.ACT_state.Act_AnGang].length > 1) {
                        var gangList = [];
                        for (var i = 0; i < data.act_info[Tpm.ACT_state.Act_AnGang].length; i++) {
                            var list = [];
                            list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                            gangList.push(list);
                        }
                        this.gangChooseMod.showCombo(gangList);
                        this.gangChooseMod.addEventListener("selectComboEvent", function (Evdata) {
                            console.log("choosedAGangList==", Evdata.data);
                            _this.ctrl.sendMod.sendAct(act, Evdata.data[0]);
                        }, this);
                    }
                    else {
                        console.error("angang combo error");
                    }
                    break;
                case Tpm.ACT_state.Act_BuGang:
                    var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
                    if (data.act_info[Tpm.ACT_state.Act_BuGang].length == 1) {
                        this.ctrl.sendMod.sendAct(act, data.act_info[Tpm.ACT_state.Act_BuGang][0]);
                    }
                    else if (data.act_info[Tpm.ACT_state.Act_BuGang].length > 1) {
                        var gangList = [];
                        for (var i = 0; i < data.act_info[Tpm.ACT_state.Act_BuGang].length; i++) {
                            var list = [];
                            list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                            list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                            gangList.push(list);
                        }
                        this.gangChooseMod.showCombo(gangList);
                        this.gangChooseMod.addEventListener("selectComboEvent", function (Evdata) {
                            console.log("choosedBGangList==", Evdata.data);
                            _this.ctrl.sendMod.sendAct(act, Evdata.data[0]);
                        }, this);
                    }
                    else {
                        console.error("bugang combo error");
                    }
                    break;
                case Tpm.ACT_state.Act_ZuheGang:
                    var data = Tpm.App.DataCenter.MsgCache.getMsgData(Tpm.ProtocolHeadRev.R_101001, false);
                    var gangList = [];
                    for (var i = 0; i < data.act_info[Tpm.ACT_state.Act_AnGang].length; i++) {
                        var list = [];
                        list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_AnGang][i]);
                        gangList.push(list);
                    }
                    for (var i = 0; i < data.act_info[Tpm.ACT_state.Act_BuGang].length; i++) {
                        var list = [];
                        list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                        list.push(data.act_info[Tpm.ACT_state.Act_BuGang][i]);
                        gangList.push(list);
                    }
                    this.gangChooseMod.showCombo(gangList);
                    this.gangChooseMod.addEventListener("selectComboEvent", function (Evdata) {
                        console.log("choosedZuheGangList==", Evdata.data);
                        if (Evdata.data[0] == data.act_info[Tpm.ACT_state.Act_BuGang][0][0]) {
                            _this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_BuGang, Evdata.data[0]);
                        }
                        else {
                            _this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_AnGang, Evdata.data[0]);
                        }
                    }, this);
                    break;
                case Tpm.ACT_state.Act_Ting:
                    Tpm.App.DataCenter.runingData.bAllowOutCard = true;
                    this.huTipsMod.showCancle();
                    this.cardMod.tingCardShow();
                    break;
                case Tpm.ACT_state.Act_Guohu:
                    this.ctrl.sendMod.sendAct(Tpm.ACT_state.Act_Pass);
                    break;
                default:
                    this.ctrl.sendMod.sendAct(act);
                    break;
            }
        };
        /**收到某些动作后允许出牌判断 */
        GameScene.prototype.allowOutCardJudge = function (act, pos) {
            if (pos != Tpm.UserPosition.Down) {
                return;
            }
            var list = [Tpm.ACT_state.Act_Chi, Tpm.ACT_state.Act_Peng, Tpm.ACT_state.Act_Gang, Tpm.ACT_state.Act_AnGang, Tpm.ACT_state.Act_BuGang];
            if (list.indexOf(act) >= 0) {
                Tpm.App.DataCenter.runingData.bAllowOutCard = true;
            }
        };
        /**动作推送响应 */
        GameScene.prototype.onActDo = function (doAct, pos, doCardvalueList, handList) {
            console.log("处理动作：", doAct);
            if (doAct == Tpm.ACT_state.Act_Out) {
                this.outShowMod.showOutCard(doCardvalueList[0], pos);
            }
            else {
                this.dbMod.showActDb(doAct, pos);
            }
            this.allowOutCardJudge(doAct, pos);
            switch (doAct) {
                case Tpm.ACT_state.Act_Pass:
                    break;
                case Tpm.ACT_state.Act_Out:
                    if (pos == Tpm.UserPosition.Down) {
                        Tpm.App.DataCenter.runingData.bAllowOutCard = false;
                    }
                    // 更新圆盘
                    var state = pos ? Tpm.DiskState.down : Tpm.DiskState.up;
                    this.diskMod.setState(state, Tpm.App.DataCenter.roomInfo.getConfigForType(Tpm.App.DataCenter.runingData.curentRoomType).outCardTime);
                    console.log("out card===", doCardvalueList[0]);
                    this.cardMod.outCardShow(pos, doCardvalueList[0]);
                    break;
                case Tpm.ACT_state.Act_Chi:
                    this.cardMod.eatCardShow(doCardvalueList, pos);
                    break;
                case Tpm.ACT_state.Act_Peng:
                    doCardvalueList.push(doCardvalueList[0]);
                    doCardvalueList.push(doCardvalueList[0]);
                    this.cardMod.eatCardShow(doCardvalueList, pos, true);
                    break;
                case Tpm.ACT_state.Act_AnGang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case Tpm.ACT_state.Act_BuGang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case Tpm.ACT_state.Act_Gang:
                    this.cardMod.gangCardShow(doAct, doCardvalueList[0], pos);
                    break;
                case Tpm.ACT_state.Act_Ting:
                    if (pos == Tpm.UserPosition.Down) {
                        Tpm.App.DataCenter.runingData.ownTingState = true;
                        this.huTipsMod.hideTips();
                        this.cardMod.tingDidShow(handList);
                        this.tingDown.setState(Tpm.TingState.ting);
                    }
                    else {
                        this.tingUp.setState(Tpm.TingState.ting);
                    }
                    break;
                case Tpm.ACT_state.Act_DianHu:
                    this.selectBtnMod.hide();
                    this.cardMod.dianHuCardShow(doCardvalueList[0], pos);
                    break;
                case Tpm.ACT_state.Act_Guohu:
                    this.selectBtnMod.hide();
                    if (pos == Tpm.UserPosition.Down) {
                        this.tingDown.setState(Tpm.TingState.guo, 1, true);
                        Tpm.App.DataCenter.runingData.ownGuoTimes++;
                    }
                    else {
                        this.tingUp.setState(Tpm.TingState.guo, 1, true);
                    }
                    break;
                default:
                    break;
            }
        };
        return GameScene;
    }(Tpm.BaseScene));
    Tpm.GameScene = GameScene;
    __reflect(GameScene.prototype, "Tpm.GameScene");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameScene.js.map