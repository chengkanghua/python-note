var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var Tpm;
(function (Tpm) {
    var PersonalInfoData = (function () {
        function PersonalInfoData() {
        }
        return PersonalInfoData;
    }());
    PersonalInfoData.infoData = {
        action: "PersonalInfoHandler",
        data: {
            point: -77,
            accid: 1,
            uid: 9123,
            ratewinning: "5%",
            avater_url: "",
            totalgames: 165,
            sex: 1,
            highest_winning_streak: 2,
            name: "abc"
        },
        ret: 0,
        desc: "success"
    };
    Tpm.PersonalInfoData = PersonalInfoData;
    __reflect(PersonalInfoData.prototype, "Tpm.PersonalInfoData");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=PersonalInfoData.js.map