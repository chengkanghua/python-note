module Tpm {
	/**接收WEB数据*/
	export class HallHttpDataReceive extends SingleClass {
		/**
		 * 接收商品列表
		 */
		public static revGoodsList(data) {
			var revData = ProtocolHttpData.GoodsListData;
			revData=data;
			if (!revData.ret)
				App.PanelManager.open(PanelConst.ShopMallPanel, false, null, null, true, true, revData.data);
			else
				Tips.showTop(revData.desc);
		}
		/**
	     * 购买商品返回
	     */
		public static revBuyProp(data) {
			var revData = ProtocolHttpData.GoodsListData;
			revData=data;
			if (!revData.ret)
			{ }
			else if (revData.ret == 303)            //钻石不足，向平台发起购买钻石请求
			{
				App.PlatformBridge.sendPlatformEvent(PlatFormEventConst.payStart);
			}
			else
				Tips.showTop(revData.desc);
		}

		/**
		 * 接收邮件列表
		 */
		public static revEmailList(data) {
			var revData = ProtocolHttpData.EmailListData;
			revData=data;
			if (!revData.ret||revData.ret==400)
				App.PanelManager.open(PanelConst.EmailPanel, false, null, null, true, true, revData.data);
			else
				Tips.showTop(revData.desc);
		}
		/**
		 * 接收邮件详情
		 */
		public static revEmailDetail(data) {
			var revData = ProtocolHttpData.emailDeatilData;
			revData=data;
			if (!revData.ret)
				App.PanelManager.open(PanelConst.EmailDetailPanel, false, null, null, true, true, revData.data);
			else
				Tips.showTop(revData.desc);
		}

		/**
	     * 接收个人信息
	     */
		public static revUserInfo(data) {
			var revData = ProtocolHttpData.PersonalInfoData;
			revData=data;
			if (!revData.ret)
				App.PanelManager.open(PanelConst.PersonalInfoPanel, false, null, null, true, true, revData.data);
			else
				Tips.showTop(revData.desc);
		}
		/**
	     * 接收钻石金币信息
	     */
		public static revMoneyMsg(data) {
			var revData = ProtocolHttpData.PersonalInfoData;
			revData = data;
			if (!revData.ret) {
				var hallscene = App.SceneManager.getScene(SceneConst.HallScene) as HallScene;
				hallscene && hallscene.headMod.updateDiamondAndGold(revData.data.diamond, revData.data.money);
			}
			else
				Tips.showTop(revData.desc);
		}
		/**
	     * 接收获取救济金信息
	     */
		public static revIncomeSupportMsg(data) {
			var revData = ProtocolHttpData.GiveMoneyData;
			revData = data;
			if (!revData.ret) {
				App.PanelManager.open(PanelConst.GiveMoneyPanel,false,null,this,false,true,revData.data);
			}
			else
				Tips.showTop(revData.desc);
		}
		/**
	     * 接收领取救济金
	     */
		public static revIncomeSupport(data) {
			var revData = ProtocolHttpData.GiveMoneyData;
			revData = data;
			if (!revData.ret) {
				var hallscene = App.SceneManager.getScene(SceneConst.HallScene) as HallScene;
				// hallscene && hallscene.headMod.updateDiamondAndGold(revData.data.diamond, revData.data.money);
			}
			else
				Tips.showTop(revData.desc);
		}
	}
}