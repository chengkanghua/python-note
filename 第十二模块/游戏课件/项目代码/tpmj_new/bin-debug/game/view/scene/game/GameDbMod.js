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
     * 龙骨动画模块
     */
    var GameDbMod = (function (_super) {
        __extends(GameDbMod, _super);
        function GameDbMod() {
            var _this = _super.call(this) || this;
            _this.skinName = TpmSkin.GameDbModSkin;
            return _this;
        }
        GameDbMod.prototype.childrenCreated = function () {
            this.dbAmaureList = this.createDBArmatureList("tpm_NewProject_ske_json", "tpm_NewProject_tex_json", "tpm_NewProject_tex_png");
        };
        GameDbMod.prototype.onEnable = function () {
        };
        GameDbMod.prototype.onRemove = function () {
        };
        /**
         * 显示对应动作的龙骨动画
         */
        GameDbMod.prototype.showActDb = function (act, pos) {
            switch (act) {
                case Tpm.ACT_state.Act_Chi:
                    this.showDB("chi_erren", pos);
                    break;
                case Tpm.ACT_state.Act_Peng:
                    this.showDB("peng_erren", pos);
                    break;
                case Tpm.ACT_state.Act_Gang:
                    this.showDB("gang_erren", pos);
                    break;
                case Tpm.ACT_state.Act_AnGang:
                    this.showDB("gang_erren", pos);
                    break;
                case Tpm.ACT_state.Act_BuGang:
                    this.showDB("gang_erren", pos);
                    break;
                case Tpm.ACT_state.Act_DianHu:
                    this.showDB("hu__erren", pos);
                    break;
                case Tpm.ACT_state.Act_Zimo:
                    this.showDB("hu__erren", pos);
                    break;
                case Tpm.ACT_state.Act_Buhua:
                    this.showDB("BuHua", pos);
                    break;
                case Tpm.ACT_state.Act_Guohu:
                    this.showDB("guohu_erren", pos);
                    break;
                case Tpm.ACT_state.Act_Ting:
                    this.showDB("ting_erren", pos);
                    break;
                default:
                    console.error("act error db");
                    break;
            }
        };
        GameDbMod.prototype.showDB = function (name, pos) {
            var offsetListX = [0, 0];
            var offsetLIstY = [170, -250];
            this.dbAmaureList[pos].y = 750 / 2 + offsetLIstY[pos];
            if (name == "BuHua") {
                this.dbAmaureList[pos].x = 1334 / 2 + offsetListX[pos] + 30;
            }
            else {
                this.dbAmaureList[pos].x = 1334 / 2 + offsetListX[pos];
            }
            if (!this.dbAmaureList[pos].parent) {
                this.addChild(this.dbAmaureList[pos]);
            }
            this.dbAmaureList[pos].animation.play(name, 1);
        };
        GameDbMod.prototype.createDBArmatureList = function (dbJson, tetJson, tetPng) {
            var factory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes(dbJson));
            factory.parseTextureAtlasData(RES.getRes(tetJson), RES.getRes(tetPng));
            var list = [];
            for (var i = 0; i < 2; i++) {
                var ar = factory.buildArmatureDisplay("Armature");
                list.push(ar);
            }
            return list;
        };
        return GameDbMod;
    }(Tpm.BaseUI));
    Tpm.GameDbMod = GameDbMod;
    __reflect(GameDbMod.prototype, "Tpm.GameDbMod");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=GameDbMod.js.map