module Tpm {
    export class BaseUI extends eui.Component {
        public constructor() {
            super();
            this.addEventListener(egret.Event.ADDED_TO_STAGE, this.onEnable, this);
            this.addEventListener(egret.Event.REMOVED_FROM_STAGE, this.onRemove, this);
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, (e: egret.TouchEvent) => {
                if (e.target instanceof eui.Button) {
                    //按钮声音统一的话，在此播放
                    App.SoundManager.playEffect(SoundManager.button);
                }
            }, this)
        }

        /**组件创建完毕*/
        protected childrenCreated() {

        }

        /**添加到场景中*/
        protected onEnable() {

        }

        /**从场景中移除*/
        protected onRemove() {

        }

        /**销毁*/
        protected onDestroy() {

        }

        /**隐藏*/
        public hide() {
            this.parent && this.parent.removeChild(this);
        }
    }
}
