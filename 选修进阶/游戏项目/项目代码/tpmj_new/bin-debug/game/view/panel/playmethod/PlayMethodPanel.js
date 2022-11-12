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
    var PlayMethodPanel = (function (_super) {
        __extends(PlayMethodPanel, _super);
        function PlayMethodPanel() {
            var _this = _super.call(this) || this;
            _this.contentList = []; //文本组件列表
            _this.styleList = []; //文本格式列表
            _this.skinName = TpmSkin.PlayMethodPanelSkin;
            return _this;
        }
        /**添加到场景中*/
        PlayMethodPanel.prototype.onEnable = function () {
            // this.playMethodtabBar.selectedIndex
            this.showTargetScroller(0, true);
            this.setContenTex();
            this.setFanType();
            this.playMethodtabBar.addEventListener(egret.TouchEvent.TOUCH_TAP, this.showPlayMethod, this);
            this.closeBtn.addEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**从场景中移除*/
        PlayMethodPanel.prototype.onRemove = function () {
            this.playMethodtabBar.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.showPlayMethod, this);
            this.closeBtn.removeEventListener(egret.TouchEvent.TOUCH_TAP, this.hide, this);
        };
        /**销毁*/
        PlayMethodPanel.prototype.onDestory = function () {
            this.removeChildren();
        };
        PlayMethodPanel.prototype.showPlayMethod = function (e) {
            this.showTargetScroller(this.playMethodtabBar.selectedIndex);
        };
        /**
        * 格式化内容文本
        */
        PlayMethodPanel.prototype.setContenTex = function () {
            if (this.textIsInt)
                return;
            //"fontFamily":"楷体"
            var tetleTextStyleJson = { "size": 27.2, "textColor": 0x370b00, "fontFamily": "SimHei", "bold": "true" };
            var contentTextStyleJson = { "size": 26.2, "textColor": 0x370b00, "fontFamily": "SimHei" };
            this.contentList = [this.baseRuleText, this.tsRuleText, this.resultRuleText];
            this.styleList = [tetleTextStyleJson, contentTextStyleJson];
            this.setAllTextContent();
            this.textIsInt = true;
        };
        /**
         * 添加分割线
         */
        PlayMethodPanel.prototype.addLine = function (x, y) {
            var line = new eui.Image();
            line.source = RES.getRes("tpm_line_png");
            line.x = x;
            line.y = y;
            line.width = this.baseRuleText.width;
            line.height = 1;
            this.baseRuleScroller.viewport.addChild(line);
        };
        PlayMethodPanel.prototype.setAllTextContent = function () {
            var baseRuleConf = RES.getRes("tpm_baseRuleConf_json");
            var len = baseRuleConf.content.length;
            var clen = this.contentGroup.numChildren;
            for (var i = 0; i < len; i++) {
                this.setTextContent(this.contentList[i], baseRuleConf.content[i]);
            }
            this.addLine(40, 90);
            this.addLine(40, 310);
        };
        PlayMethodPanel.prototype.setTextContent = function (target, src) {
            var len = src.length;
            var arr = [];
            for (var i = 0; i < len; i++) {
                var textItem = {};
                textItem.text = src[i].text;
                textItem.style = this.styleList[Number(src[i].style)];
                arr.push(textItem);
            }
            target.textFlow = arr;
        };
        /**
         * 设置番型
         */
        PlayMethodPanel.prototype.setFanType = function () {
            if (this.fanTypeIsInt)
                return;
            var typeConf = RES.getRes("tpm_fanTypeConf_json");
            var len = typeConf.content.length;
            var viewport = this.baseTypeScroller.viewport;
            var titleWidth = this.baseTypeScroller.width;
            for (var i = len - 1; i > 0; i--) {
                var flen = typeConf.content[i].length;
                for (var j = 0; j < flen; j++) {
                    var data = typeConf.content[i][j];
                    if (j == 0) {
                        var title = new eui.Label(data.fanNum);
                        title.size = 27.2;
                        title.width = titleWidth;
                        title.textColor = 0x370b00;
                        title.fontFamily = "SimHei";
                        title.textAlign = "left";
                        viewport.addChild(title);
                        j = 1;
                        data = typeConf.content[i][j];
                    }
                    var item = new Tpm.FanTypeItem();
                    // item.setName(data.name);
                    item.setDescripe(data.name + "：" + data.descripe);
                    item.setCardList(data.cardList);
                    viewport.addChild(item);
                }
            }
            this.fanTypeIsInt = true;
        };
        /**
         * 显示选择的滑动组件
         */
        PlayMethodPanel.prototype.showTargetScroller = function (index, isreset) {
            if (index === void 0) { index = 0; }
            if (isreset === void 0) { isreset = false; }
            this.playMethodtabBar.selectedIndex = index;
            var len = this.contentGroup.numChildren;
            for (var i = 0; i < len; i++) {
                var target = this.contentGroup.getChildAt(i);
                if (i == index)
                    target.visible = true;
                else
                    target.visible = false;
                if (isreset)
                    target.viewport.scrollV = 0;
            }
        };
        return PlayMethodPanel;
    }(Tpm.BasePanel));
    Tpm.PlayMethodPanel = PlayMethodPanel;
    __reflect(PlayMethodPanel.prototype, "Tpm.PlayMethodPanel");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PlayMethodPanel.js.map