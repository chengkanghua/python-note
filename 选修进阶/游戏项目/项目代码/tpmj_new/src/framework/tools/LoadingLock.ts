module Tpm {
    export class LoadingLock extends SingleClass{
        private lockNum: number;
        private lockBg: eui.Rect;
        private circle: eui.Image;
        private descLab: eui.Label;
        private timeOutIndex: number;

        constructor() {
            super();

            this.lockNum = 0;

            this.lockBg = new eui.Rect();
            this.lockBg.width = 1334;
            this.lockBg.height = 750;
            this.lockBg.fillAlpha = 0.5;

            this.circle = new eui.Image();
            this.circle.source = Tpm.ResPathConfig.lockRotat;
            this.circle.anchorOffsetX = this.circle.width / 2;
            this.circle.anchorOffsetY = this.circle.height / 2;
            this.circle.verticalCenter = 0;
            this.circle.horizontalCenter = 0;

            this.descLab = new eui.Label();
            this.descLab.verticalCenter = 50;
            this.descLab.horizontalCenter = 0;
            this.descLab.textColor = App.ArtConfig.getColor(ColorConst.white);
            this.descLab.text = "";
            this.descLab.fontFamily = App.ArtConfig.getFont(FontConst.Microsoft);
        }

        public addLock(desc: string = "") {
            if (this.lockNum < 0) {
                this.lockNum = 0;
            }
            this.lockNum++;
            egret.Tween.removeTweens(this.circle);
            this.descLab.text = desc;
            egret.Tween.get(this.circle, { loop: true }).to({ rotation: 360 }, 1000)
            App.LayerManager.addChildToLayer(this.lockBg, LayerConst.lockLayer);
            App.LayerManager.addChildToLayer(this.circle, LayerConst.lockLayer);
            App.LayerManager.addChildToLayer(this.descLab, LayerConst.lockLayer);
        }

        public minusLock() {
            this.lockNum--;
            if (this.lockNum <= 0 && this.circle && this.circle.parent) {
                egret.Tween.removeTweens(this.circle);
                App.LayerManager.removeChildFromLayer(this.lockBg, LayerConst.lockLayer);
                App.LayerManager.removeChildFromLayer(this.circle, LayerConst.lockLayer);
                App.LayerManager.removeChildFromLayer(this.descLab, LayerConst.lockLayer);
            }
        }
    }
}