module Tpm {
    export enum LayerConst {
        sceneLayer,
        popLayer,
        msgLayer,
        lockLayer,
        tipLayer
    }

    export class LayerManager extends SingleClass {
        /**根容器*/
        private rootLayer: eui.UILayer;
        /**场景层*/
        private sceneLayer: eui.UILayer;
        /**弹框层*/
        private popLayer: eui.UILayer;
        /**消息层*/
        public msgLayer: eui.UILayer;
        /**锁定动画层*/
        private lockLayer: eui.UILayer;
        /**提示语层*/
        private tipLayer: eui.UILayer;

        private layerList: Array<eui.UILayer>;

        public constructor() {
            super();

            this.rootLayer = new eui.UILayer();
            this.rootLayer.percentWidth = 100;
            this.rootLayer.percentHeight = 100;
            this.rootLayer.touchEnabled = false;
            App.StageUtils.stage.addChild(this.rootLayer);

            this.sceneLayer = new eui.UILayer();
            this.sceneLayer.touchEnabled = false;
            this.rootLayer.addChild(this.sceneLayer);

            this.popLayer = new eui.UILayer();
            this.popLayer.touchEnabled = false;
            this.rootLayer.addChild(this.popLayer);

            this.lockLayer = new eui.UILayer();
            this.lockLayer.touchEnabled = false;
            this.rootLayer.addChild(this.lockLayer);

            this.msgLayer = new eui.UILayer();
            this.msgLayer.touchEnabled = false;
            this.rootLayer.addChild(this.msgLayer);

            this.tipLayer = new eui.UILayer();
            this.tipLayer.touchEnabled = false;
            this.rootLayer.addChild(this.tipLayer);

            this.layerList = [this.sceneLayer, this.popLayer, this.lockLayer, this.msgLayer, this.tipLayer];
        }

        /**
         * 添加component至指定Layer
         */
        public addChildToLayer(child: any, layer: LayerConst) {
            if (!this.layerList[layer] || !child) {
                console.log("add to layer fault");
                return;
            }
            this.layerList[layer].addChild(child);
        }

        /**
         * 从指定Layer中移除某个子项
         */
        public removeChildFromLayer(child: any, layer: LayerConst) {
            if (!this.layerList[layer] || !child) {
                console.log("remove from layer fault");
                return;
            }
            this.layerList[layer].removeChild(child);
        }

        /**
         * poplayer调整弹窗背景层级
         */
        public adjustIndex(lockBg:any) {
            this.popLayer.setChildIndex(lockBg, this.popLayer.numChildren - 2);
        }

        /**
         * 移除某个Lyaer所有子项
         * 谨慎操作popLayer
         */
        public removeLayerChirdren(layer: LayerConst) {
            this.layerList[layer].removeChildren();
        }

        /**
         * 获取某个Layer子项数目
         */
        public getLayerChildrenNum(layer: LayerConst) {
            return this.layerList[layer].numChildren;
        }

        /**
         * 获取根节点；全局事件监听
         */
        public get RootLayer() {
            return this.rootLayer;
        }
    }
}