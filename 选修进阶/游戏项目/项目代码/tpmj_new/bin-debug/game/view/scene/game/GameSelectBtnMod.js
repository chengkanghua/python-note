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
    /**
     * 由于美术资源的不规范或龙骨动画的一些问题，这个模块有点骚，请勿模仿
     */
    var GameSelectBtnMod = (function (_super) {
        __extends(GameSelectBtnMod, _super);
        function GameSelectBtnMod() {
            var _this = _super.call(this) || this;
            _this.btnList = {};
            _this.btnListTouch = {};
            _this.vectorWidth = 1126;
            _this.itemWidth = 150;
            _this.bInitRes = false;
            _this.skinName = TpmSkin.GameSelectBtnModSkin;
            return _this;
        }
        GameSelectBtnMod.prototype.childrenCreated = function () {
            this.btnList[Tpm.ACT_state.Act_Pass] = this.passBtn;
            this.btnList[Tpm.ACT_state.Act_Peng] = this.pengBtn;
            this.btnList[Tpm.ACT_state.Act_Chi] = this.eatBtn;
            this.btnList[Tpm.ACT_state.Act_Gang] = this.gangBtn;
            this.btnList[Tpm.ACT_state.Act_BuGang] = this.gangBtn;
            this.btnList[Tpm.ACT_state.Act_AnGang] = this.gangBtn;
            this.btnList[Tpm.ACT_state.Act_DianHu] = this.huBtn;
            this.btnList[Tpm.ACT_state.Act_Zimo] = this.huBtn;
            this.btnList[Tpm.ACT_state.Act_Guohu] = this.guoHuBtn;
            this.btnList[Tpm.ACT_state.Act_Cancle] = this.cancleBtn;
            this.btnList[Tpm.ACT_state.Act_Ting] = this.tingBtn;
            this.btnListTouch[Tpm.ACT_state.Act_Pass] = this.passBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Peng] = this.pengBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Chi] = this.eatBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Gang] = this.gangBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_BuGang] = this.gangBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_AnGang] = this.gangBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_DianHu] = this.huBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Zimo] = this.huBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Guohu] = this.guoHuBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Cancle] = this.cancleBtn0;
            this.btnListTouch[Tpm.ACT_state.Act_Ting] = this.tingBtn0;
            this.touchEnabled = false;
        };
        GameSelectBtnMod.prototype.initRes = function () {
            if (this.bInitRes == false) {
                this.bInitRes = true;
                this.passBtn.setNewActSkin(Tpm.ACT_act.Act_Pass);
                this.eatBtn.setNewActSkin(Tpm.ACT_act.Act_Chi);
                this.pengBtn.setNewActSkin(Tpm.ACT_act.Act_Peng);
                this.gangBtn.setNewActSkin(Tpm.ACT_act.Act_Gang);
                this.huBtn.setNewActSkin(Tpm.ACT_act.Act_Hu);
                this.guoHuBtn.setNewActSkin(Tpm.ACT_act.Act_Guohu);
                this.cancleBtn.setNewActSkin(Tpm.ACT_act.Act_cancle);
                this.tingBtn.setNewActSkin(Tpm.ACT_act.Act_Ting);
                this.passBtn0.setSortWeight(Tpm.ACT_act.Act_Pass);
                this.eatBtn0.setSortWeight(Tpm.ACT_act.Act_Chi);
                this.pengBtn0.setSortWeight(Tpm.ACT_act.Act_Peng);
                this.gangBtn0.setSortWeight(Tpm.ACT_act.Act_Gang);
                this.huBtn0.setSortWeight(Tpm.ACT_act.Act_Hu);
                this.guoHuBtn0.setSortWeight(Tpm.ACT_act.Act_Guohu);
                this.cancleBtn0.setSortWeight(Tpm.ACT_act.Act_cancle);
                this.tingBtn0.setSortWeight(Tpm.ACT_act.Act_Ting);
            }
        };
        /**
         * 监听
         */
        GameSelectBtnMod.prototype.onTouch = function (touchRect) {
            for (var key in this.btnListTouch) {
                if (this.btnListTouch[key] == touchRect.parent) {
                    if (this.btnListTouch[key] == this.gangBtn0) {
                        if (this.keyIn(Tpm.ACT_state.Act_AnGang) && this.keyIn(Tpm.ACT_state.Act_BuGang)) {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_ZuheGang);
                        }
                        else if (this.keyIn(Tpm.ACT_state.Act_AnGang)) {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_AnGang);
                        }
                        else if (this.keyIn(Tpm.ACT_state.Act_BuGang)) {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_BuGang);
                        }
                        else {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_Gang);
                        }
                    }
                    else if (this.btnListTouch[key] == this.huBtn0) {
                        if (this.keyIn(Tpm.ACT_state.Act_DianHu) && !this.keyIn(Tpm.ACT_state.Act_Zimo)) {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_DianHu);
                        }
                        else if (!this.keyIn(Tpm.ACT_state.Act_DianHu) && this.keyIn(Tpm.ACT_state.Act_Zimo)) {
                            this.dispatchEventWith("sendActEvent", false, Tpm.ACT_state.Act_Zimo);
                        }
                    }
                    else {
                        this.dispatchEventWith("sendActEvent", false, parseInt(key));
                    }
                    break;
                }
            }
        };
        GameSelectBtnMod.prototype.keyIn = function (state) {
            for (var i = 0; i < this.actList.length; i++) {
                if (state == this.actList[i]) {
                    return true;
                }
            }
            return false;
        };
        /**
         * 根据可行操作，显示操作面板
         * @param actList 动作列表Act_state (碰、杠、胡等)
         */
        GameSelectBtnMod.prototype.showActBtn = function (actList) {
            console.log("btnlit===", actList);
            this.actList = Tpm.ArrayTool.deepCopy(actList);
            if ((this.keyIn(Tpm.ACT_state.Act_DianHu) || this.keyIn(Tpm.ACT_state.Act_Zimo)) && Tpm.App.DataCenter.runingData.guoHuFlag && Tpm.App.DataCenter.runingData.ownTingState) {
                for (var i = 0; i < this.actList.length; i++) {
                    if (this.actList[i] == Tpm.ACT_state.Act_Pass) {
                        this.actList[i] = Tpm.ACT_state.Act_Guohu;
                        this.setTipsState(true);
                        break;
                    }
                }
            }
            this.initRes();
            var len = this.actList.length;
            this.showBtnList = [];
            this.touchBtnList = [];
            for (var i = len - 1; i >= 0; i--) {
                var act = this.actList[i];
                var btn = this.btnList[act];
                var btnT = this.btnListTouch[act];
                if (btn == null) {
                    console.error("缺少动作操作按钮:", act);
                    continue;
                }
                if (this.btnAdded(btn)) {
                    console.log("重复按钮");
                    continue;
                }
                this.showBtnList.push(btn);
                this.touchBtnList.push(btnT);
            }
            for (var key in this.btnList) {
                this.btnList[key].visible = false;
            }
            for (var key in this.btnListTouch) {
                this.btnListTouch[key].visible = false;
            }
            for (var i = 0; i < this.showBtnList.length; i++) {
                this.showBtnList[i].visible = true;
                this.showBtnList[i].playAnim();
                this.touchBtnList[i].visible = true;
            }
            this.showBtnList.sort(function (a, b) {
                return a.sortWeight - b.sortWeight;
            });
            this.touchBtnList.sort(function (a, b) {
                return a.sortWeight - b.sortWeight;
            });
            var btnLen = this.showBtnList.length;
            var startX = this.vectorWidth - len * this.itemWidth;
            var offsetX = 0;
            for (var i = btnLen - 1; i >= 0; i--) {
                var child = this.showBtnList[i];
                var childT = this.touchBtnList[i];
                childT.x = child.x = startX + this.itemWidth * i + offsetX;
            }
            if (this.actList.length > 1 || (this.actList[0] != Tpm.ACT_state.Act_Out && this.actList.length == 1)) {
                this.show();
            }
        };
        GameSelectBtnMod.prototype.btnAdded = function (btn) {
            for (var i = 0; i < this.showBtnList.length; i++) {
                if (this.showBtnList[i] == btn) {
                    return true;
                }
            }
            return false;
        };
        GameSelectBtnMod.prototype.show = function () {
            this.visible = true;
            Tpm.App.DataCenter.runingData.selectBtnState = true;
        };
        GameSelectBtnMod.prototype.hide = function () {
            for (var key in this.btnList) {
                this.btnList[key].stopAnim();
            }
            this.visible = false;
            Tpm.App.DataCenter.runingData.selectBtnState = false;
            this.setTipsState(false);
        };
        GameSelectBtnMod.prototype.reShow = function () {
            for (var i = 0; i < this.showBtnList.length; i++) {
                this.showBtnList[i].visible = true;
                this.showBtnList[i].playAnim();
            }
            if (this.keyIn(Tpm.ACT_state.Act_DianHu) || this.keyIn(Tpm.ACT_state.Act_Zimo)) {
                Tpm.App.DataCenter.runingData.bAllowOutCard = false;
            }
            this.show();
        };
        GameSelectBtnMod.prototype.setTipsState = function (flag) {
            this.tipsGro.visible = flag;
            if (flag) {
                var times = Tpm.App.DataCenter.runingData.ownGuoTimes + 1;
                this.tipsLab.text = "过胡" + times + "次，金币x" + Math.pow(2, times);
            }
        };
        return GameSelectBtnMod;
    }(eui.Component));
    Tpm.GameSelectBtnMod = GameSelectBtnMod;
    __reflect(GameSelectBtnMod.prototype, "Tpm.GameSelectBtnMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameSelectBtnMod.js.map