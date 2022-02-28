import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login/Login'
import Index from '@/components/Login/Index'
Vue.use(Router)

// 配置路由规则
export default new Router({
   linkActiveClass:'is-active',
   mode: 'history',//改成history模式
  routes: [
    {
      path: '/',
      redirect:'/Login'
      // component: HelloWorld
    },
    {
    	path:"/index",
    	name:'Index',
    	component:Index
    },
    {
      path:'/login',
      name:'Login',
      component:Login
    },

  ]
})
