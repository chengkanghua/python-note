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
    var LayerConst;
    (function (LayerConst) {
        LayerConst[LayerConst["sceneLayer"] = 0] = "sceneLayer";
        LayerConst[LayerConst["popLayer"] = 1] = "popLayer";
        LayerConst[LayerConst["msgLayer"] = 2] = "msgLayer";
        LayerConst[LayerConst["lockLayer"] = 3] = "lockLayer";
        LayerConst[LayerConst["tipLayer"] = 4] = "tipLayer";
    })(LayerConst = Tpm.LayerConst || (Tpm.LayerConst = {}));
    var LayerManager = (function (_super) {
        __extends(LayerManager, _super);
        function LayerManager() {
            var _this = _super.call(this) || this;
            _this.rootLayer = new eui.UILayer();
            _this.rootLayer.percentWidth = 100;
            _this.rootLayer.percentHeight = 100;
            _this.rootLayer.touchEnabled = false;
            Tpm.App.StageUtils.stage.addChild(_this.rootLayer);
            _this.sceneLayer = new eui.UILayer();
            _this.sceneLayer.touchEnabled = false;
            _this.rootLayer.addChild(_this.sceneLayer);
            _this.popLayer = new eui.UILayer();
            _this.popLayer.touchEnabled = false;
            _this.rootLayer.addChild(_this.popLayer);
            _this.lockLayer = new eui.UILayer();
            _this.lockLayer.touchEnabled = false;
            _this.rootLayer.addChild(_this.lockLayer);
            _this.msgLayer = new eui.UILayer();
            _this.msgLayer.touchEnabled = false;
            _this.rootLayer.addChild(_this.msgLayer);
            _this.tipLayer = new eui.UILayer();
            _this.tipLayer.touchEnabled = false;
            _this.rootLayer.addChild(_this.tipLayer);
            _this.layerList = [_this.sceneLayer, _this.popLayer, _this.lockLayer, _this.msgLayer, _this.tipLayer];
            return _this;
        }
        /**
         * 添加component至指定Layer
         */
        LayerManager.prototype.addChildToLayer = function (child, layer) {
            if (!this.layerList[layer] || !child) {
                console.log("add to layer fault");
                return;
            }
            this.layerList[layer].addChild(child);
        };
        /**
         * 从指定Layer中移除某个子项
         */
        LayerManager.prototype.removeChildFromLayer = function (child, layer) {
            if (!this.layerList[layer] || !child) {
                console.log("remove from layer fault");
                return;
            }
            this.layerList[layer].removeChild(child);
        };
        /**
         * poplayer调整弹窗背景层级
         */
        LayerManager.prototype.adjustIndex = function (lockBg) {
            this.popLayer.setChildIndex(lockBg, this.popLayer.numChildren - 2);
        };
        /**
         * 移除某个Lyaer所有子项
         * 谨慎操作popLayer
         */
        LayerManager.prototype.removeLayerChirdren = function (layer) {
            this.layerList[layer].removeChildren();
        };
        /**
         * 获取某个Layer子项数目
         */
        LayerManager.prototype.getLayerChildrenNum = function (layer) {
            return this.layerList[layer].numChildren;
        };
        Object.defineProperty(LayerManager.prototype, "RootLayer", {
            /**
             * 获取根节点；全局事件监听
             */
            get: function () {
                return this.rootLayer;
            },
            enumerable: true,
            configurable: true
        });
        return LayerManager;
    }(Tpm.SingleClass));
    Tpm.LayerManager = LayerManager;
    __reflect(LayerManager.prototype, "Tpm.LayerManager");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LayerManager.js.map