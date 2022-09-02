module Tpm {
    /**
     * 用户数据
     */
    export class UserInfo {
        /**用户列表 [userID][userVO]*/
        public userList = {};
        /**用户本人uid */
        public myUserUid:number;

        /**用户本人信息 */
        public get myUserInfo ():UserVO {
            if (!this.myUserUid) {
                console.error("uid null");
                return;
            }
            var info = this.getUser(this.myUserUid);
            if (!info) {
                console.error("userinfo null");
                return;
            }
            return info;
        }

        /**
         * 添加用户
         * @param userVo 用户数据Vo
         */
        public addUser(userVo: UserVO) {
            if (this.userList[userVo.userID]) {
                console.log("用户重复添加:", userVo.userID);
            } else {
                this.userList[userVo.userID] = userVo;
            }

            var userNum = this.getUserNum();
            if (userNum > 2) {
                console.error("user > 2");
            }
            console.log("自己ID==", this.myUserUid);
            console.log("玩家列表==", this.userList);
        }

        /**
         * 获取用户
         * @param userId 用户userId
         * @returns 返回用户信息
         */
        public getUser(userID: number) {
            return this.userList[userID];
        }

        /**
         * 判断用户是否存在
         * @userID 用户ID
         * @return 是否存在
         */
        public isExist(userID: number) {
            if (this.getUser(userID)) {
                return true;
            } else {
                return false;
            }
        }

        /**
         * 根据座位号获取用户信息
         * @param seatID 座位号
         * @returns 返回用户信息
         */
        public getUserBySeatID(seatID: number): UserVO {
            for (var key in this.userList) {
                if (this.userList[key].seatID == seatID) {
                    return this.userList[key];
                }
            }
        }

        /**
         * 根据pos获得用户信息
         */
        public getUserByPos(pos: UserPosition): UserVO {
            for (let key in this.userList) {
                if (this.userList[key].userPos == pos) {
                    return this.userList[key];
                }
            }
            return null;
        }

        /**
     * 根据userID获取用户信息
     * @param userID 
     * @returns 返回用户信息
     */
        public getUserByUserID(userID: number): UserVO {
            for (var key in this.userList) {
                if (this.userList[key].userID == userID) {
                    return this.userList[key];
                }
            }
        }

        /**
         * 删除用户信息
         * @param userID 用户ID
         */
        public deleteUser(userID: number) {
            delete this.userList[userID];
        }

        /**删除所有用户信息，除了自己*/
        public deleteAllUserExcptMe() {
            for (var key in this.userList) {
                if (parseInt(key) != this.myUserInfo.userID) {
                    delete this.userList[key];
                }
            }
        }
        /**删除所有用户信息*/
        public deleteAllUser() {
            for (var key in this.userList) {
                delete this.userList[key];
            }
        }

        /**获取用户数量*/
        public getUserNum() {
            return ArrayTool.getObjectLength(this.userList);
        }

        /**
         * 获取位置
         */
        public getPosFromSeat(seat: number):UserPosition {
            console.log("isMine--------", this.myUserInfo.seatID==seat);
            if (this.myUserInfo.seatID == seat) {
                return UserPosition.Down;
            }
            else {
                return UserPosition.Up;
            }
        }

        public getSeatFromPos(pos: UserPosition):number {
            var user = this.getUserByPos(pos);
            return user.seatID;
        }

        /**判断是否是庄家 */
        public isZhuang(userid: number):boolean {
            var user = this.getUserByUserID(userid);
            if (user.zhuangFlag) {
                return true;
            }
            return false;
        }

        /**清除庄家标识 */
        public clearZhuang() {
            for (var key in this.userList) {
                this.userList[key].zhuangFlag = false;
            }
        }
    }
}
