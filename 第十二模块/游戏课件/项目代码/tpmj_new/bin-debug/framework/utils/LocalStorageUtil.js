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
    var LocalStorageUtil = (function (_super) {
        __extends(LocalStorageUtil, _super);
        function LocalStorageUtil() {
            return _super.call(this) || this;
        }
        Object.defineProperty(LocalStorageUtil.prototype, "allowMusic", {
            get: function () {
                var item = this.loadItem("tpm_allowMusic");
                if (item == null) {
                    this.allowMusic = true;
                    item = "1";
                }
                return !!parseInt(item);
            },
            set: function (allow) {
                this.saveItem("tpm_allowMusic", (allow ? "1" : "0"));
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(LocalStorageUtil.prototype, "allowEffect", {
            get: function () {
                var item = this.loadItem("tpm_allowEffect");
                if (item == null) {
                    this.allowEffect = true;
                    item = "1";
                }
                return !!parseInt(item);
            },
            set: function (allow) {
                this.saveItem("tpm_allowEffect", (allow ? "1" : "0"));
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(LocalStorageUtil.prototype, "autoVoice", {
            get: function () {
                var item = this.loadItem("tpm_autoVoice");
                if (item == null) {
                    this.autoVoice = true;
                    item = "1";
                }
                return !!parseInt(item);
            },
            set: function (allow) {
                this.saveItem("tpm_autoVoice", (allow ? "1" : "0"));
            },
            enumerable: true,
            configurable: true
        });
        LocalStorageUtil.prototype.saveItem = function (key, data) {
            if (!key)
                return;
            egret.localStorage.setItem(key, data);
        };
        LocalStorageUtil.prototype.loadItem = function (key) {
            if (!key)
                return;
            return egret.localStorage.getItem(key);
        };
        return LocalStorageUtil;
    }(Tpm.SingleClass));
    Tpm.LocalStorageUtil = LocalStorageUtil;
    __reflect(LocalStorageUtil.prototype, "Tpm.LocalStorageUtil");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=LocalStorageUtil.js.map