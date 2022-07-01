package com.bilibili.nativelibrary;

import android.text.TextUtils;
import android.util.Log;

import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

import android.text.TextUtils;

import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

public final class SignedQuery {
    public final String a;
    public final String b;
    private static char[] c;

    static {
        SignedQuery.c = "0123456789ABCDEF".toCharArray();
    }

    public SignedQuery(String arg1, String arg2) {
        super();
        Log.e("init", arg1);
        Log.e("init", String.valueOf(arg2));
        this.a = arg1;
        this.b = arg2;
    }

    private static boolean a(char arg2, String arg3) {
        return false;
    }

    static String b(String arg1) {
        return SignedQuery.c(arg1, null);
    }

    static String c(String arg9, String arg10) {
        return arg9;
    }

    static String r(Map arg4) {
        // Log.e("rrr", arg4.toString());
        // String str = "access_key=&appkey=1d8b6e7d45233436&build=6240300&buvid=XZ0BAA0094F75EE97BF6B1541ABA8B7F37D3C&c_locale=zh_CN&channel=bili&device=android&from_spmid=search.search-result.0.0&install_apps=&mobi_app=android&oid=803139487&platform=android&s_locale=zh_CN&share_id=main.ugc-video-detail.0.0.pv&share_origin=vinfo_share&sid=340411234&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.24.0%22%2C%22abtest%22%3A%22%22%7D&ts=1622890959";
        // String str = "actual_played_time=0&aid=803139487&appkey=1d8b6e7d45233436&auto_play=0&build=6240300&c_locale=zh_CN&channel=bili&cid=340411234&epid=0&epid_status=&from=64&from_spmid=main.my-history.0.0&last_play_progress_time=0&list_play_time=0&max_play_progress_time=0&mid=0&miniplayer_play_time=0&mobi_app=android&network_type=1&paused_time=0&platform=android&play_status=0&play_type=1&played_time=0&quality=32&s_locale=zh_CN&session=566f368d51b014ca76053f2491f59ed3aed579a8&sid=0&spmid=main.ugc-video-detail.0.0&start_ts=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.24.0%22%2C%22abtest%22%3A%22%22%7D&sub_type=0&total_time=0&ts=1622906721&type=3&user_status=0&video_duration=367";
        // return str;

        StringBuilder v0 = new StringBuilder(0x100);
        for (Object entry : arg4.entrySet()) {
            Object key = ((Map.Entry) entry).getKey();
            v0.append(SignedQuery.b(((String) key)));
            v0.append("=");

            Object value = ((Map.Entry) entry).getValue();
            String v1_1 = value == null ? "" : SignedQuery.b(((String) value));
            v0.append(v1_1);
            v0.append("&");
        }

        int v4_2 = v0.length();
        if (v4_2 > 0) {
            v0.deleteCharAt(v4_2 - 1);
        }
        String v4_3 = v4_2 == 0 ? null : v0.toString();
        return v4_3;

    }

    public String toString() {
        String v0 = this.a;
        if (v0 == null) {
            return "";
        }

        if (this.b == null) {
            return v0;
        } else {
        }
        return this.a + "&sign=" + this.b;
    }
}

