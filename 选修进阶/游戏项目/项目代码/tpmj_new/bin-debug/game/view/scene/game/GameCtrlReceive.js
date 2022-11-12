var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 消息接收、处理模块
     */
    var GameCtrlReceive = (function () {
        function GameCtrlReceive(ctrl) {
            this.gameCtrl = ctrl;
        }
        Object.defineProperty(GameCtrlReceive.prototype, "gameScene", {
            /**对应的scene */
            get: function () {
                return this.gameCtrl.gameScene;
            },
            enumerable: true,
            configurable: true
        });
        /**对应场景添加到显示列表时调用 */
        GameCtrlReceive.prototype.onRegister = function () {
            var gameSocket = Tpm.App.gameSocket;
            gameSocket.register(Tpm.ProtocolHeadRev.R_100100, this.revReady, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_100103, this.revExit, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101001, this.revAct, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101004, this.revDingZhuang, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101105, this.revElseExit, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101107, this.revUserInto, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101109, this.revUserReconnect, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101110, this.revUserConnectState, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101005, this.revDealCard, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101008, this.revDealHua, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101002, this.revMoCard, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101112, this.revActDo, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101007, this.revMoHua, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_100999, this.revCheat, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101003, this.revOver, this);
            gameSocket.register(Tpm.ProtocolHeadRev.R_101006, this.revResult, this);
        };
        /**对应场景从显示列表移除是调用 */
        GameCtrlReceive.prototype.onRemove = function () {
        };
        /**自己准备 */
        GameCtrlReceive.prototype.revReady = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_100100.info;
            revData = data.info;
            Tpm.App.DataCenter.runingData.gameState = Tpm.GameState.Ready;
            this.gameScene.readyMod.hideBeginBtn();
        };
        /**退出房间 */
        GameCtrlReceive.prototype.revExit = function (data) {
            if (data.code != 200) {
                // Tips.showTop(data.desc);
                Tpm.Tips.showTop("游戏已经开始，无法退出。");
                return;
            }
            Tpm.App.DataCenter.UserInfo.deleteAllUserExcptMe();
            Tpm.App.DataCenter.UserInfo.clearZhuang();
            Tpm.App.SceneManager.runScene(Tpm.SceneConst.HallScene, Tpm.App.getController(Tpm.HallController.NAME));
        };
        /**其他玩家退出 */
        GameCtrlReceive.prototype.revElseExit = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            Tpm.App.DataCenter.UserInfo.deleteAllUserExcptMe();
            this.gameScene.headUp.reHeadState(Tpm.UserPosition.Up);
        };
        /**玩家重连 */
        GameCtrlReceive.prototype.revUserReconnect = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            // Tips.showTop(data.info.nick + "重新连接");
        };
        /**玩家连接状态 */
        GameCtrlReceive.prototype.revUserConnectState = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            if (data.info.is_offline) {
            }
        };
        /**定庄 */
        GameCtrlReceive.prototype.revDingZhuang = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101004.info;
            revData = data.info;
            Tpm.App.DataCenter.UserInfo.clearZhuang();
            Tpm.App.DataCenter.UserInfo.getUserBySeatID(revData.bank_seat_id).zhuangFlag = true;
            if (revData.dice.length > 1) {
                this.gameScene.diskMod.setState(Tpm.DiskState.dice, 0, revData.dice);
            }
            else {
                this.gameScene.headDown.reZhuangFlag(Tpm.UserPosition.Down);
                this.gameScene.headUp.reZhuangFlag(Tpm.UserPosition.Up);
                setTimeout(function () {
                    console.log("deal card");
                    Tpm.App.DataCenter.MsgCache.exeMsg(Tpm.ProtocolHeadRev.R_101005);
                }, 1100);
            }
            Tpm.App.DataCenter.runingData.gameState = Tpm.GameState.DealCard;
        };
        /**接收玩家加入房间 */
        GameCtrlReceive.prototype.revUserInto = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101107.info;
            revData = data.info;
            var user = new Tpm.UserVO();
            user.initUserFromSocket(revData);
            Tpm.App.DataCenter.UserInfo.addUser(user);
            this.gameScene.headUp.reHeadState(Tpm.UserPosition.Up);
            this.gameScene.matchMod.setType(Tpm.MatchType.common);
        };
        /**发牌 */
        GameCtrlReceive.prototype.revDealCard = function (data) {
            Tpm.App.DataCenter.MsgCache.addMsg(Tpm.ProtocolHeadRev.R_101005, data, this.exeDealCard, this);
        };
        /**发牌处理 */
        GameCtrlReceive.prototype.exeDealCard = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101005.info;
            revData = data.info;
            for (var i = 0; i < revData.card_list.length; i++) {
                if (revData.card_list[i].seat_id == Tpm.App.DataCenter.UserInfo.myUserInfo.seatID) {
                    this.gameScene.cardMod.dealCardShow(revData.card_list[i].card_list);
                }
            }
        };
        /**补花 */
        GameCtrlReceive.prototype.revDealHua = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            Tpm.App.DataCenter.MsgCache.addMsgData(Tpm.ProtocolHeadRev.R_101008, data.info, true);
        };
        /**动作提示 */
        GameCtrlReceive.prototype.revAct = function (data) {
            console.log("gameState==", Tpm.App.DataCenter.runingData.gameState);
            if (Tpm.App.DataCenter.runingData.gameState == Tpm.GameState.Playing) {
                this.exeAct(data);
            }
            else {
                Tpm.App.DataCenter.MsgCache.addMsg(Tpm.ProtocolHeadRev.R_101001, data, this.exeAct, this);
            }
        };
        /**动作提示处理 */
        GameCtrlReceive.prototype.exeAct = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101001.info;
            revData = data.info;
            var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            // 更新圆盘
            var state = pos ? Tpm.DiskState.up : Tpm.DiskState.down;
            this.gameScene.diskMod.setState(state, Tpm.App.DataCenter.roomInfo.getConfigForType(Tpm.App.DataCenter.runingData.curentRoomType).outCardTime);
            console.log("接收动作,seat_id==" + revData.seat_id + "----" + "mySeatId==" + Tpm.App.DataCenter.UserInfo.myUserInfo.seatID);
            if (revData.seat_id == Tpm.App.DataCenter.UserInfo.myUserInfo.seatID) {
                console.log("动作操作数据：", revData);
                Tpm.App.DataCenter.MsgCache.addMsgData(Tpm.ProtocolHeadRev.R_101001, revData);
                var actList = Tpm.CardLogic.getInstance().getActListFromKey(revData.act_info);
                this.gameScene.selectBtnMod.showActBtn(actList);
            }
        };
        /**摸牌 */
        GameCtrlReceive.prototype.revMoCard = function (data) {
            this.exeMoCard(data);
        };
        /**摸牌处理 */
        GameCtrlReceive.prototype.exeMoCard = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101002.info;
            revData = data.info;
            var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            this.gameScene.cardMod.moCardShow(revData.card_list[0], pos);
            // 更新圆盘
            var state = pos ? Tpm.DiskState.up : Tpm.DiskState.down;
            this.gameScene.diskMod.setState(state, Tpm.App.DataCenter.roomInfo.getConfigForType(Tpm.App.DataCenter.runingData.curentRoomType).outCardTime);
            // 更新出牌状态
            if (pos == Tpm.UserPosition.Down) {
                Tpm.App.DataCenter.runingData.bAllowOutCard = true;
            }
            // 更新剩余牌数
            this.gameScene.reResidue(true, revData.remain_count);
        };
        /**摸牌补花 */
        GameCtrlReceive.prototype.revMoHua = function (data) {
            this.exeMoHua(data);
        };
        /**摸牌补花处理 */
        GameCtrlReceive.prototype.exeMoHua = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101007.info;
            revData = data.info;
            var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            this.gameScene.cardMod.moCardBuHua(pos);
            this.gameScene.flowerMod.setFlowerState(pos, 1);
        };
        /**操作响应 */
        GameCtrlReceive.prototype.revActDo = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101112.info;
            revData = data.info;
            var doAct = revData.act_type;
            if (doAct == 110) {
                doAct = Tpm.ACT_state.Act_Guohu;
            }
            var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(revData.seat_id);
            var doCardList = revData.card_list;
            this.gameScene.onActDo(doAct, pos, doCardList, revData.all_hand_cards);
        };
        /**作弊接口返回 */
        GameCtrlReceive.prototype.revCheat = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_100999.info;
            revData = data.info;
            if (revData.test_type == 1) {
                this.gameScene.cardMod.reCardValue(this.gameScene.cheatMod.selectValue0, this.gameScene.cheatMod.selectValue1);
                this.gameScene.cheatMod.clearSelect();
            }
            else if (revData.test_type == 3) {
                this.gameScene.cheatMod.card_s3.setCardValueAndShowOut(revData.cards[0]);
            }
        };
        /**游戏结束 */
        GameCtrlReceive.prototype.revOver = function (data) {
            var cData = Tpm.ArrayTool.deepCopy(data);
            Tpm.App.DataCenter.MsgCache.addMsg(Tpm.ProtocolHeadRev.R_101003, cData, this.exeOver, this);
            this.exeOver(cData);
        };
        /**游戏结束处理 */
        GameCtrlReceive.prototype.exeOver = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101003.info;
            revData = Tpm.ArrayTool.deepCopy(data.info);
            // 推牌
            for (var key in revData.player_info) {
                var pos = Tpm.App.DataCenter.UserInfo.getPosFromSeat(Number(key));
                this.gameScene.cardMod.huCardShow(pos, revData.player_info[key].hand_card);
            }
            Tpm.App.DataCenter.runingData.gameState = Tpm.GameState.Over;
            this.gameScene.diskMod.setState(Tpm.DiskState.normal);
        };
        /**游戏结算 */
        GameCtrlReceive.prototype.revResult = function (data) {
            var _this = this;
            Tpm.App.DataCenter.MsgCache.addMsg(Tpm.ProtocolHeadRev.R_101006, data, this.exeResult, this);
            setTimeout(function () {
                _this.exeResult(data);
            }, 2000);
        };
        /**游戏结算处理 */
        GameCtrlReceive.prototype.exeResult = function (data) {
            if (data.code != 200) {
                Tpm.Tips.showTop(data.desc);
                return;
            }
            var revData = Tpm.ProtocolDataRev.R_101006.info;
            revData = data.info;
            Tpm.App.PanelManager.open(Tpm.PanelConst.ResultPanel);
        };
        return GameCtrlReceive;
    }());
    Tpm.GameCtrlReceive = GameCtrlReceive;
    __reflect(GameCtrlReceive.prototype, "Tpm.GameCtrlReceive");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameCtrlReceive.js.map