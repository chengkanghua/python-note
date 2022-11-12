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
    var ResultFanItem = (function (_super) {
        __extends(ResultFanItem, _super);
        function ResultFanItem() {
            var _this = _super.call(this) || this;
            _this.skinName = "TpmSkin.ResultFanItemSkin";
            return _this;
        }
        ResultFanItem.prototype.dataChanged = function () {
            this.nameLab.text = this.data.name;
            this.fanLab.text = this.data.fan + "";
        };
        return ResultFanItem;
    }(eui.ItemRenderer));
    Tpm.ResultFanItem = ResultFanItem;
    __reflect(ResultFanItem.prototype, "Tpm.ResultFanItem");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=ResultFanItem.js.map