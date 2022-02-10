import Vue from 'vue'
import App from './App.vue'
import router from './router'  // 这里会自动加载目录下的index  ./router/index

// 全局守卫
router.beforeEach((to,from,next)=>{
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
}) 
Vue.config.productionTip = false

new Vue({
  // 4 挂载到vue实例中挂载  
  router,
  render: h => h(App)
}).$mount('#app')
