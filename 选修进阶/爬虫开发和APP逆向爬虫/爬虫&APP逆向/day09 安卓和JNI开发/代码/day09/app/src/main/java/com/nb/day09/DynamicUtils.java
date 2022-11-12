package com.nb.day09;

class DynamicUtils {
    static {
        System.loadLibrary("dynamic");
    }

    public static native int add(int v1, int v2);
}
