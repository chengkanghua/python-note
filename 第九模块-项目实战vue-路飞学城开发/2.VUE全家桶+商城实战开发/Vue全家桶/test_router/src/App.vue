<template>
  <div id="app">
    <!-- router-link相当于a标签 to属性相当于a标签的href -->
    <!-- <router-link to='/'>首页</router-link>|
    <router-link to='/about'>关于</router-link>-->
    <router-link :to="{name:'home'}">首页</router-link>|
    <router-link :to="{name:'about'}">关于</router-link>|
    <!-- 声明式 -->
    <router-link :to="{name:'user',params:{id:1}}">User1</router-link>|
    <router-link :to="{name:'user',params:{id:2}}">User2</router-link>|
    <router-link :to="{name:'page',query:{id:1,title:'foo'}}">Page</router-link>|
    <!-- 路由嵌套 -->
    <router-link to='/user/1/profile'>user/1/profile</router-link>|
    <router-link to='/user/1/posts'>user/1/posts</router-link>|
    <router-link :to='{name:"notes"}'>我的笔记</router-link>|
    <router-link :to='{name:"eaditor"}'>编辑</router-link>|
    <router-link :to='{name:"blog"}'>博客</router-link>|
    <router-link :to='{name:"post"}'>Post</router-link>|


    <!-- router-view相当于路由组件的出口 -->
    <!-- Home -->
    <router-view></router-view> 
    <router-view name='main' class="main"></router-view> 
    <router-view name='sideBar' class="sidebar"></router-view> 
  </div>
</template>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
