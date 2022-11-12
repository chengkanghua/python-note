import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';
Vue.prototype.$https = axios;
Vue.config.productionTip = false

// 全局守卫
/* router.beforeEach((to,from,next)=>{
  // 用户访问了/notes
  if(to.path === '/notes'){
    // 获取用户登录的信息
    const user = JSON.parse(localStorage.getItem('user'));
    if(user){
      // 用户已登录
      next();
    }else{
      // 用户没有登录 跳转到登录页面进行登录
      next('/login');
    }
  }
  next();
}) */
router.beforeEach((to, from, next) => {
  if(to.matched.some(record=>record.meta.requireAuth)){
    // 需要权限,在黑名单
    if(!localStorage.getItem('user')){
      next({
        path:'/login',
        query:{
          redirect:to.fullPath
        }
      })
    }else{
      next();
    }
  }
  // 在白名单
  next();
})

new Vue({
  // 4.挂载到vue的实例中
  router,
  render: h => h(App)
}).$mount('#app')
