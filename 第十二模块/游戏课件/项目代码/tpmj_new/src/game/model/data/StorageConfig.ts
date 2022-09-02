module Tpm {
	/**
	 * 本地缓存配置
	 */
	export class StorageConfig extends SingleClass {
		public constructor() {
			super();
		}

		public init() {
			App.SoundManager.allowPlayBGM=App.LocalStorageUtil.allowMusic;
			App.SoundManager.allowPlayEffect=App.LocalStorageUtil.allowEffect;
		}
	}
}