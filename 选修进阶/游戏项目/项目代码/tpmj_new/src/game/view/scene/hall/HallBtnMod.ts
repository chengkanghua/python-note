module Tpm {
	export enum HallBtnMsg {
		playMethod,
		email,
		share,
		shop,
		set
	}

	export class HallBtnMod extends BaseUI{
		private hall_playMethod:eui.Button;
		private hall_email:eui.Button;
		private hall_share:eui.Button;
		private hall_shop:eui.Button;
		private hall_set:eui.Button;

		public listener:Function;

		public constructor() {
			super();
            this.skinName = TpmSkin.HallBtnModSkin;
		}

		protected childrenCreated() {

        }

		protected onEnable() {
			this.addEventListener(egret.TouchEvent.TOUCH_TAP, this.onTouch, this);
        }

		protected onRemove() {

        }

		private onTouch(e: egret.TouchEvent) {
			if (!this.listener) {
				console.error("按钮未设置监听");
				return;
			}

			var target = e.target;
			var message;
			switch (target) {
				case this.hall_playMethod:
					message = HallBtnMsg.playMethod;
					break;
				case this.hall_email:
					message = HallBtnMsg.email;
					break;
				case this.hall_share:
					message = HallBtnMsg.share;
					break;
				case this.hall_shop:
					message = HallBtnMsg.shop;
					break;
				case this.hall_set:
					message = HallBtnMsg.set;
					break;
				default:
					break;
			}
			if (message || message == 0) {
				this.listener(message);
			}
		}
	}
}