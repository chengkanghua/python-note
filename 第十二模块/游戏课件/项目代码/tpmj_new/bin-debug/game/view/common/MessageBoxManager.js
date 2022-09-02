var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * 消息弹出框管理类
 * @author chenkai
 * @date 2016/7/22
 */
var Tpm;
(function (Tpm) {
    var MessageBoxManager = (function (_super) {
        __extends(MessageBoxManager, _super);
        function MessageBoxManager() {
            var _this = _super.call(this) || this;
            _this.boxPool = Tpm.ObjectPool.getPool(Tpm.MessageBox.NAME);
            return _this;
        }
        /**获取一个消息弹框A，有确定和取消按钮 */
        MessageBoxManager.prototype.getBox = function () {
            var box = this.boxPool.getObject();
            box.skinName = "TpmSkin.MessageBoxSkin";
            return box;
        };
        // /**获取一个消息弹框B，只有确定按钮 */
        // public getBoxB():MessageBox{
        // 	var box:MessageBox = this.boxPool.getObject();
        // 	box.skinName = "TpmSkin.MessageBoxBSkin";
        // 	return box;
        // }
        // /**获取一个消息弹框C, 无任何按钮*/
        // public getBoxC():MessageBox{
        //     var box: MessageBox = this.boxPool.getObject();
        //     box.skinName = "TpmSkin.MessageBoxCSkin";
        //     return box;
        // }
        // /**获取一个消息弹框A，有确定和取消按钮 */
        // public getBoxD(): MessageBox {
        //     var box: MessageBox = this.boxPool.getObject();
        //     box.skinName = "TpmSkin.MessageBoxDSkin";
        //     return box;
        // }
        /**回收 */
        MessageBoxManager.prototype.recycle = function (msgBox) {
            this.boxPool.returnObject(msgBox);
        };
        /**回收所有弹框*/
        MessageBoxManager.prototype.recycleAllBox = function () {
            var layer = Tpm.App.LayerManager.msgLayer;
            var len = layer.numChildren;
            for (var i = len - 1; i >= 0; i--) {
                var box = layer.getChildAt(i);
                if (box && box instanceof Tpm.MessageBox) {
                    box.hideAndRecycle();
                }
            }
        };
        return MessageBoxManager;
    }(Tpm.SingleClass));
    Tpm.MessageBoxManager = MessageBoxManager;
    __reflect(MessageBoxManager.prototype, "Tpm.MessageBoxManager");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=MessageBoxManager.js.map