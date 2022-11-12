module Tpm {
    /**
     * 龙骨动画模块
     */
    export class GameDbMod extends BaseUI {
        private dbAmaureList:Array<dragonBones.EgretArmatureDisplay>;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameDbModSkin;
        }

        protected childrenCreated() {
            this.dbAmaureList = this.createDBArmatureList("tpm_NewProject_ske_json", "tpm_NewProject_tex_json", "tpm_NewProject_tex_png");
        }

        protected onEnable() {
        }

        protected onRemove() {
            
        }

        /**
         * 显示对应动作的龙骨动画
         */
        public showActDb(act: ACT_state, pos: UserPosition) {
            switch (act) {
                case ACT_state.Act_Chi:
                    this.showDB("chi_erren", pos);
                    break;
                case ACT_state.Act_Peng:
                    this.showDB("peng_erren", pos);
                    break;
                case ACT_state.Act_Gang:
                    this.showDB("gang_erren", pos);
                    break;
                case ACT_state.Act_AnGang:
                    this.showDB("gang_erren", pos);
                    break;
                case ACT_state.Act_BuGang:
                    this.showDB("gang_erren", pos);
                    break;
                case ACT_state.Act_DianHu:
                    this.showDB("hu__erren", pos);
                    break;
                case ACT_state.Act_Zimo:
                    this.showDB("hu__erren", pos);
                    break;
                case ACT_state.Act_Buhua:
                    this.showDB("BuHua", pos);
                    break;
                case ACT_state.Act_Guohu:
                    this.showDB("guohu_erren", pos);
                    break;
                case ACT_state.Act_Ting:
                    this.showDB("ting_erren", pos);
                    break;
                default:
                    console.error("act error db");
                    break;
            }
        }

        private showDB(name: string, pos: number) {
            var offsetListX = [0,0];
            var offsetLIstY = [170,-250];
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
        }

        private createDBArmatureList(dbJson: string, tetJson: string, tetPng: string): Array<dragonBones.EgretArmatureDisplay> {
            var factory: dragonBones.EgretFactory = new dragonBones.EgretFactory;
            factory.parseDragonBonesData(RES.getRes(dbJson));
            factory.parseTextureAtlasData(RES.getRes(tetJson), RES.getRes(tetPng));
            var list = [];
            for (var i = 0; i < 2; i++) {
                var ar: dragonBones.EgretArmatureDisplay = factory.buildArmatureDisplay("Armature");
                list.push(ar);
            }
            return list;
        }
    }
}