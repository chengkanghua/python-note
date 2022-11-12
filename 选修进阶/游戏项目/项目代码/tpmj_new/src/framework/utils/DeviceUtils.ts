module Tpm {
	export class DeviceUtils extends SingleClass {

		public get IsWeb() {
			return (egret.Capabilities.runtimeType == egret.RuntimeType.WEB);
		}

		public get IsNative() {
			return (egret.Capabilities.runtimeType == egret.RuntimeType.NATIVE);
		}

		public get IsIos() {
			return (egret.Capabilities.os == "iOS")
		}

		public get IsAndroid() {
			return (egret.Capabilities.os == "Android")
		}
	}
}