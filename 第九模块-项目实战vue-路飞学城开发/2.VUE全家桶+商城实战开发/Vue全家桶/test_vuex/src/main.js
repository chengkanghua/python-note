import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 导入创建的store
import store from './store'
Vue.config.productionTip = false
// 注册全局组件的方式
import ShoppingCart from '@/components/ShoppingCart';
Vue.component(ShoppingCart.name, ShoppingCart)
// 全局注册过滤器
Vue.filter('currency',(value)=>{
  return '$' + value;
})

new Vue({
  router,
  //一定要挂载
  store,
  render: h => h(App)
}).$mount('#app')
