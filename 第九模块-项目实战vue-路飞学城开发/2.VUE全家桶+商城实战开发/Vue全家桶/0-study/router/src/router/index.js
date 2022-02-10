import Vue from 'vue'
// 1导入vue-router
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
// 2模块化机制使用router
Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    // redirect:'/home',
    redirect:{name:'Home'}   // 路由重定向
  },
  {
    path: '/home',
    name: 'Home',
    // component: Home
    components:{   // 主页显示两个视图页面  
      default: Home,//默认的名字
      main: () => import('../views/Main.vue'),
      sideBar: () => import('../views/SideBar.vue')
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/user/:id',
    name:'user',
    component:() => import('../views/User.vue'),
    // props:true  // true的时候只能传一个id 路由组件传值
    props: (route) => ({  
      id: route.params.id,
      title: route.query.title
    }),
    // 嵌套路由
    children:[
      {
        path:'profile',
        component:() => import('../views/Profile.vue')
      },
      {
        path:'posts',
        component:() => import('../views/Posts.vue')
      }
    ],
  },
  {
    path: '/notes',
    name: 'notes',
    component: () => import('@/views/Notes'),
    meta: {
        // 加到黑名单
        requireAuth: true
      }
  },
  {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login')
  },
  {
    path: '/editor',
    name: 'editor',
    component: () => import('@/views/Editor')
  },
  {
    path:'/page',
    name:'page',
    component:() => import('../views/Page.vue'),
    alias:'/aaa'   //别名

  },
  {
    path:'/user-*',
    component:() => import('../views/User-admin.vue')
  },
  {
    path:'*',
    component:() => import('../views/404.vue')
  },

]
// 3.创建路由器对象
const router = new VueRouter({
  mode:'history', //history 历史模式 干净的网页地址
  routes
})
// 抛出路由对象
export default router
