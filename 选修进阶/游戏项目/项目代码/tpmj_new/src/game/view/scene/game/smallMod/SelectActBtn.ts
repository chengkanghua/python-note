module Tpm {
    export class SelectActBtn extends eui.Component {
        private resList = [];
        private bInitRes: boolean = false;

        private img: eui.Image;
        private _sortWeight : number;
        private btnGro:eui.Group;
        private dbAmature: dragonBones.EgretArmatureDisplay;
        private dbName: string;
        private touchRect: eui.Rect;
        private dbKey: ACT_act;

        public constructor() {
            super();
            this.skinName = TpmSkin.SelectActBtnSkin;
        }

        public childrenCreated() {
            this.dbAmature = this.createDBArmature("tpm_NewProject_ske_json", "tpm_NewProject_tex_json", "tpm_NewProject_tex_png");
            this.touchRect.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        }

        private onTouch() {
            console.log("touch rect");
            (<GameScene>App.SceneManager.getScene(SceneConst.GameScene)).selectBtnMod.onTouch(this.touchRect);
        }

        /**排序权值 */
        public get sortWeight() {
            return this._sortWeight;
        }

        private initRes() {
            if (this.bInitRes == false) {
                this.bInitRes = true;
                var head = "annui_";
                this.resList[ACT_act.Act_Pass] = "actBtnGuo";
                this.resList[ACT_act.Act_Chi] = head+"chi_erren";
                this.resList[ACT_act.Act_Peng] = head+"peng_erren";
                this.resList[ACT_act.Act_Gang] = head+"gang_erren";
                this.resList[ACT_act.Act_AnGang] = head+"gang_erren";
                this.resList[ACT_act.Act_Hu] = head+"hu_erren";
                this.resList[ACT_act.Act_Guohu] = head+"guohujiabei_erren";
                this.resList[ACT_act.Act_cancle] = "actBtnCancle";
                this.resList[ACT_act.Act_Ting] = head+"ting_erren";
            }
        }

        /**
         * 根据动作创建MovieClip或图片
         */
        public setNewActSkin(act: ACT_act) {
            this.initRes();
            var resName = this.resList[act];
            this.dbKey = act;

            if (act == ACT_act.Act_Pass || act == ACT_act.Act_cancle) {
                this.img = new eui.Image("tpm_" + resName + "_png");
                this.img.x = 19;
                this.img.y = 19;
                this.btnGro.addChild(this.img);
            }
            else {
                this.dbName = resName;
                this.dbAmature.x = 75;
                this.dbAmature.y = 75;
                this.dbAmature.touchEnabled = false;
                this.btnGro.addChild(this.dbAmature);
            }

            this.setSortWeight(act);
        }

        public setSortWeight(act: ACT_act) {
            var weight = 0;
            switch (act) {
                case ACT_act.Act_Chi:
                    weight = 10;
                    break;
                case ACT_act.Act_Peng:
                    weight = 20;
                    break;
                case ACT_act.Act_Gang:
                    weight = 30;
                    break;
                case ACT_act.Act_AnGang:
                    weight = 40;
                    break;
                case ACT_act.Act_Hu:
                    weight = 50;
                    break;
                case ACT_act.Act_Ting:
                    weight = 55;
                    break;
                case ACT_act.Act_Guohu:
                    weight = 60;
                    break;
                case ACT_act.Act_Pass:
                    weight = 70;
                    break;
                case ACT_act.Act_cancle:
                    weight = 80;
                    break;
                default:
                    break;
            }
            this._sortWeight = weight;
        }

        /**播放动画*/
        public playAnim() {
            if (this.dbName && this.dbAmature.animation) {
                this.dbAmature.animation.play(this.dbName, 0);
            }
        }

        /**暂停播放 */
        public stopAnim() {
            if (this.dbName && this.dbAmature.animation) {
                this.dbAmature.animation.stop();
            }
        }

        private createDBArmature(dbJson: string, tetJson: string, tetPng: string): dragonBones.EgretArmatureDisplay {
            var factory: dragonBones.EgretFactory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes(dbJson));
            factory.parseTextureAtlasData(RES.getRes(tetJson), RES.getRes(tetPng));
            var ar: dragonBones.EgretArmatureDisplay = factory.buildArmatureDisplay("Armature");
            return ar;
        }
    }
}