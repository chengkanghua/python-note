module Tpm {
    export class HallScene extends BaseScene {
        /**大厅场景控制类*/
        protected ctrl: HallController;

        private hallBackBtn: eui.Button;
        private hallKefuBtn: eui.Button;
        private hallQuickBtn: eui.Button;
        public headMod: Tpm.HallHeadMod;
        public btnMod: Tpm.HallBtnMod;
        public roomMod:Tpm.HallRoomMod;

        private quickDb: dragonBones.EgretArmatureDisplay;
        private moveGro:eui.Group;

        public constructor() {
            super();
            this.skinName = TpmSkin.HallSceneSkin;
        }

        protected childrenCreated() {
            // 底部按钮响应函数
            this.btnMod.listener = (msg) => {
                this.onTouchBottomBtn(msg);
            };
        }

        protected onEnable() {
            this.hallQuickBtn.touchEnabled = true;
            this.ctrl.onRegister();
            this.playQuick();

            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTap, this);
            this.hallBackBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
            this.hallKefuBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onKefu, this);
            this.hallQuickBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onQuick, this);
            this.headMod.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
            if(!App.DataCenter.debugInfo.skipNet)this.headMod.updatePersonalInfo();

            this.ctrl.sendRoomNum();
        }

        protected onRemove() {
            this.ctrl.onRemove();

            this.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTap, this);
            this.hallBackBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
            this.hallKefuBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onKefu, this);
            this.hallQuickBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onQuick, this);
            this.headMod.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
        }

        /**
         * 点击大厅任意位置响应
         */
        private onTap(evt: egret.Event) {
            // 隐藏钻石UI
            if (evt.target != this.headMod.arrowGroup) {
                this.headMod.setDiamondVisible(false);
            }
        }

        /**
         * 点击退出
         */
        private onBack() {
            /**test */
            var msgBox = App.MessageBoxManager.getBox();
            msgBox.showMsg("您确定要退出游戏吗?",true);
            msgBox.ok = () => {
                this.ctrl.sendJieSanTest();
            }
        }

        /**
         * 点击快速开始
         */
        private onQuick() {
            this.hallQuickBtn.touchEnabled = false;
            setTimeout(()=>{
                this.hallQuickBtn.touchEnabled = true;
            }, 1000);
            this.ctrl.sendQuickBegin();
        }

        /**
         * 点击客服
         */
        private onKefu() {
            HallHttpDataSend.sendGetIncomeSupportMsg();
        }

        /**
         * 点击头像区域
         */
        private onHead() {

        }

        /**
         * 创建龙骨动画
         */
        private createQuickDb() {
            var factory: dragonBones.EgretFactory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes("tpm_NewProject_ske_json"));
            factory.parseTextureAtlasData(RES.getRes("tpm_NewProject_tex_json"), RES.getRes("tpm_NewProject_tex_png"));
            this.quickDb = factory.buildArmatureDisplay("Armature");
            this.moveGro.addChild(this.quickDb);
            this.quickDb.x = 1334/2;
            this.quickDb.y = 550-5;
        }

        /**播放快速开始动画 */
        private playQuick() {
            if (!this.quickDb) {
                this.createQuickDb();
            }
            this.quickDb.animation.play("kuaisukaishi", 0);
        }

        private onTouchBottomBtn(msg) {
            switch (msg) {
                case HallBtnMsg.playMethod:
                    App.PanelManager.open(PanelConst.PlayMethodPanel);
                    // App.PanelManager.open(PanelConst.MoneyNotEnoughPanel, false, null, null, true, true, ProtocolHttpData.MoneyNotEnoughData);
                    break;
                case HallBtnMsg.email:
                    // var emaildata = [];
                    // var emaildatalen = 5;
                    // for (var i = 0; i < emaildatalen; i++) {
                    //     var emailitemData = ProtocolHttpData.EmailListItemData;
                    //     emailitemData.icon="";
                    //     emailitemData.id = 1;
                    //     emailitemData.title = "500";
                    //     emailitemData.content = "5";
                    //     emailitemData.send_date = "5";
                    //     emaildata.push(emailitemData);
                    // }
                    // App.PanelManager.open(PanelConst.EmailPanel, false, null, null, true, true, emaildata);
                     HallHttpDataSend.sendGetEmailList();
                    break;
                case HallBtnMsg.share:
                    App.PanelManager.open(PanelConst.SharePanel);
                    break;
                case HallBtnMsg.shop:
                    //     var shopdata=[];
                    //     var shopdatalen=5;
                    //     	for (var i = 0; i < 5; i++) {
                    // 	var shopitemData = ProtocolHttpData.GoodsListItemData;
                    // 	shopitemData.id=1;
                    // 	shopitemData.selling_price=500;
                    // 	shopitemData.quantity=5;
                    // 	shopdata.push(shopitemData);
                    // }
                    //     App.PanelManager.open(PanelConst.ShopMallPanel,false,null,null,true,true,shopdata);
                    HallHttpDataSend.sendGetGoodsList();
                    break;
                case HallBtnMsg.set:
                    App.PanelManager.open(PanelConst.SetPanel);
                    break;
                default:
                    console.error("hallbtn error");
                    break;
            }
        }
    }
}