package com.douyin.hook;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.util.Base64;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.bilibili.nativelibrary.LibBili;
import com.bilibili.nativelibrary.SignedQuery;

import org.json.JSONException;
import org.json.JSONObject;

import java.awt.font.NumericShaper;
import java.security.GeneralSecurityException;
import java.util.Map;
import java.util.TreeMap;

import okhttp3.FormBody;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

import java.security.Key;
import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.PrivateKey;
import java.security.spec.X509EncodedKeySpec;
import java.security.spec.PKCS8EncodedKeySpec;

import javax.crypto.Cipher;


public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    private Button btnStart;
    private Button btnStop;
    private EditText txtHost;

    private static boolean status = false;

    private Context mContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initView();
        initListener();
    }

    /**
     * 初始化页面视图
     */
    private void initView() {

        mContext = MainActivity.this;

        btnStart = findViewById(R.id.btn_start);
        btnStop = findViewById(R.id.btn_stop);
        txtHost = findViewById(R.id.txt_host);
    }

    /**
     * 初识监听事件
     */
    private void initListener() {
        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        status = true;
                        clickStart();
                    }
                }).start();

            }
        });

        btnStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                status = false;
            }
        });


    }


    private void clickStart() {
        // 开始死循环，从url获取参数，根据so文件生成sign，然后给用户返回。
        String host = String.valueOf(txtHost.getText());
        while (status) {
            try {
                String res = "error";
                do {
                    Log.e(TAG, "获取任务");
                    res = requestGet(String.format("http://%s/sign/task/", host));

                } while (res.equals("error"));

                // 获取任务JSON
                JSONObject json = new JSONObject(res);
                String uid = (String) json.get("uid");
                String sign_type = (String) json.get("sign_type");
                String param_string = (String) json.get("param_string");

                // 2. 生成TreeMap
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


                // 3. 根据sign_type，决定调用 LibBili.g 或 LibBili.h
                SignedQuery query;
                if (sign_type.equals("1")) {
                    query = LibBili.g(v1);
                } else {
                    query = LibBili.h(v1, 1, 0);
                }
                String totalString = query.toString();


                // 4. 签名后的结果发送给Flask服务
                JSONObject object = new JSONObject();
                object.put("uid", uid);
                object.put("total_string", totalString);
                requestPost(String.format("http://%s/sign/", host), object);

            } catch (Exception ex) {
                Log.e(TAG, "处理sign失败: " + ex.toString());
            }
        }
    }

    /**
     * 发送GET请求
     *
     * @param url
     * @return
     */
    public String requestGet(String url) {  //这里没有返回，也可以返回string
        OkHttpClient mOkHttpClient = new OkHttpClient();
        Request request = new Request
                .Builder()
                .url(url)
                .build();
        try (Response response = mOkHttpClient.newCall(request).execute()) {
            return response.body().string();
        } catch (Exception e) {
            Log.e(TAG, "GET请求失败: " + e.toString());
            return null;
        }
    }

    /**
     * 发送POST请求
     *
     * @param url
     * @param json
     * @return
     */
    public String requestPost(String url, JSONObject json) {  //这里没有返回，也可以返回string
        MediaType JSON = MediaType.parse("application/json; charset=utf-8");
        OkHttpClient mOkHttpClient = new OkHttpClient();
        RequestBody body = RequestBody.create(JSON, json.toString());
        Request request = new Request
                .Builder()
                .post(body)
                .url(url)
                .build();
        try (Response response = mOkHttpClient.newCall(request).execute()) {
            return response.body().string();
        } catch (Exception e) {
            return null;
        }
    }
}