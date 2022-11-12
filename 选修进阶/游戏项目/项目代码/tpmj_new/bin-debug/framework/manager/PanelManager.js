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
    var PanelManager = (function (_super) {
        __extends(PanelManager, _super);
        function PanelManager() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            /**弹框*/
            _this.panelList = {};
            /**弹框类定义*/
            _this.panelClassList = {};
            /**资源组*/
            _this.assetList = {};
            return _this;
        }
        /**
         * 注册弹框
         * @panelID 弹框ID
         * @panelClass 弹框类定义
         * @group 资源组名(支持字符串和数组)
         */
        PanelManager.prototype.register = function (panelID, panelClass, group) {
            if (group === void 0) { group = null; }
            this.panelClassList[panelID] = panelClass;
            this.assetList[panelID] = group;
        };
        /**
         * 注册所有弹框
         */
        PanelManager.prototype.registerAll = function () {
            for (var key in Tpm.PanelConst) {
                var panelID = Number(key);
                var panelClass = egret.getDefinitionByName("Tpm." + Tpm.PanelConst[key]);
                this.register(panelID, panelClass);
            }
        };
        /**
         * 打开弹框
         * @panelID 弹框ID
         * @gameBool 是否在游戏场内打开Panel
         * @callBack 打开后回调(需要加载资源时，在加载完成后回调)
         * @thisObject 执行环境
         * @return 弹框
       * @click 是否监听点击黑色背景关闭弹框事件
       * @lock 是否弹出透明遮罩
       * @transData 传递给Panel的参数
       * @clickCallback click为true时点击黑色背景回调
         */
        PanelManager.prototype.open = function (panelID, gameBool, callBack, thisObject, click, lock, transData, clickCallback) {
            var _this = this;
            if (gameBool === void 0) { gameBool = false; }
            if (callBack === void 0) { callBack = null; }
            if (thisObject === void 0) { thisObject = null; }
            if (click === void 0) { click = true; }
            if (lock === void 0) { lock = true; }
            if (transData === void 0) { transData = null; }
            if (clickCallback === void 0) { clickCallback = null; }
            console.log("open Panel==" + panelID);
            var panel = this.panelList[panelID];
            if (panel == null) {
                var clz = this.panelClassList[panelID];
                if (clz != null) {
                    panel = new clz();
                    this.panelList[panelID] = panel;
                }
                else {
                    return null;
                }
            }
            if (gameBool)
                Tpm.App.PopUpManager.changeTransparency(0.5);
            else
                Tpm.App.PopUpManager.changeTransparency(0.8);
            /**接收参数 */
            if (transData != null) {
                panel.recDataFun(transData);
            }
            //加载弹框所需资源后，再打开弹框
            var group = this.assetList[panelID];
            if (group != null) {
                Tpm.App.LoadingLock.addLock();
                Tpm.App.ResUtils.loadGroup(group, this, function () {
                    Tpm.App.LoadingLock.minusLock();
                    if (callBack != null && thisObject != null) {
                        panel.once(egret.Event.ADDED_TO_STAGE, function () {
                            callBack.call(thisObject, true);
                        }, _this);
                    }
                    panel.show(lock, click);
                }, null, 10);
            }
            else {
                if (callBack != null && thisObject != null) {
                    panel.once(egret.Event.ADDED_TO_STAGE, function () {
                        callBack.call(thisObject);
                    }, this);
                }
                panel.show(lock, click);
            }
            return panel;
        };
        /**
         * 关闭弹框
         * @panelID 弹框ID
         * @return 弹框
         */
        PanelManager.prototype.close = function (panelID) {
            var panel = this.panelList[panelID];
            if (panel != null) {
                panel.hide();
            }
            return panel;
        };
        /**
         * 获取弹框
         * @panelID 弹框ID
         */
        PanelManager.prototype.getPanel = function (panelID) {
            return this.panelList[panelID];
        };
        /**
         * 移除所有弹框
         */
        PanelManager.prototype.closeAllPanel = function () {
            Tpm.App.ResUtils.deleteAllCallBack(); //防止当有弹框加载时，调用了该函数，加载完成后仍然会显示弹框
            Tpm.App.PopUpManager.removeAllPopUp();
            Tpm.App.LoadingLock.minusLock();
        };
        return PanelManager;
    }(Tpm.SingleClass));
    Tpm.PanelManager = PanelManager;
    __reflect(PanelManager.prototype, "Tpm.PanelManager");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PanelManager.js.map