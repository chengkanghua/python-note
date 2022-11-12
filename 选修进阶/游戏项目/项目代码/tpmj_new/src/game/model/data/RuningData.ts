module Tpm {
    /**
     * 运行时的全局变量类
     */
    export class RuningData {
        /*牌局内游戏状态*/
        public gameState: GameState;
        /**socket是否被断开 */
        public socketClose: boolean;
        /**牌局内是否允许出牌 */
        public bAllowOutCard: boolean;
        /**自家是否是听牌状态 */
        public ownTingState: boolean;
        /**当前牌局的类型 */
        public curentRoomType: RoomType;
        /**记录最近可操作的牌 */
        public latelyCardValue: number;
        /**是否在显示操作按钮 */
        public selectBtnState: boolean;
        /**自家过胡次数 */
        public ownGuoTimes: number;

        public constructor() {
            this.gameState = GameState.Free;
            this.socketClose = false;
            this.bAllowOutCard = false;
            this.ownTingState = false;
            this.curentRoomType = RoomType.noob;
            this.selectBtnState = false;
            this.ownGuoTimes = 0;
        }

        /**是否是可过胡规则 */
        public get guoHuFlag():boolean {
            if (this.curentRoomType != RoomType.noob) {
                return true;
            }
            else {
                return false;
            }
        }

        /**状态值重置 */
        public clearData(flag: boolean = true) {
            this.gameState = GameState.Free;
            this.socketClose = false;
            this.bAllowOutCard = false;
            this.ownTingState = false;
            this.selectBtnState = false;
            flag && (this.curentRoomType = RoomType.noob);
            this.ownGuoTimes = 0;
        }
    }
}