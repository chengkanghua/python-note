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
    var LoadingLock = (function (_super) {
        __extends(LoadingLock, _super);
        function LoadingLock() {
            var _this = _super.call(this) || this;
            _this.lockNum = 0;
            _this.lockBg = new eui.Rect();
            _this.lockBg.width = 1334;
            _this.lockBg.height = 750;
            _this.lockBg.fillAlpha = 0.5;
            _this.circle = new eui.Image();
            _this.circle.source = Tpm.ResPathConfig.lockRotat;
            _this.circle.anchorOffsetX = _this.circle.width / 2;
            _this.circle.anchorOffsetY = _this.circle.height / 2;
            _this.circle.verticalCenter = 0;
            _this.circle.horizontalCenter = 0;
            _this.descLab = new eui.Label();
            _this.descLab.verticalCenter = 50;
            _this.descLab.horizontalCenter = 0;
            _this.descLab.textColor = Tpm.App.ArtConfig.getColor(Tpm.ColorConst.white);
            _this.descLab.text = "";
            _this.descLab.fontFamily = Tpm.App.ArtConfig.getFont(Tpm.FontConst.Microsoft);
            return _this;
        }
        LoadingLock.prototype.addLock = function (desc) {
            if (desc === void 0) { desc = ""; }
            if (this.lockNum < 0) {
                this.lockNum = 0;
            }
            this.lockNum++;
            egret.Tween.removeTweens(this.circle);
            this.descLab.text = desc;
            egret.Tween.get(this.circle, { loop: true }).to({ rotation: 360 }, 1000);
            Tpm.App.LayerManager.addChildToLayer(this.lockBg, Tpm.LayerConst.lockLayer);
            Tpm.App.LayerManager.addChildToLayer(this.circle, Tpm.LayerConst.lockLayer);
            Tpm.App.LayerManager.addChildToLayer(this.descLab, Tpm.LayerConst.lockLayer);
        };
        LoadingLock.prototype.minusLock = function () {
            this.lockNum--;
            if (this.lockNum <= 0 && this.circle && this.circle.parent) {
                egret.Tween.removeTweens(this.circle);
                Tpm.App.LayerManager.removeChildFromLayer(this.lockBg, Tpm.LayerConst.lockLayer);
                Tpm.App.LayerManager.removeChildFromLayer(this.circle, Tpm.LayerConst.lockLayer);
                Tpm.App.LayerManager.removeChildFromLayer(this.descLab, Tpm.LayerConst.lockLayer);
            }
        };
        return LoadingLock;
    }(Tpm.SingleClass));
    Tpm.LoadingLock = LoadingLock;
    __reflect(LoadingLock.prototype, "Tpm.LoadingLock");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LoadingLock.js.map