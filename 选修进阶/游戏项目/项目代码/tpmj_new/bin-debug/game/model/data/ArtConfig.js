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
    /**
     * 美术配置
     * 皮肤配置中的style注释
     */
    var ArtConfig = (function (_super) {
        __extends(ArtConfig, _super);
        function ArtConfig() {
            var _this = _super.call(this) || this;
            _this.initList();
            return _this;
        }
        ArtConfig.prototype.initList = function () {
            this.colorList = [
                0x000000,
                0xffffff,
                0xF9F4D5,
                0x6D0006
            ];
            this.fontList = [
                "Microsoft YaHei"
            ];
            this.sizeList = [];
        };
        ArtConfig.prototype.getColor = function (color) {
            if (!this.colorList[color] && this.colorList[color] != 0) {
                console.error("color null");
            }
            return this.colorList[color];
        };
        ArtConfig.prototype.getFont = function (font) {
            if (!this.fontList[font]) {
                console.error("font null");
            }
            return this.fontList[font];
        };
        ArtConfig.prototype.getSize = function (size) {
            if (!this.sizeList[size]) {
                console.error("size null");
            }
            return this.sizeList[size];
        };
        return ArtConfig;
    }(Tpm.SingleClass));
    Tpm.ArtConfig = ArtConfig;
    __reflect(ArtConfig.prototype, "Tpm.ArtConfig");
    /**
     * 颜色配置
     */
    var ColorConst;
    (function (ColorConst) {
        ColorConst[ColorConst["black"] = 0] = "black";
        ColorConst[ColorConst["white"] = 1] = "white";
        ColorConst[ColorConst["middleTips"] = 2] = "middleTips";
        ColorConst[ColorConst["topTips"] = 3] = "topTips";
    })(ColorConst = Tpm.ColorConst || (Tpm.ColorConst = {}));
    /**
     * 字体配置
     */
    var FontConst;
    (function (FontConst) {
        FontConst[FontConst["Microsoft"] = 0] = "Microsoft";
    })(FontConst = Tpm.FontConst || (Tpm.FontConst = {}));
    /**
     * 尺寸配置
     */
    var SizeConst;
    (function (SizeConst) {
    })(SizeConst = Tpm.SizeConst || (Tpm.SizeConst = {}));
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ArtConfig.js.map