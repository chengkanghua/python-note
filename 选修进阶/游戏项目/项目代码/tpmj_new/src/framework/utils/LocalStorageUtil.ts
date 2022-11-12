module Tpm {
	export class LocalStorageUtil extends SingleClass {
		public constructor() {
			super();
		}

		public set allowMusic(allow: boolean) {
			this.saveItem("tpm_allowMusic", (allow ? "1" : "0"))
		}

		public get allowMusic(): boolean {
			var item = this.loadItem("tpm_allowMusic")
			if (item == null) {
				this.allowMusic = true;
				item = "1"
			}
			return !!parseInt(item);
		}

		public set allowEffect(allow: boolean) {
			this.saveItem("tpm_allowEffect", (allow ? "1" : "0"))
		}

		public get allowEffect(): boolean {
			var item = this.loadItem("tpm_allowEffect")
			if (item == null) {
				this.allowEffect = true;
				item = "1"
			}
			return !!parseInt(item);
		}

		public set autoVoice(allow: boolean) {
			this.saveItem("tpm_autoVoice", (allow ? "1" : "0"))
		}

		public get autoVoice(): boolean {
			var item = this.loadItem("tpm_autoVoice")
			if (item == null) {
				this.autoVoice = true;
				item = "1"
			}
			return !!parseInt(item);
		}

		private saveItem(key: string, data: string) {
			if (!key) return
			egret.localStorage.setItem(key, data)
		}

		private loadItem(key: string): string {
			if (!key) return
			return egret.localStorage.getItem(key);
		}
	}
}