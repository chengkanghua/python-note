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
    var SelectActBtn = (function (_super) {
        __extends(SelectActBtn, _super);
        function SelectActBtn() {
            var _this = _super.call(this) || this;
            _this.resList = [];
            _this.bInitRes = false;
            _this.skinName = TpmSkin.SelectActBtnSkin;
            return _this;
        }
        SelectActBtn.prototype.childrenCreated = function () {
            this.dbAmature = this.createDBArmature("tpm_NewProject_ske_json", "tpm_NewProject_tex_json", "tpm_NewProject_tex_png");
            this.touchRect.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        };
        SelectActBtn.prototype.onTouch = function () {
            console.log("touch rect");
            Tpm.App.SceneManager.getScene(Tpm.SceneConst.GameScene).selectBtnMod.onTouch(this.touchRect);
        };
        Object.defineProperty(SelectActBtn.prototype, "sortWeight", {
            /**排序权值 */
            get: function () {
                return this._sortWeight;
            },
            enumerable: true,
            configurable: true
        });
        SelectActBtn.prototype.initRes = function () {
            if (this.bInitRes == false) {
                this.bInitRes = true;
                var head = "annui_";
                this.resList[Tpm.ACT_act.Act_Pass] = "actBtnGuo";
                this.resList[Tpm.ACT_act.Act_Chi] = head + "chi_erren";
                this.resList[Tpm.ACT_act.Act_Peng] = head + "peng_erren";
                this.resList[Tpm.ACT_act.Act_Gang] = head + "gang_erren";
                this.resList[Tpm.ACT_act.Act_AnGang] = head + "gang_erren";
                this.resList[Tpm.ACT_act.Act_Hu] = head + "hu_erren";
                this.resList[Tpm.ACT_act.Act_Guohu] = head + "guohujiabei_erren";
                this.resList[Tpm.ACT_act.Act_cancle] = "actBtnCancle";
                this.resList[Tpm.ACT_act.Act_Ting] = head + "ting_erren";
            }
        };
        /**
         * 根据动作创建MovieClip或图片
         */
        SelectActBtn.prototype.setNewActSkin = function (act) {
            this.initRes();
            var resName = this.resList[act];
            this.dbKey = act;
            if (act == Tpm.ACT_act.Act_Pass || act == Tpm.ACT_act.Act_cancle) {
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
        };
        SelectActBtn.prototype.setSortWeight = function (act) {
            var weight = 0;
            switch (act) {
                case Tpm.ACT_act.Act_Chi:
                    weight = 10;
                    break;
                case Tpm.ACT_act.Act_Peng:
                    weight = 20;
                    break;
                case Tpm.ACT_act.Act_Gang:
                    weight = 30;
                    break;
                case Tpm.ACT_act.Act_AnGang:
                    weight = 40;
                    break;
                case Tpm.ACT_act.Act_Hu:
                    weight = 50;
                    break;
                case Tpm.ACT_act.Act_Ting:
                    weight = 55;
                    break;
                case Tpm.ACT_act.Act_Guohu:
                    weight = 60;
                    break;
                case Tpm.ACT_act.Act_Pass:
                    weight = 70;
                    break;
                case Tpm.ACT_act.Act_cancle:
                    weight = 80;
                    break;
                default:
                    break;
            }
            this._sortWeight = weight;
        };
        /**播放动画*/
        SelectActBtn.prototype.playAnim = function () {
            if (this.dbName && this.dbAmature.animation) {
                this.dbAmature.animation.play(this.dbName, 0);
            }
        };
        /**暂停播放 */
        SelectActBtn.prototype.stopAnim = function () {
            if (this.dbName && this.dbAmature.animation) {
                this.dbAmature.animation.stop();
            }
        };
        SelectActBtn.prototype.createDBArmature = function (dbJson, tetJson, tetPng) {
            var factory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes(dbJson));
            factory.parseTextureAtlasData(RES.getRes(tetJson), RES.getRes(tetPng));
            var ar = factory.buildArmatureDisplay("Armature");
            return ar;
        };
        return SelectActBtn;
    }(eui.Component));
    Tpm.SelectActBtn = SelectActBtn;
    __reflect(SelectActBtn.prototype, "Tpm.SelectActBtn");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=SelectActBtn.js.map