function hook_RegisterNatives() {

    var symbols = Module.enumerateSymbolsSync("libart.so");

    // RegisterNatives的内存地址
    var addrRegisterNatives = null;


    for (var i = 0; i < symbols.length; i++) {
        var symbol = symbols[i];

        // _ZN3art3JNI15RegisterNativesEP7_JNIEnvP7_jclassPK15JNINativeMethodi
        if (symbol.name.indexOf("art") >= 0 &&
            symbol.name.indexOf("JNI") >= 0 &&
            symbol.name.indexOf("RegisterNatives") >= 0 &&
            symbol.name.indexOf("CheckJNI") < 0) {
            addrRegisterNatives = symbol.address;
            console.log("RegisterNatives is at ", symbol.address, symbol.name);
        }
    }

    if (addrRegisterNatives != null) {
        // args，就是执行 addrRegisterNatives 传递的参数。
        Interceptor.attach(addrRegisterNatives, {
            onEnter: function (args) {
                var env = args[0]; // JNI对象
                var java_class = args[1]; // 类的对象
                var class_name = Java.vm.tryGetEnv().getClassName(java_class); // 类的路径

                // 只有类名为 com.bilibili.nativelibrary.LibBili ，才打印输出
                var target_class = "com.bilibili.nativelibrary.LibBili";

                if (class_name === target_class) {
                    var methods_ptr = ptr(args[2]); // 所有 c和java的函数对应地方。
                    var method_count = parseInt(args[3]);

                    for (var i = 0; i < method_count; i++) {
                        // Java中函数名字的
                        var name_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3));

                        // 参数和返回值类型
                        var sig_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3 + Process.pointerSize));

                        // C中的函数指针
                        var fnPtr_ptr = Memory.readPointer(methods_ptr.add(i * Process.pointerSize * 3 + Process.pointerSize * 2));

                        var name = Memory.readCString(name_ptr); // 读取java中函数名
                        var sig = Memory.readCString(sig_ptr); // 参数和返回值类型
                        var find_module = Process.findModuleByAddress(fnPtr_ptr); // 根据C中函数指针获取模块

                        var offset = ptr(fnPtr_ptr).sub(find_module.base) // fnPtr_ptr - 模块基地址
                        // console.log("[RegisterNatives] java_class:", class_name);
                        // console.log("name:", name, "sig:", sig, "module_name:", find_module.name, "offset:", offset);
                        console.log("name:", name, "module_name:", find_module.name, "offset:", offset);

                    }
                }
            }
        });
    }
}

setImmediate(hook_RegisterNatives);
