var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 用户数据
     */
    var UserInfo = (function () {
        function UserInfo() {
            /**用户列表 [userID][userVO]*/
            this.userList = {};
        }
        Object.defineProperty(UserInfo.prototype, "myUserInfo", {
            /**用户本人信息 */
            get: function () {
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
            },
            enumerable: true,
            configurable: true
        });
        /**
         * 添加用户
         * @param userVo 用户数据Vo
         */
        UserInfo.prototype.addUser = function (userVo) {
            if (this.userList[userVo.userID]) {
                console.log("用户重复添加:", userVo.userID);
            }
            else {
                this.userList[userVo.userID] = userVo;
            }
            var userNum = this.getUserNum();
            if (userNum > 2) {
                console.error("user > 2");
            }
            console.log("自己ID==", this.myUserUid);
            console.log("玩家列表==", this.userList);
        };
        /**
         * 获取用户
         * @param userId 用户userId
         * @returns 返回用户信息
         */
        UserInfo.prototype.getUser = function (userID) {
            return this.userList[userID];
        };
        /**
         * 判断用户是否存在
         * @userID 用户ID
         * @return 是否存在
         */
        UserInfo.prototype.isExist = function (userID) {
            if (this.getUser(userID)) {
                return true;
            }
            else {
                return false;
            }
        };
        /**
         * 根据座位号获取用户信息
         * @param seatID 座位号
         * @returns 返回用户信息
         */
        UserInfo.prototype.getUserBySeatID = function (seatID) {
            for (var key in this.userList) {
                if (this.userList[key].seatID == seatID) {
                    return this.userList[key];
                }
            }
        };
        /**
         * 根据pos获得用户信息
         */
        UserInfo.prototype.getUserByPos = function (pos) {
            for (var key in this.userList) {
                if (this.userList[key].userPos == pos) {
                    return this.userList[key];
                }
            }
            return null;
        };
        /**
     * 根据userID获取用户信息
     * @param userID
     * @returns 返回用户信息
     */
        UserInfo.prototype.getUserByUserID = function (userID) {
            for (var key in this.userList) {
                if (this.userList[key].userID == userID) {
                    return this.userList[key];
                }
            }
        };
        /**
         * 删除用户信息
         * @param userID 用户ID
         */
        UserInfo.prototype.deleteUser = function (userID) {
            delete this.userList[userID];
        };
        /**删除所有用户信息，除了自己*/
        UserInfo.prototype.deleteAllUserExcptMe = function () {
            for (var key in this.userList) {
                if (parseInt(key) != this.myUserInfo.userID) {
                    delete this.userList[key];
                }
            }
        };
        /**删除所有用户信息*/
        UserInfo.prototype.deleteAllUser = function () {
            for (var key in this.userList) {
                delete this.userList[key];
            }
        };
        /**获取用户数量*/
        UserInfo.prototype.getUserNum = function () {
            return Tpm.ArrayTool.getObjectLength(this.userList);
        };
        /**
         * 获取位置
         */
        UserInfo.prototype.getPosFromSeat = function (seat) {
            console.log("isMine--------", this.myUserInfo.seatID == seat);
            if (this.myUserInfo.seatID == seat) {
                return Tpm.UserPosition.Down;
            }
            else {
                return Tpm.UserPosition.Up;
            }
        };
        UserInfo.prototype.getSeatFromPos = function (pos) {
            var user = this.getUserByPos(pos);
            return user.seatID;
        };
        /**判断是否是庄家 */
        UserInfo.prototype.isZhuang = function (userid) {
            var user = this.getUserByUserID(userid);
            if (user.zhuangFlag) {
                return true;
            }
            return false;
        };
        /**清除庄家标识 */
        UserInfo.prototype.clearZhuang = function () {
            for (var key in this.userList) {
                this.userList[key].zhuangFlag = false;
            }
        };
        return UserInfo;
    }());
    Tpm.UserInfo = UserInfo;
    __reflect(UserInfo.prototype, "Tpm.UserInfo");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=UserInfo.js.map