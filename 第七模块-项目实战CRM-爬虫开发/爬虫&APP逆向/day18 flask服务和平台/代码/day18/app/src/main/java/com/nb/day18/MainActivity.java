package com.nb.day18;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.bilibili.nativelibrary.LibBili;
import com.bilibili.nativelibrary.SignedQuery;

import java.util.TreeMap;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        String param_string = "abi=x86&appid=tv.danmaku.bili&appkey=1d8b6e7d45233436&brand=HUAWEI&build=6240300&channel=bili&env=prod&iv=6240300&mobi_app=android&model=Mate 10 Pro&nt=1&ov=23&screen=1872_1170@416.0_416.0&sn=5398898&vn=6.24.0";
        TreeMap v1 = new TreeMap();
        String[] itemList = param_string.split("&");
        for (String item : itemList) {
            String[] kv = item.split("=");
            if (kv.length == 2) {
                v1.put(kv[0], kv[1]);
            } else {
                v1.put(kv[0], "");
            }

        }

        SignedQuery query = LibBili.g(v1);

        String totalString = query.toString();
        Log.e("加密后的参数--->", totalString);
    }
}