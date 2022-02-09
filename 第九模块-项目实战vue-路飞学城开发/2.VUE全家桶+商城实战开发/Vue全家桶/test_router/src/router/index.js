import Vue from 'vue';
// 1.导入
import VueRouter from 'vue-router';
// 2.模块化机制 使用Router
Vue.use(VueRouter)
import Home from '@/views/Home';
import About from '@/views/About';
import User from '@/views/User';

// 3.创建路由器对象
export default new VueRouter({
    mode: 'history', //history模式 干净的网页地址
    routes: [
        {
            path: '/',
            // redirect:'/home'
            redirect: { name: 'home' }
        },
        {
            path: "/home",
            name: 'home',
            // component: Home
            components: {
                default: Home,//默认的名字
                main: () => import('@/views/Main'),
                sideBar: () => import('@/views/SideBar'),
            }
        },
        // 同一个路径可以匹配多个路由,匹配的优先级按照路由的定义顺序:
        // 谁先定义的,谁的优先级最高
        {
            path: '/about',
            name: 'about',
            component: About
        },
        // {
        //     path: '/about',
        //     name: "about",
        //     component: Home
        // },

        {
            path: '/user/:id',
            name: 'user',
            component: User,
            // props:true
            props: (route) => ({
                id: route.params.id,
                title: route.query.title
            }),
            children: [
                {
                    path: 'profile',
                    component: () => import('@/views/Profile')
                },
                {
                    path: 'posts',
                    component: () => import('@/views/Posts')
                }
            ],
            meta: {
                // 加到黑名单
                requireAuth: true
            }

        },
        {
            path: '/post',
            name: "post",
            component: () => import('@/views/Post')
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
            path: '/eaditor',
            name: 'eaditor',
            component: () => import('@/views/Eaditor')
        },
        // http://localhost:8080/page?id=1&title=foo  query
        {
            path: '/page',
            name: 'page',
            component: () => import('@/views/Page'),
            alias: '/aaa' //给路由别名 
        },
        {
            path: "/blog",
            name: 'blog',
            component: () => import('@/views/Blog'),
            meta: {
                // 加到黑名单
                requireAuth: true
            }
        },
        {
            path: '/user-*',
            component: () => import('@/views/User-admin')
        },
        {
            path: '*',
            component: () => import('@/views/404')
        }
    ]
})

// http://localhost:8080/user/1
// http://localhost:8080/user/2
// 同一个页面
