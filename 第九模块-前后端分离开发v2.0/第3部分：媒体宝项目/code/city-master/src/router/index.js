import Vue from 'vue'
import VueRouter from 'vue-router'
import {getToken} from '@/plugins/cookie'

Vue.use(VueRouter)

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login.vue')
    },
    {
        path: '/',
        name: 'Layout',
        component: () => import('../views/Layout.vue'),
        children: [
            {
                path: "",
                redirect: "task",
            },
            {
                path: 'task',
                name: 'Task',
                component: () => import('../views/task/TaskLayout.vue'),
                children: [
                    {
                        path: "/",
                        redirect: "activity"
                    },
                    {
                        path: "activity",
                        name: 'Activity',
                        component: () => import('../views/task/Activity.vue'),
                        children: [
                            {
                                path: "/",
                                redirect: "list"
                            },
                            {
                                path: "list",
                                name: 'ActivityList',
                                component: () => import('../views/task/ActivityList.vue'),
                            },
                            {
                                path: "create",
                                name: 'ActivityCreate',
                                component: () => import('../views/task/ActivityCreate.vue'),
                            }
                        ]

                    },
                    {
                        path: "promo",
                        name: 'Promo',
                        component: () => import('../views/task/Promo.vue'),
                    },
                    {
                        path: "stat",
                        name: 'Stat',
                        component: () => import('../views/task/Stat.vue'),
                    },
                    {
                        path: "fans",
                        name: 'Fans',
                        component: () => import('../views/task/Fans.vue'),
                    },
                ]
            },
            {
                path: 'msg',
                name: 'Msg',
                component: () => import('../views/msg/MsgLayout.vue'),
                children: [
                    {
                        path: "/",
                        redirect: "push"
                    },
                    {
                        path: "push",
                        name: 'Push',
                        component: () => import('../views/msg/Push.vue'),
                    },
                    {
                        path: "sop",
                        name: 'Sop',
                        component: () => import('../views/msg/Sop.vue'),
                    },
                ]
            },
            {
                path: 'auth',
                name: 'Auth',
                component: () => import('../views/auth/Auth.vue'),
            }
        ]
    },
    {
        path: '/*',
        component: () => import('../views/NotFound.vue')
    }
]

const router = new VueRouter({
    routes,
    mode: "history"
})

router.beforeEach((to, from, next) => {
    let token = getToken();

    // 如果已登录，则可以继续访问目标地址
    if (token) {
        next();
        return;
    }
    // 未登录，访问登录页面
    if (to.name === "Login") {
        next();
        return;
    }

    // 未登录，跳转登录页面
    next({name: 'Login'});
})



export default router
