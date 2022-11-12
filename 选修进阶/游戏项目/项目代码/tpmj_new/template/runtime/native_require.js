
var game_file_list = [
    //以下为自动修改，请勿修改
    //----auto game_file_list start----
	"libs/modules/egret/egret.js",
	"libs/modules/egret/egret.native.js",
	"libs/modules/game/game.js",
	"libs/modules/res/res.js",
	"libs/modules/eui/eui.js",
	"libs/modules/tween/tween.js",
	"libs/modules/socket/socket.js",
	"libs/modules/dragonBones/dragonBones.js",
	"polyfill/promise.js",
	"bin-debug/framework/base/BaseUI.js",
	"bin-debug/framework/base/BaseGameMod.js",
	"bin-debug/framework/base/SingleClass.js",
	"bin-debug/framework/base/BaseApp.js",
	"bin-debug/framework/base/BaseController.js",
	"bin-debug/framework/base/BasePanel.js",
	"bin-debug/framework/base/BaseScene.js",
	"bin-debug/game/view/scene/game/smallMod/CardModBase.js",
	"bin-debug/game/model/protocol/ProtocolHeadRev.js",
	"bin-debug/framework/manager/EventMananger.js",
	"bin-debug/framework/manager/LayerManager.js",
	"bin-debug/framework/manager/PanelManager.js",
	"bin-debug/framework/manager/PopUpManager.js",
	"bin-debug/framework/manager/SceneManager.js",
	"bin-debug/framework/manager/SoundManager.js",
	"bin-debug/framework/net/ClientSocket.js",
	"bin-debug/framework/net/HttpSender.js",
	"bin-debug/framework/net/MsgCache.js",
	"bin-debug/framework/net/SocketManager.js",
	"bin-debug/framework/tools/ArrayTool.js",
	"bin-debug/framework/tools/DateTimer.js",
	"bin-debug/framework/tools/LoadingLock.js",
	"bin-debug/framework/tools/NumberTool.js",
	"bin-debug/framework/tools/ObjectPool.js",
	"bin-debug/framework/tools/StringTool.js",
	"bin-debug/framework/tools/Tips.js",
	"bin-debug/framework/utils/DeviceUtils.js",
	"bin-debug/framework/utils/EffectUtils.js",
	"bin-debug/framework/utils/KeyWord.js",
	"bin-debug/framework/utils/LocalStorageUtil.js",
	"bin-debug/framework/utils/ResUtils.js",
	"bin-debug/framework/utils/StageUtils.js",
	"bin-debug/framework/utils/Utils.js",
	"bin-debug/game/App.js",
	"bin-debug/game/model/constant/AssetConst.js",
	"bin-debug/game/model/constant/EventConst.js",
	"bin-debug/game/model/constant/PanelConst.js",
	"bin-debug/game/model/constant/SceneConst.js",
	"bin-debug/game/model/data/ArtConfig.js",
	"bin-debug/game/model/data/DataCenter.js",
	"bin-debug/game/model/data/DebugInfo.js",
	"bin-debug/game/model/data/DeskInfo.js",
	"bin-debug/game/model/data/GameInfo.js",
	"bin-debug/game/model/data/panel/email/EmailData.js",
	"bin-debug/game/model/data/panel/mall/MallData.js",
	"bin-debug/game/model/data/panel/personalinfo/PersonalInfoData.js",
	"bin-debug/game/model/data/panel/share/ShareData.js",
	"bin-debug/game/model/data/ResPathConfig.js",
	"bin-debug/game/model/data/roomInfo/RoomData.js",
	"bin-debug/game/model/data/roomInfo/RoomInfo.js",
	"bin-debug/game/model/data/RuningData.js",
	"bin-debug/game/model/data/ServerInfo.js",
	"bin-debug/game/model/data/StorageConfig.js",
	"bin-debug/game/model/data/userInfo/UserInfo.js",
	"bin-debug/game/model/data/userInfo/UserVO.js",
	"bin-debug/game/model/httpdatahandler/HallHttpDataReceive.js",
	"bin-debug/game/model/httpdatahandler/HallHttpDataSend.js",
	"bin-debug/game/model/platform/PlatformBridge.js",
	"bin-debug/game/model/platform/PlatFormEventConst.js",
	"bin-debug/game/model/protocol/ProtocolDataRev.js",
	"bin-debug/game/model/protocol/ProtocolDataSend.js",
	"bin-debug/framework/adapter/ThemeAdapter.js",
	"bin-debug/game/model/protocol/ProtocolHeadSend.js",
	"bin-debug/game/model/protocol/ProtocolHttp.js",
	"bin-debug/game/model/protocol/ProtocolHttpData.js",
	"bin-debug/game/view/common/MessageBox.js",
	"bin-debug/game/view/common/MessageBoxManager.js",
	"bin-debug/game/view/panel/common/CommonMessageBoxPanel.js",
	"bin-debug/game/view/panel/email/EmailDetailPanel.js",
	"bin-debug/game/view/panel/email/EmailItem.js",
	"bin-debug/game/view/panel/email/EmailPanel.js",
	"bin-debug/game/view/panel/givemoney/GiveMoneyPanel.js",
	"bin-debug/game/view/panel/givemoney/MoneyNotEnoughPanel.js",
	"bin-debug/game/view/panel/login/LoginPanel.js",
	"bin-debug/game/view/panel/login/RegistPanel.js",
	"bin-debug/game/view/panel/mall/ShopMallItem.js",
	"bin-debug/game/view/panel/mall/ShopMallPanel.js",
	"bin-debug/game/view/panel/net/SocketClosePanel.js",
	"bin-debug/game/view/panel/personalinfo/PersonalInfoPanel.js",
	"bin-debug/game/view/panel/playmethod/FanTypeItem.js",
	"bin-debug/game/view/panel/playmethod/PlayMethodPanel.js",
	"bin-debug/game/view/panel/result/ResultFanItem.js",
	"bin-debug/game/view/panel/result/ResultPanel.js",
	"bin-debug/game/view/panel/set/SetPanel.js",
	"bin-debug/game/view/panel/share/SharePanel.js",
	"bin-debug/game/view/rest/BitmapMovie.js",
	"bin-debug/game/view/rest/Card.js",
	"bin-debug/game/view/rest/CardFactory.js",
	"bin-debug/game/view/rest/CardLogic.js",
	"bin-debug/game/view/scene/game/GameCardMod.js",
	"bin-debug/game/view/scene/game/GameCheatMod.js",
	"bin-debug/game/view/scene/game/GameController.js",
	"bin-debug/game/view/scene/game/GameCtrlReceive.js",
	"bin-debug/game/view/scene/game/GameCtrlSend.js",
	"bin-debug/game/view/scene/game/GameDbMod.js",
	"bin-debug/game/view/scene/game/GameDiskMod.js",
	"bin-debug/game/view/scene/game/GameEatChooseMod.js",
	"bin-debug/game/view/scene/game/GameFlowerMod.js",
	"bin-debug/game/view/scene/game/GameGangChooseMod.js",
	"bin-debug/game/view/scene/game/GameHeadMod.js",
	"bin-debug/game/view/scene/game/GameHuTipsMod.js",
	"bin-debug/game/view/scene/game/GameMatchMod.js",
	"bin-debug/game/view/scene/game/GameMenuMod.js",
	"bin-debug/game/view/scene/game/GameOutShowMod.js",
	"bin-debug/game/view/scene/game/GameReadyMod.js",
	"bin-debug/game/view/scene/game/GameScene.js",
	"bin-debug/game/view/scene/game/GameSelectBtnMod.js",
	"bin-debug/game/view/scene/game/GameTingMod.js",
	"bin-debug/game/view/scene/game/GameTuogMod.js",
	"bin-debug/framework/adapter/AssetAdapter.js",
	"bin-debug/game/view/scene/game/smallMod/CardPosConfig.js",
	"bin-debug/game/view/scene/game/smallMod/HuTipsItem.js",
	"bin-debug/game/view/scene/game/smallMod/HuTypeItem.js",
	"bin-debug/game/view/scene/game/smallMod/SelectActBtn.js",
	"bin-debug/game/view/scene/hall/HallBtnMod.js",
	"bin-debug/game/view/scene/hall/HallController.js",
	"bin-debug/game/view/scene/hall/HallHeadMod.js",
	"bin-debug/game/view/scene/hall/HallRoomMod.js",
	"bin-debug/game/view/scene/hall/HallScene.js",
	"bin-debug/game/view/scene/login/LoginController.js",
	"bin-debug/game/view/scene/login/LoginScene.js",
	"bin-debug/Main.js",
	//----auto game_file_list end----
];

var window = this;

egret_native.setSearchPaths([""]);

egret_native.requireFiles = function () {
    for (var key in game_file_list) {
        var src = game_file_list[key];
        require(src);
    }
};

egret_native.egretInit = function () {
    if(egret_native.featureEnable) {
        //控制一些优化方案是否开启
        var result = egret_native.featureEnable({
            
        });
    }
    egret_native.requireFiles();
    //egret.dom为空实现
    egret.dom = {};
    egret.dom.drawAsCanvas = function () {
    };
};

egret_native.egretStart = function () {
    var option = {
        //以下为自动修改，请勿修改
        //----auto option start----
		entryClassName: "Main",
		frameRate: 30,
		scaleMode: "showAll",
		contentWidth: 1334,
		contentHeight: 750,
		showPaintRect: false,
		showFPS: false,
		fpsStyles: "x:0,y:0,size:12,textColor:0xffffff,bgAlpha:0.9",
		showLog: false,
		logFilter: "",
		maxTouches: 2,
		textureScaleFactor: 1
		//----auto option end----
    };

    egret.native.NativePlayer.option = option;
    egret.runEgret();
    egret_native.Label.createLabel("/system/fonts/DroidSansFallback.ttf", 20, "", 0);
    egret_native.EGTView.preSetOffScreenBufferEnable(true);
};