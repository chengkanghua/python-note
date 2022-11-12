module Tpm {
    export module Tips {
        /**
         * 中间获得提示
         */
        export function showMiddle(str: string) {
            _showMiddle(str);
        }

        /**
         * 顶部提示
         */
        export function showTop(str: string) {
            _showTop(str);
        }

        function _showTop(str: string) {
            var tipGro = new eui.Group();
            tipGro.width = App.StageUtils.stageWidth;
            tipGro.height = 100;
            tipGro.touchEnabled = false;
        
            var tipsBg = new eui.Image();
            tipsBg.texture = RES.getRes(ResPathConfig.tipsTopBg);
            tipsBg.horizontalCenter = 0;
            tipGro.y = -tipsBg.height;

            var showText = new eui.Label();
            showText.size = 30;
            showText.textColor = App.ArtConfig.getColor(ColorConst.topTips);
            showText.text = str;
            showText.horizontalCenter = 0;
            showText.y = (tipsBg.height-showText.size)/2-3;

            tipGro.addChild(tipsBg);
            tipGro.addChild(showText);

            if (App.LayerManager.getLayerChildrenNum(LayerConst.tipLayer) > 0) {
                egret.Tween.removeTweens(tipGro);
                App.LayerManager.removeLayerChirdren(LayerConst.tipLayer);
            }
            App.LayerManager.addChildToLayer(tipGro, LayerConst.tipLayer);

            var timeId = egret.setTimeout(() => {
                if (tipGro && tipGro.parent) {
                    App.LayerManager.removeChildFromLayer(tipGro, LayerConst.tipLayer);
                }
            }, this, 4000);

            egret.Tween.get(tipGro)
            .to({y: 0}, 200)
            .wait(2000)
            .to({y: -tipsBg.height, alpha: 0}, 300)
            .call(()=>{
                egret.clearTimeout(timeId);
                egret.Tween.removeTweens(tipGro);
                if (tipGro && tipGro.parent) {
                    App.LayerManager.removeChildFromLayer(tipGro, LayerConst.tipLayer);
                }
            })
        }

        function _showMiddle(str: string) {
            var tipGro = new eui.Group();
            tipGro.width = 1334;
            tipGro.height = 50;
            tipGro.y = 720 / 2 - 25;
            tipGro.alpha = 0;

            var tipsBg = new eui.Image();
            tipsBg.texture = RES.getRes(ResPathConfig.tipsBg);
            tipsBg.horizontalCenter = 0;

            var showText = new eui.Label();
            showText.size = 30;
            showText.textColor = App.ArtConfig.getColor(ColorConst.middleTips);
            showText.text = str;
            showText.horizontalCenter = 0;
            showText.y = 14;

            tipGro.addChild(tipsBg);
            tipGro.addChild(showText);

            if (App.LayerManager.getLayerChildrenNum(LayerConst.tipLayer) > 0) {
                egret.Tween.removeTweens(tipGro);
                App.LayerManager.removeLayerChirdren(LayerConst.tipLayer);
            }
            App.LayerManager.addChildToLayer(tipGro, LayerConst.tipLayer);

            var timeId = egret.setTimeout(() => {
                if (tipGro && tipGro.parent) {
                    App.LayerManager.removeChildFromLayer(tipGro, LayerConst.tipLayer);
                }
            }, this, 4000);

            egret.Tween.get(tipGro)
            .to({ alpha: 1 }, 200)
            .wait(1300)
            .to({ y: tipGro.y - 750 / 4, alpha: 0 }, 500)
            .call(() => {
                egret.clearTimeout(timeId);
                egret.Tween.removeTweens(tipGro);
                if (tipGro && tipGro.parent) {
                    App.LayerManager.removeChildFromLayer(tipGro, LayerConst.tipLayer);
                }
            })
        }
    }
}