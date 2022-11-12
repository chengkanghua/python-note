package com.nb.day09;

// com.nb.day09.encryptUtils
class encryptUtils {
    static {
        System.loadLibrary("encrypt");
    }
    public static native int add(int v1, int v2);

    public static native String sign(String origin);
}
