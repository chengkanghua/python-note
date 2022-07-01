import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("tv.danmaku.bili")

scr = """
Java.perform(function () {
    
    // Hook必须用真机 arm
    var libbili = Module.findBaseAddress("libbili.so");
    
    var s_func = libbili.add(0x22b0 + 1);
    
    Interceptor.attach(s_func, {
        onEnter: function (args) {
            // args[0]
            // args[1]，字符串
            // args[2]，字符串长度
            // console.log(args[1])，内存地址
            // hexdump(内存地址, { length:长度 }) -> 二进制 -> 字符串显示。
            // console.log("执行update，长度是：",args[2]);
            console.log(hexdump(args[1], {length: args[2].toInt32()}));
        },
        onLeave: function (args) {
            console.log("=======================结束===================");
        }
    });
});
"""
script = session.create_script(scr)


def on_message(message, data):
    pass


script.on("message", on_message)
script.load()
sys.stdin.read()
