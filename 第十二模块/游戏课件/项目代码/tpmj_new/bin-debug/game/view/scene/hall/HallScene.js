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
    var HallScene = (function (_super) {
        __extends(HallScene, _super);
        function HallScene() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.HallSceneSkin;
            return _this;
        }
        HallScene.prototype.childrenCreated = function () {
            var _this = this;
            // 底部按钮响应函数
            this.btnMod.listener = function (msg) {
                _this.onTouchBottomBtn(msg);
            };
        };
        HallScene.prototype.onEnable = function () {
            this.hallQuickBtn.touchEnabled = true;
            this.ctrl.onRegister();
            this.playQuick();
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTap, this);
            this.hallBackBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
            this.hallKefuBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onKefu, this);
            this.hallQuickBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onQuick, this);
            this.headMod.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
            if (!Tpm.App.DataCenter.debugInfo.skipNet)
                this.headMod.updatePersonalInfo();
            this.ctrl.sendRoomNum();
        };
        HallScene.prototype.onRemove = function () {
            this.ctrl.onRemove();
            this.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTap, this);
            this.hallBackBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onBack, this);
            this.hallKefuBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onKefu, this);
            this.hallQuickBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onQuick, this);
            this.headMod.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onHead, this);
        };
        /**
         * 点击大厅任意位置响应
         */
        HallScene.prototype.onTap = function (evt) {
            // 隐藏钻石UI
            if (evt.target != this.headMod.arrowGroup) {
                this.headMod.setDiamondVisible(false);
            }
        };
        /**
         * 点击退出
         */
        HallScene.prototype.onBack = function () {
            var _this = this;
            /**test */
            var msgBox = Tpm.App.MessageBoxManager.getBox();
            msgBox.showMsg("您确定要退出游戏吗?", true);
            msgBox.ok = function () {
                _this.ctrl.sendJieSanTest();
            };
        };
        /**
         * 点击快速开始
         */
        HallScene.prototype.onQuick = function () {
            var _this = this;
            this.hallQuickBtn.touchEnabled = false;
            setTimeout(function () {
                _this.hallQuickBtn.touchEnabled = true;
            }, 1000);
            this.ctrl.sendQuickBegin();
        };
        /**
         * 点击客服
         */
        HallScene.prototype.onKefu = function () {
            Tpm.HallHttpDataSend.sendGetIncomeSupportMsg();
        };
        /**
         * 点击头像区域
         */
        HallScene.prototype.onHead = function () {
        };
        /**
         * 创建龙骨动画
         */
        HallScene.prototype.createQuickDb = function () {
            var factory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes("tpm_NewProject_ske_json"));
            factory.parseTextureAtlasData(RES.getRes("tpm_NewProject_tex_json"), RES.getRes("tpm_NewProject_tex_png"));
            this.quickDb = factory.buildArmatureDisplay("Armature");
            this.moveGro.addChild(this.quickDb);
            this.quickDb.x = 1334 / 2;
            this.quickDb.y = 550 - 5;
        };
        /**播放快速开始动画 */
        HallScene.prototype.playQuick = function () {
            if (!this.quickDb) {
                this.createQuickDb();
            }
            this.quickDb.animation.play("kuaisukaishi", 0);
        };
        HallScene.prototype.onTouchBottomBtn = function (msg) {
            switch (msg) {
                case Tpm.HallBtnMsg.playMethod:
                    Tpm.App.PanelManager.open(Tpm.PanelConst.PlayMethodPanel);
                    // App.PanelManager.open(PanelConst.MoneyNotEnoughPanel, false, null, null, true, true, ProtocolHttpData.MoneyNotEnoughData);
                    break;
                case Tpm.HallBtnMsg.email:
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
                    Tpm.HallHttpDataSend.sendGetEmailList();
                    break;
                case Tpm.HallBtnMsg.share:
                    Tpm.App.PanelManager.open(Tpm.PanelConst.SharePanel);
                    break;
                case Tpm.HallBtnMsg.shop:
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
                    Tpm.HallHttpDataSend.sendGetGoodsList();
                    break;
                case Tpm.HallBtnMsg.set:
                    Tpm.App.PanelManager.open(Tpm.PanelConst.SetPanel);
                    break;
                default:
                    console.error("hallbtn error");
                    break;
            }
        };
        return HallScene;
    }(Tpm.BaseScene));
    Tpm.HallScene = HallScene;
    __reflect(HallScene.prototype, "Tpm.HallScene");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=HallScene.js.map