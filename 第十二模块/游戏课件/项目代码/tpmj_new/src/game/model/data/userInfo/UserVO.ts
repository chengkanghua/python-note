module Tpm {
    export class UserVO {
        /**用户ID*/
        private _userID: number = 0;
        /**昵称*/
        public nickName: string = "";
        /**用户位置 0-3  0下 1右 2中上 3左*/
        private userPos: UserPosition;
        /**玩家性别*/
        private sex: SEX_TYPE = SEX_TYPE.girl;
        /**用户头像地址*/
        private _headUrl = "";
        /**验证用户有效性*/
        public skey: string = "";
        /**设备号 */
        private deviceID = "111";

        /**玩家状态*/
        public state: UserState;
        /**钻石*/
        public diamond: number = 0;
        /**玩家座位号*/
        public seatID: number = 0;
        /**金币*/
        public gold: number = 0;
        /**庄家标识 */
        public zhuangFlag: boolean = false;

        /**根据http登录返回初始化用户 */
        public initUserFromHttp(data) {
            this._userID = data.uid;
            this.nickName = data.nick_name;
            this.headUrl = data.avater_url == "1" ? "" : data.avater_url;
            this.skey = data.skey;		
            this.sex = data.sex;
            this.diamond = data.diamond;
            this.gold = data.money;
            this.userPos = UserPosition.Down;
        }

        /**根据socket返回初始化用户 */
        public initUserFromSocket(data) {
            this._userID = data.user_id;
            this.nickName = data.nick;
            this.seatID = data.seat_id;
            this.gold = data.point;
            this.state = data.status;
            if (this._userID == App.DataCenter.UserInfo.myUserUid) {
                this.userPos = UserPosition.Down;
            }
            else {
                this.userPos = UserPosition.Up;
            }
        }

        //服务端头像默认传送的不是字符串，而是数字，导致加载头像无法识别
        public set headUrl(url: any) {
            if (url == 1) {
                this._headUrl = "";
            } else {
                this._headUrl = url;
            }
        }

        public get userID() {
            return this._userID;
        }

        public get headUrl() {
            return this._headUrl;
        }
    }
}
