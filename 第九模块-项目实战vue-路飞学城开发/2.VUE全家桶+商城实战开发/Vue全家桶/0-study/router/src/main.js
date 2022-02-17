import Vue from 'vue'
import App from './App.vue'
import router from './router'  // 这里会自动加载目录下的index  ./router/index
import axios from 'axios';
Vue.prototype.$https = axios;


// 全局守卫
/* router.beforeEach((to,from,next)=>{
  // console.log(to)
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
})  */

router.beforeEach((to,from,next)=>{
    if(to.matched.some(record=>record.meta.requireAuth)){
      //需要权限,在黑名单
      if(!localStorage.getItem('user')){
        next({
          path:'/login',  // 跳转 login页面
          query:{ // 跳转之前的地址添加到 login?后面
            redirect:to.fullPath
          }
        })
      }else{
        next();
      }
    }
    //白名单
    next();
})

Vue.config.productionTip = false

new Vue({
  // 4 挂载到vue实例中挂载  
  router,
  render: h => h(App)
}).$mount('#app')
