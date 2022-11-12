module Tpm {
	/**
	 * 美术配置
	 * 皮肤配置中的style注释
	 */
	export class ArtConfig extends SingleClass{

		private colorList: Array<number>;
		private fontList: Array<string>;
		private sizeList: Array<number>; 

		public constructor() {
			super();

			this.initList();
		}

		private initList() {
			this.colorList = [
				0x000000,
				0xffffff,
				0xF9F4D5,
				0x6D0006
			];

			this.fontList = [
				"Microsoft YaHei"
			];

			this.sizeList = [

			];
		}

		public getColor(color: ColorConst):number {
			if (!this.colorList[color] && this.colorList[color] != 0) {
				console.error("color null");
			}
			return this.colorList[color];
		}

		public getFont(font: FontConst):string {
			if (!this.fontList[font]) {
				console.error("font null");
			}
			return this.fontList[font];
		}

		public getSize(size: SizeConst):number {
			if (!this.sizeList[size]) {
				console.error("size null");
			}
			return this.sizeList[size];
		}
	}

	/**
	 * 颜色配置
	 */
	export enum ColorConst {
		"black",
		"white",
		"middleTips",
		"topTips"
	}

	/**
	 * 字体配置
	 */
	export enum FontConst {
		"Microsoft"
	}

	/**
	 * 尺寸配置
	 */
	export enum SizeConst {

	}
}