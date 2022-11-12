package com.douyin.hook;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;
import android.text.format.Time;
import android.util.Log;

import com.bilibili.nativelibrary.LibBili;
import com.bilibili.nativelibrary.SignedQuery;

import org.json.JSONObject;

import java.util.TreeMap;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class HookSoService extends Service {
    // 定义个一个Tag标签
    private static final String TAG = "HookSoService";
    public static String Host = "192.168.0.6:5000";
    public static Thread taskThread = null;


    // 一个Binder类，用在onBind()有方法里，这样Activity那边可以获取到
    private MyBinder mBinder = new MyBinder();

    public IBinder onBind(Intent intent) {
        Log.e(TAG, "start IBinder~~~");
        return mBinder;
    }

    public void onCreate() {
        Log.e(TAG, "start onCreate~~~");
        super.onCreate();

        taskThread = new Thread(new Runnable() {
            @Override
            public void run() {
                doTask();
            }
        });
        taskThread.start();
    }

    public void doTask() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                clickStart();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public void onStart(Intent intent, int startId) {
        Log.e(TAG, "start onStart~~~");
        super.onStart(intent, startId);
    }

    public void onDestroy() {
        super.onDestroy();

        Log.e(TAG, "start onDestroy~~~");

        if (taskThread != null) {
            taskThread.interrupt();
            Log.e(TAG, "start onDestroy~~~1111");
        }

    }

    public boolean onUnbind(Intent intent) {
        Log.e(TAG, "start onUnbind~~~");
        return super.onUnbind(intent);
    }

    public class MyBinder extends Binder {
        HookSoService getService() {
            return HookSoService.this;
        }
    }


    private void clickStart() {
        // 开始死循环，从url获取参数，根据so文件生成sign，然后给用户返回。
        try {
            Log.e(TAG, "循环");
            // 1. 发送网络请求，获取json格式数据。 {uid:'...', param_string:'...' }
            String res = "error";
            do {
                Log.e(TAG, "获取任务");
                res = requestGet(String.format("http://%s/sign/task/", Host));
            } while (res.equals("error"));

            JSONObject json = new JSONObject(res);
            String uid = (String) json.get("uid");
            String sign_type = (String) json.get("sign_type");
            String param_string = (String) json.get("param_string");

            // 2. 生成TreeMap
            TreeMap v1 = new TreeMap();
            String[] itemList = param_string.split("&");
            for (String item : itemList) {
                String[] kv = item.split("=");
                v1.put(kv[0], kv[1]);
            }

            // 3. 创建sign
            SignedQuery query;
            if (sign_type.equals("1")) {
                query = LibBili.g(v1);
            } else {
                query = LibBili.h(v1, 1, 0);
            }
            String totalString = query.toString();
            // 4. 发送给调用者

            JSONObject object = new JSONObject();
            object.put("uid", uid);
            object.put("total_string", totalString);
            requestPost(String.format("http://%s/sign/", Host), object);

        } catch (Exception ex) {
            Log.e(TAG, "处理sign失败: " + ex.toString());
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
            return "error";
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
            return "error";
        }
    }
}
