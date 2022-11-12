module Tpm {
	export class BaseController {

		/**绑定Scene添加到显示列表后调用, 无绑定SCEN则手动调用*/
		public onRegister() {

		}

		/**绑定Scene移除显示列表后调用*/
		public onRemove() {

		}

		/**
		 * 发送事件
		 * @type 事件名
		 * @args 发送数据
		 */
		public sendEvent(type: string, ...args: any[]) {
			App.EventManager.sendEvent(type, args);
		}

		/**
		 * 监听事件
		 * @type 事件名
		 * @listener 回调函数
		 * @thisObject 执行对象
		 */
		public addEvent(type: string, listener: Function, thisObject: any) {
			App.EventManager.addEvent(type, listener, thisObject);
		}

		/**
		 * 移除监听
		 * @type 事件名
		 * @listener 回调函数
		 * @thisObject 执行对象
		 */
		public removeEvent(type: string, listener: Function, thisObject: any) {
			App.EventManager.removeEvent(type, listener, thisObject);
		}
	}
}
