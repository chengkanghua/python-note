package com.bilibili.nativelibrary;
import com.bilibili.nativelibrary.SignedQuery;

import java.security.InvalidKeyException;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

import javax.crypto.spec.IvParameterSpec;

public class LibBili {
    public static final int a = 0;
    public static final int b = 1;
    public static final int c = 0;
    public static final int d = 1;
    public static final int e = 2;
    public static final int f = 3;

    static {
        System.loadLibrary("bili");
    }

    private static native String a(String arg0);

    private static native String ao(String arg0, int arg1, int arg2);

    private static native IvParameterSpec b(String arg0) throws InvalidKeyException;

    public static SignedQuery g(Map arg1) {
        TreeMap v1 = arg1 == null ? new TreeMap() : new TreeMap(arg1);
        return LibBili.s(((SortedMap) v1));
    }

    public static SignedQuery h(Map arg1, int arg2, int arg3) {
        TreeMap v1 = arg1 == null ? new TreeMap() : new TreeMap(arg1);
        return LibBili.so(((SortedMap)v1), arg2, arg3);
    }

    public static native int getCpuCount();

    @Deprecated
    public static native int getCpuId();

    static native SignedQuery s(SortedMap arg0);

    static native SignedQuery so(SortedMap arg0, int arg1, int arg2);

    static native SignedQuery so(SortedMap arg0, byte[] arg1);

}
