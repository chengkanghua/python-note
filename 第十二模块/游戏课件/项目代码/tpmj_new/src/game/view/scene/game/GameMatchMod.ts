module Tpm {
    export class GameMatchMod extends BaseUI {
        private matchGro:eui.Group;
        private circleImg:eui.Image;
        private reMatchGro:eui.Group;
        private circleImgRe:eui.Image;
        private jieSanGro:eui.Group;


        // 当前类型下，对应的圈圈
        private curentCircleImg: eui.Image;
        private uiType: MatchType;

        public constructor() {
            super();
            this.skinName = TpmSkin.GameMatchModSkin;
        }

        protected childrenCreated() {
        }

        protected onEnable() {

        }

        protected onRemove() {
            this.removeCircleTween();
        }

        /**
         * 设置类型、倒计时时间,并更新相关UI
         */
        public setType(type: MatchType) {
            this.uiType = type;
            this.removeCircleTween();
            switch (this.uiType) {
                case MatchType.common:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = false;
                    break;
                case MatchType.match:
                    this.matchGro.visible = true;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = false;
                    this.curentCircleImg = this.circleImg;
                    this.circleRound();
                    break;
                case MatchType.jieSan:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = false;
                    this.jieSanGro.visible = true;
                    this.curentCircleImg = null;
                    break;
                case MatchType.reMatch:
                    this.matchGro.visible = false;
                    this.reMatchGro.visible = true;
                    this.jieSanGro.visible = false;
                    this.curentCircleImg = this.circleImgRe;
                    this.circleRound();
                    break;
                default:
                    console.error("type error");
                    break;
            }
        }

        /**
         * 转圈圈
         */
        private circleRound() {
            egret.Tween.get(this.curentCircleImg, {loop: true}).to({rotation: 360}, 1000);
        }

        private removeCircleTween() {
            this.curentCircleImg && egret.Tween.removeTweens(this.curentCircleImg);
        }
    }

    /**
     * MatchMod的显示类型
     */
    export enum MatchType {
        common,
        match,
        jieSan,
        reMatch
    }
}