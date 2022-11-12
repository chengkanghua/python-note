module Tpm {
	export class ShareData {
		public static wxShareData = {
			shareType: "wxShare",//微信分享
			type: 0,//分享类型 0.聊天界面 1.朋友圈
			title: "",//标题，长度不能超过512字节
			content: "",//描述内容，长度不能超过1K
			picUrlstr: ""//图标 URL地址（网络地址）
		}
		public static qqShareData = {
			shareType: "qqShare",//QQ分享
			title: "",//标题，长度不能超过512字节
			url: "",//目标URL
			description: "",//描述内容，长度不能超过1K
			picUrlstr: ""//图标 URL地址（网络地址）
		}

	}
}