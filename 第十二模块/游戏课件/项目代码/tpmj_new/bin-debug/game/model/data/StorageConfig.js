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
     * 本地缓存配置
     */
    var StorageConfig = (function (_super) {
        __extends(StorageConfig, _super);
        function StorageConfig() {
            return _super.call(this) || this;
        }
        StorageConfig.prototype.init = function () {
            Tpm.App.SoundManager.allowPlayBGM = Tpm.App.LocalStorageUtil.allowMusic;
            Tpm.App.SoundManager.allowPlayEffect = Tpm.App.LocalStorageUtil.allowEffect;
        };
        return StorageConfig;
    }(Tpm.SingleClass));
    Tpm.StorageConfig = StorageConfig;
    __reflect(StorageConfig.prototype, "Tpm.StorageConfig");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=StorageConfig.js.map