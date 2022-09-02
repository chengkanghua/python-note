module Tpm {
	/**
	 * 测试环境配置
	 */
	export class DebugInfo {
		/**是否调试模式*/
		public get isDebug(): boolean {
			return (egret.getOption("debug") != null && egret.getOption("debug") != "");
		};

		/**是否访问本地php，用于php访问地址设置*/
		public get isLocalPhp(): number {
			return parseInt(egret.getOption("local"));
		};

		/**
		 * gamesocket地址
		 */
		public get Sever() {
			return Number(egret.getOption("server"));
		}

		/**测试账号*/
		public get account() {
			var debug: string = egret.getOption("debug");
			if (typeof Number(debug.substr(0, 1) == "number")) {
				return "oldboy1" + egret.getOption("debug");
			}
			//临时登录测试
			else {
				this.password = egret.getOption("password");
				return egret.getOption("debug");
			}
		}
		/**测试密码*/
		public password: string = "123456";

		/**是否跳过大厅 */
		public get skipHall():boolean {
			return false;
		}

		/**是否跳过Http登录*/
		public get skipNet():boolean {
			return false;
		}
		/**是否跳过游戏服登录 */
		public get skipGameServer(): boolean {
			return false;
		}

		/**是否是测试环境 */
		public get testState():boolean {
			return true;
		}

		/**自动准备 */
		public get autoReady():boolean {
			return false;
		}
	}
}