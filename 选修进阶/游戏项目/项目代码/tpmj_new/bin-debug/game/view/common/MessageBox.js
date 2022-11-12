var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * 消息提示框
 * @author chenkai
 * @date 2016/7/20
 */
var Tpm;
(function (Tpm) {
    var MessageBox = (function (_super) {
        __extends(MessageBox, _super);
        function MessageBox() {
            var _this = _super.call(this) || this;
            _this.touchEnabled = true;
            return _this;
        }
        /**
         * 将msgBox显示到弹框层，并显示提示信息
         * @param msg 信息
         */
        MessageBox.prototype.showMsg = function (msg, blackBg, okCallback, thisObject, cancelCallback) {
            if (blackBg === void 0) { blackBg = false; }
            if (okCallback === void 0) { okCallback = null; }
            if (thisObject === void 0) { thisObject = null; }
            if (cancelCallback === void 0) { cancelCallback = null; }
            this.ok = okCallback;
            this.thisObject = thisObject;
            this.cancel = cancelCallback;
            this.blackBg.visible = blackBg;
            if (this.parent == null) {
                Tpm.App.LayerManager.msgLayer.addChild(this);
                this.x = (Tpm.App.StageUtils.stageWidth - this.width) / 2;
                this.y = (Tpm.App.StageUtils.stageHeight - this.height) / 2;
            }
            this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            //关闭按钮
            this.cancelBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.closeBt, this);
            this.msgLabel.text = msg;
        };
        MessageBox.prototype.onTouch = function (e) {
            switch (e.target) {
                case this.sureBtn:
                    this.ok && (this.ok.call(this.thisObject));
                    this.hideAndRecycle();
                    break;
                case this.cancelBtn || this.close:
                    this.cancel && (this.cancel.call(this.thisObject));
                    this.hideAndRecycle();
                    break;
            }
        };
        /**关闭按钮的相应 */
        MessageBox.prototype.closeBt = function () {
            this.hideAndRecycle();
        };
        /**左边按钮文字 */
        MessageBox.prototype.leftTitle = function (label) {
            this.cancelBtn.label = label;
        };
        /**中间按钮文字 */
        MessageBox.prototype.centerTitle = function (label) {
            this.sureBtn.label = label;
        };
        /**右边按钮文字 */
        MessageBox.prototype.rightTitle = function (label) {
            this.sureBtn.label = label;
        };
        //隐藏并回收消息框
        MessageBox.prototype.hideAndRecycle = function () {
            egret.Tween.removeTweens(this);
            this.ok = null;
            this.cancel = null;
            this.thisObject = null;
            this.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
            this.cancelBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.closeBt, this);
            this.hide();
        };
        //隐藏
        MessageBox.prototype.hide = function () {
            this.parent && this.parent.removeChild(this);
        };
        return MessageBox;
    }(eui.Component));
    MessageBox.NAME = "MessageBox";
    Tpm.MessageBox = MessageBox;
    __reflect(MessageBox.prototype, "Tpm.MessageBox");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=MessageBox.js.map