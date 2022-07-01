# day09 安卓和JNI开发

- 安卓开发，app【java开发，JEB、JADX】。
- JNI开发，核心算法C/C++开发 + JNI + 安卓。



## 1.安卓开发

- 登录界面

- okhttp包，将请求发送到API接口。

  - okhttp，GET请求（路飞的API为例）

  - okhttp，POST请求（路飞API为例）+ Form【user=wupeiqi&pwd=123】

  - okhttp，POST请求 + JSON格式

    ```python
    data = {
        "username":"wupeiqi",
        "pwd":"123"
    }
    ```

    ```java
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
    
                        Log.i("登录界面--->", resString);
                        // 获取数据并处理
    
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }.start();
    ```



### 1.1 序列化 Gson

- 引入

  ```
  implementation 'com.google.code.gson:gson:2.8.6'
  ```

- 序列化

  ```java
  package com.nb.city;
  
  class HttpContext {
      public int code;
      public String message;
  
      public HttpContext(int code, String msg) {
          this.code = code;
          this.message = msg;
      }
  }
  
  HttpContext context = new HttpContext(1000,"成功");
  
  // 序列化成JSON字符串
  String jsonData = new Gson().toJson(context);
  ```

- 反序列化

  ```
  {
  	"origin":"110.248.149.62",
  	"url:"https://www.httpbin.org/post",
  	"dataList":[
  		{"id":1,"name":"武沛齐"},
  		{"id":1,"name":"武沛齐"}
  	]
  }
  ```

  ```python
  class Item{
      public int id;
      pubiic String name;
  }
  
  class HttpResponse{
      public String url;
  	public String origin;
  	public ArryList<Item> dataList;
  }
  
  
  
  
  String responseString = "{\"origin\": \"110.248.149.62\",\"url\": \"https://www.httpbin.org/post\",\"dataList\":[{\"id\":1,\"name\":\"武沛齐\"},{\"id\":2,\"name\":\"eric\"}]}";
  
  HttpResponse res = new Gson().fromJson(responseString, HttpResponse.class);
  res.url
  res.origin
  res.dataList
  ```



### 1.2 保存到xml中

登录

```
SharedPreferences sp = getSharedPreferences("sp_city", MODE_PRIVATE);
SharedPreferences.Editor editor = sp.edit();
editor.putString("token",res.token);
editor.commit();
```



注销

```java
SharedPreferences sp = getSharedPreferences("sp_city", MODE_PRIVATE);
SharedPreferences.Editor editor = sp.edit();
editor.remove("token");
editor.commit();
```



读取

```python
SharedPreferences sp = getSharedPreferences("sp_city", MODE_PRIVATE);
String token = sp.getString("token","");

```



注意：不仅还会存储一些，初始化设备ID（抖音cdid），手机中的数据清空（应用清楚所有数据）。



### 1.3 跳转

```
Intent in = new Intent(mContext, IndexActivity.class);
startActivity(in);
```



### 1.4 网络请求相关补充

#### 1.OKHttp

```java
new Thread() {
    @Override
    public void run() {
        OkHttpClient client = new OkHttpClient();

        JSONObject json = new JSONObject(dataMap);
        String jsonString = json.toString();
        RequestBody form = RequestBody.create(MediaType.parse("application/json;charset=utf-8"), jsonString);
        
        // 请求头中添加  x-gorgon="sdfkkkkjfsdfsdf"
        Request request = new Request.Builder().url("https://api.luffycity.com/api/v1/auth/password/login/?loginWay=password").post(form).build();
        Call call = client.newCall(request);
        try {
            Response response = call.execute(); // 发送请求
            ResponseBody body = response.body();
            String resString = body.string();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}.start();
```

#### 2.OKhttp拦截器

```java
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

```





### 1.5 网络请求retrofit

retrofit是在OKHttp请求的基础上又封装了一层，让我们发送请求时候就可以更加的简单。（B站）

- 配置

  ```
  // implementation "com.squareup.okhttp3:okhttp:4.9.1"
  implementation "com.squareup.retrofit2:retrofit:2.9.0"
  ```

- “接口”

  ```java
  package com.nb.luffy;
  
  import okhttp3.RequestBody;
  import okhttp3.ResponseBody;
  import retrofit2.Call;
  import retrofit2.http.Body;
  import retrofit2.http.Field;
  import retrofit2.http.FormUrlEncoded;
  import retrofit2.http.POST;
  import retrofit2.http.GET;
  import retrofit2.http.Query;
  
  public interface HttpRequest {
  
      @POST("/api/v1/post")
      @FormUrlEncoded
      Call<ResponseBody> postLogin(@Field("name") String userName, @Field("pwd") String password);
  
      @GET("/api/v2/xxx")
      Call<ResponseBody> getInfo(@Query("age") String age);
  
      @POST("/post")
      Call<ResponseBody> postLoginJson(@Body RequestBody body);
  
      @GET("/index")
      Call<ResponseBody> getIndex(@Query("age") String age);
  }
  
  ```

- 发送请求

  ```java
  new Thread() {
      @Override
      public void run() {
          Retrofit retrofit = new Retrofit.Builder().baseUrl("http://api.baidu.com/").build();
          HttpRequest httpRequest = retrofit.create(HttpRequest.class);
          Call<ResponseBody> call = httpRequest.login("wupeiqi","123123");
          try {
              ResponseBody responseBody = call.execute().body();
              String responseString = responseBody.string();
              Log.i("登录", responseString);
  
          } catch (Exception e) {
              e.printStackTrace();
          }
      }
  }.start();
  ```

  ```
  http://api.baidu.com/api/v1/post
  n1=wupeiqi&n2=123123
  ```



提示：jadx打开B站：关键字：`x/report/andriod2`



### 总结

jadx、jeb去反编译安卓代码：

- 关键字搜索
- 根据请求的流程去逐步查找
- Java调用关系

注意：地方、小app一般了解上面的东西完全都可以给他逆向出来。































































