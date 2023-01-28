// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
import axios from 'axios';


Vue.config.productionTip = false;

// 项目核心配置文件
Vue.prototype.$settings = settings;
// ElementUI配置
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css";

// 全局初始化样式
import "../static/css/reset.css";
// 全局导入字体图标
import "../static/css/iconfont.css";
import "../static/css/iconfont.eot";
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// 注册ElementUI插件
Vue.use(ElementUI);
// 注册mavon-editor组件
Vue.use(mavonEditor);
// 初始化axios
// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = false;
Vue.prototype.$axios = axios; // 把对象挂载vue中

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
