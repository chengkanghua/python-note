module Tpm {
	export class KeyWord extends SingleClass {
		private keyWordList;   //关键词列表
		public constructor() {
			super();
			this.init();
		}

		//初始化
		public init() {
			var data = RES.getRes("kwx_keywordConfig_json");
			this.keyWordList = data.keyword.split("|");
		}

		/**
		 * 过滤字符串
		 * @msg 需要检查的字符串
		 * @return 处理后的字符串
		 */
		public filteString(msg: string) {
			if (this.isInit()) {
				var len = this.keyWordList.length;
				var reg;
				for (var i = 0; i < len; i++) {
					reg = new RegExp(this.keyWordList[i], "i");
					if (msg.search(reg) != -1) {
						console.log("包含敏感关键词:", this.keyWordList[i]);
						var strLen = this.keyWordList[i].length;
						var replaceStr = "";
						for (var j = 0; j < strLen; j++) {
							replaceStr += "*";
						}
						msg = msg.replace(reg, replaceStr);
					}
				}
				return msg;
			}
			return "***";
		}

		/**
		 * 检查字符串是否包含关键词
		 * @msg 待检查的字符串
		 * @return 返回字符串是否合格
		 */
		public checkStringOK(msg: string): boolean {
			if (this.isInit()) {
				var len = this.keyWordList.length;
				var reg;
				for (var i = 0; i < len; i++) {
					reg = new RegExp(this.keyWordList[i], "i");
					if (msg.match(reg) != null) {
						return false;
					}
				}
				return true;
			}
			return false;
		}

		/**是否初始化过*/
		public isInit(): boolean {
			return (this.keyWordList != null);
		}
	}
}