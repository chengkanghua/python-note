package com.nb.city;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class MainActivity extends AppCompatActivity {

    public Button btnLogin, btnReset;
    public TextView txtUser, txtPwd;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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

        // 2.POST请求
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
    }
}