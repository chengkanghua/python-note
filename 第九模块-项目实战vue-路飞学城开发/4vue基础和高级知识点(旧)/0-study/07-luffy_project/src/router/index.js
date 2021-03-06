import Vue from 'vue'
import Router from 'vue-router'
// @ 绝对路径 检索到 .....src/

// 如果我们Router当做局部模块使用 一定要Vue.use(Router)
// 以后在组件中  可以通过this.$router  获取Router实例化对象
// 路由信息对象 this.$routes
import Home from '@/components/Home/Home'
import Course from '@/components/Course/Course'
import LightCourse from '@/components/LightCourse/LightCourse'
import Micro from '@/components/Micro/Micro'
import CourseDetail from '@/components/Course/CourseDetail'
import Login from '@/components/Login/Login'
import Register from '@/components/Login/Register'
import Cart from '@/components/Cart/Cart'
import Study from '@/components/Study/Study'
import Homework from '@/components/Study/Homework'

Vue.use(Router)

// 配置路由规则
export default new Router({
   linkActiveClass:'is-active',
   mode: 'history',//改成history模式
  routes: [
    {
      path: '/',
      redirect:'/home'
      // component: HelloWorld
    },
    {
    	path:"/home",
    	name:'Home',
    	component:Home
    },
    {
    	path:"/course",
    	name:'Course',
    	component:Course
    },
    {
    	path:"/home/light-course",
    	name:'LightCourse',
    	component:LightCourse
    },
    {
    	path:"/micro",
    	name:'Micro',
    	component:Micro
    },
    // 课程详情
    {
      path:"/course/detail/:detailId",
      name:'course.detail',
      component:CourseDetail
    },
    {
      path:'/login',
      name:'Login',
      component:Login
    },
    {
      path:'/register',
      name:'Register',
      component:Register
    },
    // 购物车的页面
    {
      path:"/purchase/shopping_cart",
      name:'purchase.shop',
      component:Cart
    },
    // 学习中心
    {
      path:"/study",
      name:'Study',
      component:Study
    },
    // 模块作业
    {
      path:"/study/homework",
      name:'Homework',
      component:Homework
    }
  ]
})
