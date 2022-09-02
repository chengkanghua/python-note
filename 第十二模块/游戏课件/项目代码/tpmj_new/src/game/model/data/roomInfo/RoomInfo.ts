module Tpm {
    /**
     * 房间配置列表
     */
    export class RoomInfo {
        /**配置列表 */
        public roomList: Array<RoomData>;

        public initList(data: Array<any>) {
            this.roomList = [];
            for (var i = 0;i < data.length;i ++) {
                var itemData = new RoomData();
                itemData.initData(data[i]);
                this.roomList.push(itemData);
            }

            this.roomList.sort((a:RoomData, b:RoomData)=>{
                return a.roomType - b.roomType;
            })
            console.log("房间配置表：", this.roomList);
        }

        /**获取指定房间类型的配置 */
        public getConfigForType(type: RoomType) {
            if (!this.roomList) {
                console.error("roominfo not init")
                return;
            }

            return this.roomList[type];
        }

        /**更新房间人数 */
        public reRoomNum(list: Array<number>) {
            if ( (!list) || list.length < 3 ) {
                console.log("roomnum error");
                return;
            }

            for (var i = 0;i < list.length;i ++) {
                this.roomList[i].curPlayerCount = list[i];
            }
        }
    }
}