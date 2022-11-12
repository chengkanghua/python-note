var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var UserVO = (function () {
        function UserVO() {
            /**用户ID*/
            this._userID = 0;
            /**昵称*/
            this.nickName = "";
            /**玩家性别*/
            this.sex = Tpm.SEX_TYPE.girl;
            /**用户头像地址*/
            this._headUrl = "";
            /**验证用户有效性*/
            this.skey = "";
            /**设备号 */
            this.deviceID = "111";
            /**钻石*/
            this.diamond = 0;
            /**玩家座位号*/
            this.seatID = 0;
            /**金币*/
            this.gold = 0;
            /**庄家标识 */
            this.zhuangFlag = false;
        }
        /**根据http登录返回初始化用户 */
        UserVO.prototype.initUserFromHttp = function (data) {
            this._userID = data.uid;
            this.nickName = data.nick_name;
            this.headUrl = data.avater_url == "1" ? "" : data.avater_url;
            this.skey = data.skey;
            this.sex = data.sex;
            this.diamond = data.diamond;
            this.gold = data.money;
            this.userPos = Tpm.UserPosition.Down;
        };
        /**根据socket返回初始化用户 */
        UserVO.prototype.initUserFromSocket = function (data) {
            this._userID = data.user_id;
            this.nickName = data.nick;
            this.seatID = data.seat_id;
            this.gold = data.point;
            this.state = data.status;
            if (this._userID == Tpm.App.DataCenter.UserInfo.myUserUid) {
                this.userPos = Tpm.UserPosition.Down;
            }
            else {
                this.userPos = Tpm.UserPosition.Up;
            }
        };
        Object.defineProperty(UserVO.prototype, "headUrl", {
            get: function () {
                return this._headUrl;
            },
            //服务端头像默认传送的不是字符串，而是数字，导致加载头像无法识别
            set: function (url) {
                if (url == 1) {
                    this._headUrl = "";
                }
                else {
                    this._headUrl = url;
                }
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(UserVO.prototype, "userID", {
            get: function () {
                return this._userID;
            },
            enumerable: true,
            configurable: true
        });
        return UserVO;
    }());
    Tpm.UserVO = UserVO;
    __reflect(UserVO.prototype, "Tpm.UserVO");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=UserVO.js.map