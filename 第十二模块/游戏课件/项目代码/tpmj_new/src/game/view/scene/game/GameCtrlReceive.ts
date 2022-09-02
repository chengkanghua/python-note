module Tpm {
    /**
     * 消息接收、处理模块
     */
    export class GameCtrlReceive {
        private gameCtrl: GameController;

        public constructor(ctrl:GameController) {
            this.gameCtrl = ctrl;
        }

        /**对应的scene */
        private get gameScene():GameScene {
            return this.gameCtrl.gameScene;
        }

        /**对应场景添加到显示列表时调用 */
        public onRegister() {
            var gameSocket: ClientSocket = App.gameSocket;
            gameSocket.register(ProtocolHeadRev.R_100100, this.revReady, this);
            gameSocket.register(ProtocolHeadRev.R_100103, this.revExit, this);
            gameSocket.register(ProtocolHeadRev.R_101001, this.revAct, this);
            gameSocket.register(ProtocolHeadRev.R_101004, this.revDingZhuang, this);
            gameSocket.register(ProtocolHeadRev.R_101105, this.revElseExit, this);
            gameSocket.register(ProtocolHeadRev.R_101107, this.revUserInto, this);
            gameSocket.register(ProtocolHeadRev.R_101109, this.revUserReconnect, this);
            gameSocket.register(ProtocolHeadRev.R_101110, this.revUserConnectState, this);
            gameSocket.register(ProtocolHeadRev.R_101005, this.revDealCard, this);
            gameSocket.register(ProtocolHeadRev.R_101008, this.revDealHua, this);
            gameSocket.register(ProtocolHeadRev.R_101002, this.revMoCard, this);
            gameSocket.register(ProtocolHeadRev.R_101112, this.revActDo, this);
            gameSocket.register(ProtocolHeadRev.R_101007, this.revMoHua, this);
            gameSocket.register(ProtocolHeadRev.R_100999, this.revCheat, this);
            gameSocket.register(ProtocolHeadRev.R_101003, this.revOver, this);
            gameSocket.register(ProtocolHeadRev.R_101006, this.revResult, this);
        }
        
        /**对应场景从显示列表移除是调用 */
        public onRemove() {
            
        }

        /**自己准备 */
        private revReady(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_100100.info;
            revData = data.info;

            App.DataCenter.runingData.gameState = GameState.Ready;
            this.gameScene.readyMod.hideBeginBtn();
        }

        /**退出房间 */
        private revExit(data) {
            if (data.code != 200) {
                // Tips.showTop(data.desc);
                Tips.showTop("游戏已经开始，无法退出。");
                return;
            }

            App.DataCenter.UserInfo.deleteAllUserExcptMe();
            App.DataCenter.UserInfo.clearZhuang();
            App.SceneManager.runScene(SceneConst.HallScene, App.getController(HallController.NAME));
        }

        /**其他玩家退出 */
        private revElseExit(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }

            App.DataCenter.UserInfo.deleteAllUserExcptMe();
            this.gameScene.headUp.reHeadState(UserPosition.Up);
        }

        /**玩家重连 */
        private revUserReconnect(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }

            // Tips.showTop(data.info.nick + "重新连接");
        }

        /**玩家连接状态 */
        private revUserConnectState(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }

            if (data.info.is_offline) {
                // Tips.showTop(data.info.nick + "断开连接");
            }
        }

        /**定庄 */
        private revDingZhuang(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101004.info;
            revData = data.info;

            App.DataCenter.UserInfo.clearZhuang();
            App.DataCenter.UserInfo.getUserBySeatID(revData.bank_seat_id).zhuangFlag = true;
            
            if (revData.dice.length > 1) {
                this.gameScene.diskMod.setState(DiskState.dice, 0, revData.dice);
            }
            else {
                this.gameScene.headDown.reZhuangFlag(UserPosition.Down);
                this.gameScene.headUp.reZhuangFlag(UserPosition.Up);
                setTimeout(()=>{
                    console.log("deal card");
                    App.DataCenter.MsgCache.exeMsg(ProtocolHeadRev.R_101005);
                }, 1100);
            }

            App.DataCenter.runingData.gameState = GameState.DealCard;
        }

        /**接收玩家加入房间 */
        private revUserInto(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101107.info;
            revData = data.info;

            var user = new UserVO();
            user.initUserFromSocket(revData);
            App.DataCenter.UserInfo.addUser(user);

            this.gameScene.headUp.reHeadState(UserPosition.Up);

            this.gameScene.matchMod.setType(MatchType.common);
        }

        /**发牌 */
        private revDealCard(data) {
            App.DataCenter.MsgCache.addMsg(ProtocolHeadRev.R_101005, data, this.exeDealCard, this);
        }

        /**发牌处理 */
        private exeDealCard(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101005.info;
            revData = data.info;
            for (var i = 0;i < revData.card_list.length;i ++) {
                if (revData.card_list[i].seat_id == App.DataCenter.UserInfo.myUserInfo.seatID) {
                    this.gameScene.cardMod.dealCardShow(revData.card_list[i].card_list);
                }
            }
        }

        /**补花 */
        private revDealHua(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            App.DataCenter.MsgCache.addMsgData(ProtocolHeadRev.R_101008, data.info, true);
        }

        /**动作提示 */
        private revAct(data) {
            console.log("gameState==", App.DataCenter.runingData.gameState);
            if (App.DataCenter.runingData.gameState == GameState.Playing) {
                this.exeAct(data);
            }
            else {
                App.DataCenter.MsgCache.addMsg(ProtocolHeadRev.R_101001, data, this.exeAct, this);
            }
        }

        /**动作提示处理 */
        private exeAct(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101001.info;
            revData = data.info;

            var pos = App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            // 更新圆盘
            var state = pos ? DiskState.up : DiskState.down;
            this.gameScene.diskMod.setState(state, App.DataCenter.roomInfo.getConfigForType(App.DataCenter.runingData.curentRoomType).outCardTime);

            console.log("接收动作,seat_id=="+revData.seat_id+"----"+"mySeatId=="+App.DataCenter.UserInfo.myUserInfo.seatID);
            if (revData.seat_id == App.DataCenter.UserInfo.myUserInfo.seatID) {
                console.log("动作操作数据：", revData);
                App.DataCenter.MsgCache.addMsgData(ProtocolHeadRev.R_101001, revData);
                var actList = CardLogic.getInstance().getActListFromKey(revData.act_info);
                this.gameScene.selectBtnMod.showActBtn(actList);
            }
        }

        /**摸牌 */
        private revMoCard(data) {
            this.exeMoCard(data);
        }

        /**摸牌处理 */
        private exeMoCard(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101002.info;
            revData = data.info;
            var pos = App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            this.gameScene.cardMod.moCardShow(revData.card_list[0], pos);

            // 更新圆盘
            var state = pos ? DiskState.up : DiskState.down;
            this.gameScene.diskMod.setState(state, App.DataCenter.roomInfo.getConfigForType(App.DataCenter.runingData.curentRoomType).outCardTime);

            // 更新出牌状态
            if (pos == UserPosition.Down) {
                App.DataCenter.runingData.bAllowOutCard = true;
            }

            // 更新剩余牌数
            this.gameScene.reResidue(true, revData.remain_count)
        }

        /**摸牌补花 */
        private revMoHua(data) {
            this.exeMoHua(data);
        }

        /**摸牌补花处理 */
        private exeMoHua(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101007.info;
            revData = data.info;

            var pos = App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            this.gameScene.cardMod.moCardBuHua(pos);
            this.gameScene.flowerMod.setFlowerState(pos, 1);
        }

        /**操作响应 */
        private revActDo(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101112.info;
            revData = data.info;

            var doAct:ACT_state = revData.act_type;
            if (doAct == 110) {
                doAct = ACT_state.Act_Guohu;
            }
            var pos:UserPosition = App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            var doCardList:Array<number> = revData.card_list;

            this.gameScene.onActDo(doAct, pos, doCardList, revData.all_hand_cards);
        }

        /**作弊接口返回 */
        private revCheat(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_100999.info;
            revData = data.info;

            if (revData.test_type == 1) {
                this.gameScene.cardMod.reCardValue(this.gameScene.cheatMod.selectValue0, this.gameScene.cheatMod.selectValue1);
                this.gameScene.cheatMod.clearSelect();
            }
            else if (revData.test_type == 3) {
                this.gameScene.cheatMod.card_s3.setCardValueAndShowOut(revData.cards[0]);
            }
        }

        /**游戏结束 */
        private revOver(data) {
            var cData = ArrayTool.deepCopy(data);
            App.DataCenter.MsgCache.addMsg(ProtocolHeadRev.R_101003, cData, this.exeOver, this);
            this.exeOver(cData);
        }

        /**游戏结束处理 */
        private exeOver(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101003.info;
            revData = ArrayTool.deepCopy(data.info);

            // 推牌
            for (var key in revData.player_info) {
                var pos = App.DataCenter.UserInfo.getPosFromSeat(Number(key));
                this.gameScene.cardMod.huCardShow(pos, revData.player_info[key].hand_card);
            }
            App.DataCenter.runingData.gameState = GameState.Over;

            this.gameScene.diskMod.setState(DiskState.normal);
        }

        /**游戏结算 */
        private revResult(data) {
            App.DataCenter.MsgCache.addMsg(ProtocolHeadRev.R_101006, data, this.exeResult, this);
            setTimeout(()=>{
                this.exeResult(data);
            }, 2000)
        }

        /**游戏结算处理 */
        private exeResult(data) {
            if (data.code != 200) {
                Tips.showTop(data.desc);
                return;
            }
            var revData = ProtocolDataRev.R_101006.info;
            revData = data.info;

            App.PanelManager.open(PanelConst.ResultPanel);
        }
    }
}