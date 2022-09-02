module Tpm {
    export class HallHeadMod extends BaseUI {
        private headGro:eui.Group;
        private headMask:eui.Image;
        private headImg:eui.Image;
        private nameLab:eui.Label;
        private idLab:eui.Label;
        private moneyGro:eui.Group;
        private goldLab:eui.Label;
        private addBtn:eui.Button;
        private arrowGro:eui.Group;
        private diamondGro:eui.Group;
        private diamondLab:eui.Label;
        private showmallGro:eui.Group;
        private timeOut:number;

        public constructor() {
            super();
            this.skinName = TpmSkin.HallHeadModSkin;
        }

        protected childrenCreated() {
            this.headImg.mask = this.headMask;
        }

		protected onEnable() {
            // 初始化钻石UI显示状态
            this.setDiamondVisible();

            this.headGro.addEventListener(egret.TouchEvent.TOUCH_TAP, this.showPersonalInfo, this);
            this.arrowGro.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onArrow, this);
            this.addBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
        }

		protected onRemove() {
            this.headGro.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.showPersonalInfo, this);
            this.arrowGro.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onArrow, this);
            this.addBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onAdd, this);
        }

        /**
         * 设置钻石UI显示状态
         */
        public setDiamondVisible(visible: boolean = false) {
            if (visible) {
                this.arrowGro.visible = false;
                this.diamondGro.visible = true;
            }
            else {
                this.arrowGro.visible = true;
                this.diamondGro.visible = false;
            }
        }

        /**
         * 获取Arrow区域
         */
        public get arrowGroup () {
            return this.arrowGro;
        }

        /**
         * 点击向上箭头区域
         */
        private onArrow() {
            this.setDiamondVisible(true);
			this.timeOut = setTimeout(()=>{
				this.setDiamondVisible(false);
				clearTimeout(this.timeOut);
			}, 3000, this);
            HallHttpDataSend.sendGetDiamondAndGold();
        }
        /**
         * 显示个人信息
         */
        private showPersonalInfo()
        {
            HallHttpDataSend.sendGetUserInfo();
        }

        /**
         * 点击+
         */
        private onAdd() {
            HallHttpDataSend.sendGetGoodsList();
            // App.PanelManager.open(PanelConst.ShopMallPanel);
        }
         /**
         * 更新钻石金币
         */
        public updateDiamondAndGold(diamond, gold) {
            this.diamondLab.text = diamond+"";//NumberTool.sperateMoney(diamond);
            this.goldLab.text = NumberTool.formatMoney(gold);
        }
        /**
         * 更新个人信息
         */
        public updatePersonalInfo() {
            this.nameLab.text =StringTool.formatNickName(App.DataCenter.UserInfo.myUserInfo.nickName,12);//StringTool.formatNickName("tese1tese11411",12);
            this.idLab.text ="ID:"+App.DataCenter.UserInfo.myUserInfo.userID+""; 
            this.diamondLab.text = App.DataCenter.UserInfo.myUserInfo.diamond+"";
            this.goldLab.text = NumberTool.formatMoney(App.DataCenter.UserInfo.myUserInfo.gold);
            this.headImg.source= App.DataCenter.UserInfo.myUserInfo.headUrl;
        }
    }
}