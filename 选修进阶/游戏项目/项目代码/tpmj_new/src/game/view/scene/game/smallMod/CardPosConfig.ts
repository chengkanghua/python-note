module Tpm {
    /**
     * 牌位置的配置
     */
    export class CardPos {
        //--------位置相关配置---------
        public static outCardPosXList = [230, 1031];
        public static outCardPosYList = [536, 127];
        public static outCardGapList = [50, 46];
        public static handCardPosXList = [70, 270];
        public static handCardPosYlist = [624, 19];
        public static handCardGapList = [82, 63];
        public static eatCardPosYList = [647, 23];
        public static eatCardGapList = [73, 60];
        /**吃牌相对手牌X轴偏移量 */
        public static eatCardOffset = [0, 9];
        /**明杠第四张Y轴偏移量 */
        public static gangFourOffsetY = [-22, -19];
        /**暗杠第四张Y轴偏移量 */
        public static angFourOffsetY = [-21, -18];
        public static moCardPosXList = [1179, 185];
        /**发牌或摸牌动画时，手牌Y轴偏移值 */
        public static moCardOffsetY = [-50, -19];
        /**推倒时摸牌位置偏移 */
        public static huCardOffsetX = [30, - 9];
    }
}