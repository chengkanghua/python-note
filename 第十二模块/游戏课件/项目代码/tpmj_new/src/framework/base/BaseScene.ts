module Tpm {
	export class BaseScene extends BaseUI {
		/**场景的控制类*/
		protected ctrl: BaseController;

		public constructor() {
			super();
		}

		/**
		 * 设置
		 */
		public setController(ctrl: BaseController) {
			this.ctrl = ctrl;
		}
	}
}
