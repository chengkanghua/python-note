var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 运行时的全局变量类
     */
    var RuningData = (function () {
        function RuningData() {
            this.gameState = Tpm.GameState.Free;
            this.socketClose = false;
            this.bAllowOutCard = false;
            this.ownTingState = false;
            this.curentRoomType = Tpm.RoomType.noob;
            this.selectBtnState = false;
            this.ownGuoTimes = 0;
        }
        Object.defineProperty(RuningData.prototype, "guoHuFlag", {
            /**是否是可过胡规则 */
            get: function () {
                if (this.curentRoomType != Tpm.RoomType.noob) {
                    return true;
                }
                else {
                    return false;
                }
            },
            enumerable: true,
            configurable: true
        });
        /**状态值重置 */
        RuningData.prototype.clearData = function (flag) {
            if (flag === void 0) { flag = true; }
            this.gameState = Tpm.GameState.Free;
            this.socketClose = false;
            this.bAllowOutCard = false;
            this.ownTingState = false;
            this.selectBtnState = false;
            flag && (this.curentRoomType = Tpm.RoomType.noob);
            this.ownGuoTimes = 0;
        };
        return RuningData;
    }());
    Tpm.RuningData = RuningData;
    __reflect(RuningData.prototype, "Tpm.RuningData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=RuningData.js.map