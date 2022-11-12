module Tpm {
    export class GameHeadMod extends BaseUI {
        private headMask: eui.Image;
        private headImg: eui.Image;
        private zhuangImg: eui.Image;
        private goldLab: eui.Label;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameHeadModSkin;
        }

        protected childrenCreated() {
            this.headImg.mask = this.headMask;
        }

        protected onEnable() {
            this.zhuangImg.visible = false;
            this.reGoldLab(0);
        }

        protected onRemove() {

        }

        /**根据UserInfo刷新头像状态 */
        public reHeadState(pos: UserPosition) {
            var user = App.DataCenter.UserInfo.getUserByPos(pos);
            if (user) {
                this.visible = true;
                this.reGoldLab(user.gold);
                this.reZhuangFlag(pos);
            }
            else {
                this.visible = false;
            }
        }

        /**设置庄家图片状态 */
        public reZhuangFlag(pos: UserPosition) {
            var user = App.DataCenter.UserInfo.getUserByPos(pos);
            if (user && user.zhuangFlag) {
                this.zhuangImg.visible = true;
            }
            else {
                this.zhuangImg.visible = false;
            }
        }

        /**设置金币数 */
        public reGoldLab(goldNumb: number) {
            this.goldLab.text = NumberTool.formatGoldHead(goldNumb);
        }
    }
}