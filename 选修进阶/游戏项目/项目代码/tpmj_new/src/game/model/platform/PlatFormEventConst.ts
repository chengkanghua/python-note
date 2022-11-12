module Tpm {
	export class PlatFormEventConst {
	/**监听用户信息事件*/
	public static setUseInfo:string = "setUseInfo";
	/**监听游戏开始事件 */
	public static gameStart:string = "gameStart";
	/**发送游戏结束事件*/
	public static gameEnd:string = "gameEnd";
	/**发送支付事件*/
	public static payStart:string = "payStart";
	/**监听支付结束事件 */
	public static payEnd:string = "payEnd";
	/**发送分享开始事件 shareStart*/
	public static shareStart:string = "shareStart";
	/*监听分享完成事件**/
	public static shareEnd:string = "shareEnd";
	}
}