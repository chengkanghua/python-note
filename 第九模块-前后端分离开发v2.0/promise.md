

# 1.Promise

**示例1：**

```javascript
var p = new Promise((resolve, reject) => {
    // resolve(111);
    // reject(222);
})

p.then((res)=>{
    console.log(res);
},(err)=>{
    console.log(err);
})
```

```javascript
var p = Promise.resolve("哈哈哈"); // 创建Promise并执行resolve方法
p.then((res) => {
    console.log(1);
},(res) => {
    console.log(2);
})
```

```javascript
var p = Promise.reject("哈哈哈"); // 创建Promise并执行reject方法
p.then((res) => {
    console.log(1);
},(res) => {
    console.log(2);
})
```



**示例2**

```javascript
var p = Promise.resolve("哈哈哈"); // 创建Promise并执行resolve方法
p.then((res) => {
    console.log(1);
}, (res) => {
    console.log(2);
})

p.then((res) => {
    console.log(11);
}, (res) => {
    console.log(22);
})

p.then((res) => {
    console.log(111);
}, (res) => {
    console.log(222);
})
```

```javascript
var p = Promise.reject("哈哈哈"); // 创建Promise并执行resolve方法
p.then((res) => {
    console.log(1);
}, (res) => {
    console.log(2);
})

p.then((res) => {
    console.log(11);
}, (res) => {
    console.log(22);
})

p.then((res) => {
    console.log(111);
}, (res) => {
    console.log(222);
})
```



**示例3**

```javascript
var p = Promise.resolve("哈哈哈"); // 创建Promise并执行resolve方法
p.then((res) => {
    console.log(1,res);
    return res+"1";
}, (res) => {
    console.log(2);
})

p.then((res) => {
    console.log(11,res);
    return res+"1";
}, (res) => {
    console.log(22);
})

p.then((res) => {
    console.log(111,res);
}, (res) => {
    console.log(222);
})
```



**示例4**

```javascript
var p1 = Promise.resolve("哈哈哈"); // 创建Promise并执行resolve方法
p2 = p1.then((res) => {
    console.log(1,res);
    return res+"1";
}, (res) => {
    console.log(2);
})

p3 = p2.then((res) => {
    console.log(11,res);
    return res+"1";
}, (res) => {
    console.log(22);
})

p4 =  p3.then((res) => {
    console.log(111,res);
    return res+"1";
}, (res) => {
    console.log(222);
})
```



**示例5**

```javascript
var p = Promise.resolve("哈哈哈"); // 创建Promise并执行resolve方法
p = p.then((res) => {
    console.log(1,res);
    console.og(1,res);
    return res+"1";
}, (res) => {
    console.log(2);
})

p = p.then((res) => {
    console.log(11,res);
    return res+"1";
}, (res) => {
    console.log(22);
    return Promise.reject(res);
})

p =  p.then((res) => {
    console.log(111,res);
    return res+"1";
}, (res) => {
    console.log(222);
})
```



































# 2.axios拦截器（原理）

axios的拦截器是基于promise实现的。

```javascript
// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
}, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});
```

