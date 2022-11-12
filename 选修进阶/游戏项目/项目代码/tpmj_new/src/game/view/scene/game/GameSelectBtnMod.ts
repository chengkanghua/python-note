module Tpm{
    /**
     * 由于美术资源的不规范或龙骨动画的一些问题，这个模块有点骚，请勿模仿
     */
    export class GameSelectBtnMod extends eui.Component {
        private tipsGro:eui.Group;
        private tipsLab:eui.Label;

        private passBtn:Tpm.SelectActBtn;
        private eatBtn:Tpm.SelectActBtn;
        private pengBtn:Tpm.SelectActBtn;
        private gangBtn:Tpm.SelectActBtn;
        private huBtn:Tpm.SelectActBtn;
        private guoHuBtn:Tpm.SelectActBtn;
        private cancleBtn:Tpm.SelectActBtn;
        private tingBtn:Tpm.SelectActBtn;

        private passBtn0:Tpm.SelectActBtn;
        private eatBtn0:Tpm.SelectActBtn;
        private pengBtn0:Tpm.SelectActBtn;
        private gangBtn0:Tpm.SelectActBtn;
        private huBtn0:Tpm.SelectActBtn;
        private guoHuBtn0:Tpm.SelectActBtn;
        private cancleBtn0:Tpm.SelectActBtn;
        private tingBtn0:Tpm.SelectActBtn;

        private btnList = {};
        private btnListTouch = {};
        private vectorWidth = 1126;
        private itemWidth = 150;
        private bInitRes: boolean = false;

        private touchBtnList: Array<SelectActBtn>;
        private showBtnList: Array<SelectActBtn>;
        private actList: Array<number>;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameSelectBtnModSkin;
        }

        public childrenCreated() {
            this.btnList[ACT_state.Act_Pass] = this.passBtn;
            this.btnList[ACT_state.Act_Peng] = this.pengBtn;
            this.btnList[ACT_state.Act_Chi] = this.eatBtn;
            this.btnList[ACT_state.Act_Gang] = this.gangBtn;
            this.btnList[ACT_state.Act_BuGang] = this.gangBtn;
            this.btnList[ACT_state.Act_AnGang] = this.gangBtn;
            this.btnList[ACT_state.Act_DianHu] = this.huBtn;
            this.btnList[ACT_state.Act_Zimo] = this.huBtn;
            this.btnList[ACT_state.Act_Guohu] = this.guoHuBtn;
            this.btnList[ACT_state.Act_Cancle] = this.cancleBtn;
            this.btnList[ACT_state.Act_Ting] = this.tingBtn;

            this.btnListTouch[ACT_state.Act_Pass] = this.passBtn0;
            this.btnListTouch[ACT_state.Act_Peng] = this.pengBtn0;
            this.btnListTouch[ACT_state.Act_Chi] = this.eatBtn0;
            this.btnListTouch[ACT_state.Act_Gang] = this.gangBtn0;
            this.btnListTouch[ACT_state.Act_BuGang] = this.gangBtn0;
            this.btnListTouch[ACT_state.Act_AnGang] = this.gangBtn0;
            this.btnListTouch[ACT_state.Act_DianHu] = this.huBtn0;
            this.btnListTouch[ACT_state.Act_Zimo] = this.huBtn0;
            this.btnListTouch[ACT_state.Act_Guohu] = this.guoHuBtn0;
            this.btnListTouch[ACT_state.Act_Cancle] = this.cancleBtn0;
            this.btnListTouch[ACT_state.Act_Ting] = this.tingBtn0;


            this.touchEnabled = false;
        }

        private initRes() {
            if (this.bInitRes == false) {
                this.bInitRes = true;
                this.passBtn.setNewActSkin(ACT_act.Act_Pass);
                this.eatBtn.setNewActSkin(ACT_act.Act_Chi);
                this.pengBtn.setNewActSkin(ACT_act.Act_Peng);
                this.gangBtn.setNewActSkin(ACT_act.Act_Gang);
                this.huBtn.setNewActSkin(ACT_act.Act_Hu);
                this.guoHuBtn.setNewActSkin(ACT_act.Act_Guohu);
                this.cancleBtn.setNewActSkin(ACT_act.Act_cancle);
                this.tingBtn.setNewActSkin(ACT_act.Act_Ting);

                this.passBtn0.setSortWeight(ACT_act.Act_Pass);
                this.eatBtn0.setSortWeight(ACT_act.Act_Chi);
                this.pengBtn0.setSortWeight(ACT_act.Act_Peng);
                this.gangBtn0.setSortWeight(ACT_act.Act_Gang);
                this.huBtn0.setSortWeight(ACT_act.Act_Hu);
                this.guoHuBtn0.setSortWeight(ACT_act.Act_Guohu);
                this.cancleBtn0.setSortWeight(ACT_act.Act_cancle);
                this.tingBtn0.setSortWeight(ACT_act.Act_Ting);
            }
        }

        /**
         * 监听
         */
        public onTouch(touchRect: eui.Rect) {
            for (var key in this.btnListTouch) {
                if (this.btnListTouch[key] == touchRect.parent) {
                    if (this.btnListTouch[key] == this.gangBtn0) {
                        if (this.keyIn(ACT_state.Act_AnGang) && this.keyIn(ACT_state.Act_BuGang)) {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_ZuheGang);
                        }
                        else if (this.keyIn(ACT_state.Act_AnGang)) {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_AnGang);
                        }
                        else if (this.keyIn(ACT_state.Act_BuGang)) {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_BuGang);
                        }
                        else {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_Gang);
                        }
                    }
                    else if (this.btnListTouch[key] == this.huBtn0) {
                        if (this.keyIn(ACT_state.Act_DianHu) && !this.keyIn(ACT_state.Act_Zimo)) {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_DianHu);
                        }
                        else if (!this.keyIn(ACT_state.Act_DianHu) && this.keyIn(ACT_state.Act_Zimo)) {
                            this.dispatchEventWith("sendActEvent", false, ACT_state.Act_Zimo);
                        }
                    }
                    else {
                        this.dispatchEventWith("sendActEvent", false, parseInt(key));
                    }
                    break;
                }
            }
        }

        private keyIn(state: ACT_state) {
            for(var i = 0;i < this.actList.length;i ++) {
                if (state == this.actList[i]) {
                    return true;
                }
            }
            return false;
        }

        /**
         * 根据可行操作，显示操作面板
         * @param actList 动作列表Act_state (碰、杠、胡等)
         */
        public showActBtn(actList) {
            console.log("btnlit===", actList);
            this.actList = ArrayTool.deepCopy(actList);
            if ( (this.keyIn(ACT_state.Act_DianHu) || this.keyIn(ACT_state.Act_Zimo)) && App.DataCenter.runingData.guoHuFlag && App.DataCenter.runingData.ownTingState)  {
                for (var i = 0;i < this.actList.length;i ++) {
                    if (this.actList[i] == ACT_state.Act_Pass) {
                        this.actList[i] = ACT_state.Act_Guohu;
                        this.setTipsState(true);
                        break;
                    }
                }
            }

            this.initRes();
            var len = this.actList.length;
            this.showBtnList = [];
            this.touchBtnList = [];
            for(var i=len-1;i>=0;i--){
                var act = this.actList[i];
                var btn = this.btnList[act];
                var btnT = this.btnListTouch[act];
                if(btn == null){
                    console.error("缺少动作操作按钮:",act);
                    continue;
                }
                if ( this.btnAdded(btn) ) {
                    console.log("重复按钮");
                    continue;
                }
                this.showBtnList.push(btn);
                this.touchBtnList.push(btnT);
            }

            for(var key in this.btnList) {
                this.btnList[key].visible = false;
            }
            for(var key in this.btnListTouch) {
                this.btnListTouch[key].visible = false;
            }
            for(var i = 0;i < this.showBtnList.length;i ++) {
                this.showBtnList[i].visible = true;
                this.showBtnList[i].playAnim();
                this.touchBtnList[i].visible = true;
            }

            this.showBtnList.sort((a, b)=>{
                return  a.sortWeight - b.sortWeight;
            })
            this.touchBtnList.sort((a, b)=>{
                return  a.sortWeight - b.sortWeight;
            })

            var btnLen:number = this.showBtnList.length;
            var startX: number = this.vectorWidth - len*this.itemWidth;
            var offsetX = 0;
            for(var i = btnLen-1;i >= 0;i--){
                var child = this.showBtnList[i];
                var childT = this.touchBtnList[i];
                childT.x = child.x = startX + this.itemWidth*i + offsetX;
            }
            
            if (this.actList.length > 1 || (this.actList[0] != ACT_state.Act_Out && this.actList.length == 1)) {
                this.show();
            }
        }

        private btnAdded(btn: SelectActBtn):boolean {
            for (var i = 0;i < this.showBtnList.length;i ++) {
                if (this.showBtnList[i] == btn) {
                    return true;
                }
            }
            return false;
        }

        public show() {
            this.visible = true;
            App.DataCenter.runingData.selectBtnState = true;
        }

        public hide() {
            for (var key in this.btnList) {
                this.btnList[key].stopAnim();
            }
            this.visible = false;
            App.DataCenter.runingData.selectBtnState = false;
            this.setTipsState(false);
        }

        public reShow() {
            for(var i = 0;i < this.showBtnList.length;i ++) {
                this.showBtnList[i].visible = true;
                this.showBtnList[i].playAnim();
            }
            if (this.keyIn(ACT_state.Act_DianHu) || this.keyIn(ACT_state.Act_Zimo)) {
                App.DataCenter.runingData.bAllowOutCard = false;
            }
            this.show();
        }

        private setTipsState(flag: boolean) {
            this.tipsGro.visible = flag;
            if (flag) {
                var times = App.DataCenter.runingData.ownGuoTimes+1;
                this.tipsLab.text = "过胡" + times + "次，金币x" + Math.pow(2, times);
            }
        }
    }
}
