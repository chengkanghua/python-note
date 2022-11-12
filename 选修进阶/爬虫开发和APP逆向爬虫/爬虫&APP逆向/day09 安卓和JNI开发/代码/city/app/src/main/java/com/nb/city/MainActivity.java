package com.nb.city;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.android.material.shadow.ShadowRenderer;
import com.google.gson.Gson;

import org.jetbrains.annotations.NotNull;
import org.json.JSONObject;

import java.io.IOException;
import java.util.HashMap;

import okhttp3.Call;
import okhttp3.FormBody;
import okhttp3.Interceptor;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class MainActivity extends AppCompatActivity {
    public Context mContext;

    public Button btnLogin, btnReset;
    public TextView txtUser, txtPwd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mContext = this;

        // 页面的初始化
        initView();

        // 处理监听事件
        initListener();
    }

    private void initView() {
        // 方法在启动时会自动执行
        btnLogin = findViewById(R.id.btn_login);
        btnReset = findViewById(R.id.btn_reset);

        txtUser = findViewById(R.id.txt_user);
        txtPwd = findViewById(R.id.txt_pwd);
    }

    private void initListener() {

        btnReset.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 当重置按钮被点击时, 自动执行 onClick方法
                txtUser.setText("");
                txtPwd.setText("");
            }
        });

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 当登录按钮被点击时, 自动执行 onClick方法
                doLogin();
            }
        });

    }

    /**
     * 点击登录执行此方法
     */
    private void doLogin() {
        String username = String.valueOf(txtUser.getText());
        String password = String.valueOf(txtPwd.getText());

        HashMap<String, String> dataMap = new HashMap<String, String>();
        dataMap.put("username", username);
        dataMap.put("password", password);

        // 将用户名和密码发送到后台（第三方 OKHttp）
        //  1.引入依赖  implementation "com.squareup.okhttp3:okhttp:4.9.1"
        //  2.默认不允许发送网络请求，配置。 <uses-permission android:name="android.permission.INTERNET" />
        //  3.调用OKHttp包去发送请求

        // 1.如何发送GET请求【创建线程】
        // 创建线程并执行run方法
        /*
        new Thread() {
            @Override
            public void run() {
                OkHttpClient client = new OkHttpClient();
                Request request = new Request.Builder().url("https://api.luffycity.com/api/v1/course/actual/?category_id=1").build();
                Call call = client.newCall(request);
                try {
                    Response response = call.execute(); // 发送请求
                    ResponseBody body = response.body();
                    String resString = body.string();

                    Log.i("登录界面--->", resString);
                    // 获取数据并处理

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
         */

        // 2.POST请求(Form格式）
        /*
        new Thread() {
            @Override
            public void run() {
                OkHttpClient client = new OkHttpClient();

                FormBody form = new FormBody.Builder().add("username","wupeiqi").add("password","123").build();

                Request request = new Request.Builder().url("https://api.luffycity.com/api/v1/auth/password/login/?loginWay=password").post(form).build();
                Call call = client.newCall(request);
                try {
                    Response response = call.execute(); // 发送请求
                    ResponseBody body = response.body();
                    String resString = body.string();

                    Log.i("登录界面--->", resString);
                    // 获取数据并处理

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();
        */

        // 3.POST请求（JSON格式）
        /*
        new Thread() {
            @Override
            public void run() {
                OkHttpClient client = new OkHttpClient();

                // FormBody form = new FormBody.Builder().add("username","wupeiqi").add("password","123").build();

                // JSONObject json = new JSONObject();
                // json.put("username","wupeiqi");
                // json.put("password","123");

                JSONObject json = new JSONObject(dataMap);
                String jsonString = json.toString();
                RequestBody form = RequestBody.create(MediaType.parse("application/json;charset=utf-8"), jsonString);

                Request request = new Request.Builder().url("https://api.luffycity.com/api/v1/auth/password/login/?loginWay=password").post(form).build();
                Call call = client.newCall(request);
                try {
                    Response response = call.execute(); // 发送请求
                    ResponseBody body = response.body();
                    String resString = body.string();

                    // json字符串={"code":-1,"msg":"校验错误","data":{"global_error":["密码未设置，请使用短信登录"]}}
                    // json反序列化，字符串转化转换成对象。
                    // json.loads(json字符串)
                    String responseString = "{\"token\": \"uuyffsdkfjumfdkjsdf\",\"url\": \"https://www.httpbin.org/post\",\"dataList\":[{\"id\":1,\"name\":\"武沛齐\"},{\"id\":2,\"name\":\"eric\"}]}";
                    HttpResponse res = new Gson().fromJson(responseString, HttpResponse.class);
                    Log.e("登录界面------->", res.toString());
                    Log.i("登录界面--->", resString);
                    //  HttpResponse{url='https://www.httpbin.org/post', origin='110.248.149.62', dataList=[Item{id=1, name='武沛齐'}, Item{id=2, name='eric'}]}

                    // 保存起来：cookie、localstoreage
                    // xml文件: data/data/com.nb.city
                    // res.token
                    SharedPreferences sp = getSharedPreferences("sp_city", MODE_PRIVATE);
                    SharedPreferences.Editor editor = sp.edit();
                    editor.putString("token",res.token);
                    editor.commit();

                    // 跳转首页
                    Intent in = new Intent(mContext, IndexActivity.class);
                    startActivity(in);

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();

         */

        // 4.发送请求拦截器
        Interceptor interceptor = new Interceptor() {
            @NotNull
            @Override
            public Response intercept(@NotNull Chain chain) throws IOException {
                String sign = "sdfsdfsdf";
                // 请求还未发送，在请求体中增加了一个请求头
                Request request = chain.request().newBuilder().addHeader("x-gorgon", sign).build();
                Response response = chain.proceed(request);
                return response;
            }
        };

        new Thread() {
            @Override
            public void run() {
                OkHttpClient client = new OkHttpClient.Builder().addInterceptor(interceptor).build();

                // FormBody form = new FormBody.Builder().add("username","wupeiqi").add("password","123").build();

                // JSONObject json = new JSONObject();
                // json.put("username","wupeiqi");
                // json.put("password","123");

                JSONObject json = new JSONObject(dataMap);
                String jsonString = json.toString();
                RequestBody form = RequestBody.create(MediaType.parse("application/json;charset=utf-8"), jsonString);

                Request request = new Request.Builder().url("https://api.luffycity.com/api/v1/auth/password/login/?loginWay=password").post(form).build();
                Call call = client.newCall(request);
                try {
                    Response response = call.execute(); // 发送请求
                    ResponseBody body = response.body();
                    String resString = body.string();

                    // json字符串={"code":-1,"msg":"校验错误","data":{"global_error":["密码未设置，请使用短信登录"]}}
                    // json反序列化，字符串转化转换成对象。
                    // json.loads(json字符串)
                    String responseString = "{\"token\": \"uuyffsdkfjumfdkjsdf\",\"url\": \"https://www.httpbin.org/post\",\"dataList\":[{\"id\":1,\"name\":\"武沛齐\"},{\"id\":2,\"name\":\"eric\"}]}";
                    HttpResponse res = new Gson().fromJson(responseString, HttpResponse.class);
                    Log.e("登录界面------->", res.toString());
                    Log.i("登录界面--->", resString);
                    //  HttpResponse{url='https://www.httpbin.org/post', origin='110.248.149.62', dataList=[Item{id=1, name='武沛齐'}, Item{id=2, name='eric'}]}

                    // 保存起来：cookie、localstoreage
                    // xml文件: data/data/com.nb.city
                    // res.token
                    SharedPreferences sp = getSharedPreferences("sp_city", MODE_PRIVATE);
                    SharedPreferences.Editor editor = sp.edit();
                    editor.putString("token", res.token);
                    editor.commit();

                    // 跳转首页
                    Intent in = new Intent(mContext, IndexActivity.class);
                    startActivity(in);

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }.start();

    }
}