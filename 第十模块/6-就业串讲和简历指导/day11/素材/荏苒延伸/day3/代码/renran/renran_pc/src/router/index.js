import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

import Home from "@/components/Home";
import Login from "@/components/Login"
import Register from "@/components/Register"
import FindPassword from "@/components/FindPassword"
import ResetPassword from "@/components/ResetPassword"
import QQCallBack from "@/components/QQCallBack"
import Write from "@/components/Write"
import Writed from "@/components/Writed"
import Article from "@/components/Article"
import Wallet from "@/components/Wallet"
import Search from "@/components/Search"
import ChatList from "@/components/ChatList"
import Chat from "@/components/Chat"


export default new Router({
  mode: "history",
  routes: [
     {
       name:"Home",
       path:"/",
       component:Home,
     },
      {
       name:"Home",
       path:"/home",
       component:Home,
     },
      {
       name:"Login",
       path:"/user/login",
       component:Login,
     },
      {
       name:"Register",
       path:"/user/register",
       component: Register,
     },
      {
       name:"FindPassword",
       path:"/find_password",
       component: FindPassword,
     },
      {
       name:"ResetPassword",
       path:"/reset_password",
       component: ResetPassword,
     },
      {
       name:"QQCallBack",
       path:"/oauth_callback.html",
       component: QQCallBack,
     },
      {
       name:"Write",
       path:"/writer",
       component: Write,
     },
      {
       name:"Writed",
       path:"/:id/writed",
       component: Writed,
     },
      {
       name:"Article",
       path:"/article/:id",
       component: Article,
     },
      {
       name:"Wallet",
       path:"/user/wallet",
       component: Wallet,
     },
      {
       name:"Search",
       path:"/search",
       component: Search,
     },
      {
       name:"ChatList",
       path:"/chat",
       component: ChatList,
     },
      {
       name:"Chat",
       path:"/chat/:chat_id",
       component: Chat,
     },
  ]
})
