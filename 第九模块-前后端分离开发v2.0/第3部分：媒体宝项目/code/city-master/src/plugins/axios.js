import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import {getToken} from "@/plugins/cookie"
import router from '../router/index'
import store from '../store/index'
import {Message} from "element-ui"

Vue.use(VueAxios, axios)


// 设置默认值
// axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
// axios.defaults.baseURL = 'http://124.222.193.204:8000/api/';
// axios.defaults.headers.common['Authorization'] = getToken();  // 只在页面刷新时才执行
// axios.defaults.headers.post['Content-Type'] = 'application/json';
// axios.defaults.headers.put['Content-Type'] = 'application/json';


// 请求拦截器，axios发送请求时候，每次请求
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    const token = getToken();
    if (token) {
        // 表示用户已登录
        config.headers.common['Authorization'] = token;
    }
    return config;
});

// 响应拦截器
axios.interceptors.response.use(function (response) {
    // API请求执行成功，响应状态码200，自动执行
    if (response.data.code === "2000") {
        // store中的logout方法
        store.commit("logout");
        // 重定向登录页面  [Login,]
        // router.push({name:"Login"});
        router.replace({name: "Login"});

        // 页面提示
        Message.error("认证过期，请重新登录...");

        return Promise.reject(); // 下一个相应拦截器的第二个函数
    }

    return response;

}, function (error) {
    // API请求执行失败，响应状态码400/500，自动执行
    if (error.response.status === 401) {
        // store中的logout方法
        store.commit("logout");
        // 重定向登录页面  [Login,]
        // router.push({name:"Login"});
        router.replace({name: "Login"});
        Message.error("认证过期，请重新登录...");
        // return
    }
    return Promise.reject(error);  // 下一个相应拦截器的第二个函数
});
