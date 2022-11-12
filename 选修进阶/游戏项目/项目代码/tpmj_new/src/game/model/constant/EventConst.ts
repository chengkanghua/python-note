module Tpm {
	export class EventConst {
		/**Socket连接成功*/
		public static SocketConnect: string = "SocketConnect";
		/**socket开始重连*/
		public static StartReconnect: string = "StartReconnect";
		/**send数据时，socket未连接*/
		public static SocketNotConnect: string = "SocketNotConnect";
		/**socket 连接错误*/
		public static SocketIOError: string = "SocketIOError";
		/**socket 关闭*/
		public static SocketClose: string = "SocketClose";
	}
}