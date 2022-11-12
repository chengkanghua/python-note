var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 房间配置列表
     */
    var RoomInfo = (function () {
        function RoomInfo() {
        }
        RoomInfo.prototype.initList = function (data) {
            this.roomList = [];
            for (var i = 0; i < data.length; i++) {
                var itemData = new Tpm.RoomData();
                itemData.initData(data[i]);
                this.roomList.push(itemData);
            }
            this.roomList.sort(function (a, b) {
                return a.roomType - b.roomType;
            });
            console.log("房间配置表：", this.roomList);
        };
        /**获取指定房间类型的配置 */
        RoomInfo.prototype.getConfigForType = function (type) {
            if (!this.roomList) {
                console.error("roominfo not init");
                return;
            }
            return this.roomList[type];
        };
        /**更新房间人数 */
        RoomInfo.prototype.reRoomNum = function (list) {
            if ((!list) || list.length < 3) {
                console.log("roomnum error");
                return;
            }
            for (var i = 0; i < list.length; i++) {
                this.roomList[i].curPlayerCount = list[i];
            }
        };
        return RoomInfo;
    }());
    Tpm.RoomInfo = RoomInfo;
    __reflect(RoomInfo.prototype, "Tpm.RoomInfo");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=RoomInfo.js.map