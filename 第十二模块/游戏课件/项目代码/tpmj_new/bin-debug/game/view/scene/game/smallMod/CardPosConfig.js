var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    /**
     * 牌位置的配置
     */
    var CardPos = (function () {
        function CardPos() {
        }
        return CardPos;
    }());
    //--------位置相关配置---------
    CardPos.outCardPosXList = [230, 1031];
    CardPos.outCardPosYList = [536, 127];
    CardPos.outCardGapList = [50, 46];
    CardPos.handCardPosXList = [70, 270];
    CardPos.handCardPosYlist = [624, 19];
    CardPos.handCardGapList = [82, 63];
    CardPos.eatCardPosYList = [647, 23];
    CardPos.eatCardGapList = [73, 60];
    /**吃牌相对手牌X轴偏移量 */
    CardPos.eatCardOffset = [0, 9];
    /**明杠第四张Y轴偏移量 */
    CardPos.gangFourOffsetY = [-22, -19];
    /**暗杠第四张Y轴偏移量 */
    CardPos.angFourOffsetY = [-21, -18];
    CardPos.moCardPosXList = [1179, 185];
    /**发牌或摸牌动画时，手牌Y轴偏移值 */
    CardPos.moCardOffsetY = [-50, -19];
    /**推倒时摸牌位置偏移 */
    CardPos.huCardOffsetX = [30, -9];
    Tpm.CardPos = CardPos;
    __reflect(CardPos.prototype, "Tpm.CardPos");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=CardPosConfig.js.map