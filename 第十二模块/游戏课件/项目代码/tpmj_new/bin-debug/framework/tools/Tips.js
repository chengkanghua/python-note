var Tpm;
(function (Tpm) {
    var Tips;
    (function (Tips) {
        /**
         * 中间获得提示
         */
        function showMiddle(str) {
            _showMiddle(str);
        }
        Tips.showMiddle = showMiddle;
        /**
         * 顶部提示
         */
        function showTop(str) {
            _showTop(str);
        }
        Tips.showTop = showTop;
        function _showTop(str) {
            var tipGro = new eui.Group();
            tipGro.width = Tpm.App.StageUtils.stageWidth;
            tipGro.height = 100;
            tipGro.touchEnabled = false;
            var tipsBg = new eui.Image();
            tipsBg.texture = RES.getRes(Tpm.ResPathConfig.tipsTopBg);
            tipsBg.horizontalCenter = 0;
            tipGro.y = -tipsBg.height;
            var showText = new eui.Label();
            showText.size = 30;
            showText.textColor = Tpm.App.ArtConfig.getColor(Tpm.ColorConst.topTips);
            showText.text = str;
            showText.horizontalCenter = 0;
            showText.y = (tipsBg.height - showText.size) / 2 - 3;
            tipGro.addChild(tipsBg);
            tipGro.addChild(showText);
            if (Tpm.App.LayerManager.getLayerChildrenNum(Tpm.LayerConst.tipLayer) > 0) {
                egret.Tween.removeTweens(tipGro);
                Tpm.App.LayerManager.removeLayerChirdren(Tpm.LayerConst.tipLayer);
            }
            Tpm.App.LayerManager.addChildToLayer(tipGro, Tpm.LayerConst.tipLayer);
            var timeId = egret.setTimeout(function () {
                if (tipGro && tipGro.parent) {
                    Tpm.App.LayerManager.removeChildFromLayer(tipGro, Tpm.LayerConst.tipLayer);
                }
            }, this, 4000);
            egret.Tween.get(tipGro)
                .to({ y: 0 }, 200)
                .wait(2000)
                .to({ y: -tipsBg.height, alpha: 0 }, 300)
                .call(function () {
                egret.clearTimeout(timeId);
                egret.Tween.removeTweens(tipGro);
                if (tipGro && tipGro.parent) {
                    Tpm.App.LayerManager.removeChildFromLayer(tipGro, Tpm.LayerConst.tipLayer);
                }
            });
        }
        function _showMiddle(str) {
            var tipGro = new eui.Group();
            tipGro.width = 1334;
            tipGro.height = 50;
            tipGro.y = 720 / 2 - 25;
            tipGro.alpha = 0;
            var tipsBg = new eui.Image();
            tipsBg.texture = RES.getRes(Tpm.ResPathConfig.tipsBg);
            tipsBg.horizontalCenter = 0;
            var showText = new eui.Label();
            showText.size = 30;
            showText.textColor = Tpm.App.ArtConfig.getColor(Tpm.ColorConst.middleTips);
            showText.text = str;
            showText.horizontalCenter = 0;
            showText.y = 14;
            tipGro.addChild(tipsBg);
            tipGro.addChild(showText);
            if (Tpm.App.LayerManager.getLayerChildrenNum(Tpm.LayerConst.tipLayer) > 0) {
                egret.Tween.removeTweens(tipGro);
                Tpm.App.LayerManager.removeLayerChirdren(Tpm.LayerConst.tipLayer);
            }
            Tpm.App.LayerManager.addChildToLayer(tipGro, Tpm.LayerConst.tipLayer);
            var timeId = egret.setTimeout(function () {
                if (tipGro && tipGro.parent) {
                    Tpm.App.LayerManager.removeChildFromLayer(tipGro, Tpm.LayerConst.tipLayer);
                }
            }, this, 4000);
            egret.Tween.get(tipGro)
                .to({ alpha: 1 }, 200)
                .wait(1300)
                .to({ y: tipGro.y - 750 / 4, alpha: 0 }, 500)
                .call(function () {
                egret.clearTimeout(timeId);
                egret.Tween.removeTweens(tipGro);
                if (tipGro && tipGro.parent) {
                    Tpm.App.LayerManager.removeChildFromLayer(tipGro, Tpm.LayerConst.tipLayer);
                }
            });
        }
    })(Tips = Tpm.Tips || (Tpm.Tips = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=Tips.js.map