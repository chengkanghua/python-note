<template>
  <div id="app">
    <div id="nav">
      <!-- router-link 相当于a标签,to属性相当于a标签的href -->
      <router-link :to="{name:'Home'}">Home</router-link> |
      <router-link :to="{name:'About'}">About</router-link>|
          <!-- 声明式 -->
      <router-link :to="{name:'user',params:{id:1}}">User1</router-link>|
      <router-link :to="{name:'user',params:{id:2}}">User2</router-link>|
      <router-link :to="{name:'page',query:{id:1,title:'foo'}}">Page</router-link>|
        <!-- 路由嵌套 -->
      <router-link to="/user/1/profile">/user/1/Profile</router-link>|
      <router-link to="/user/1/posts">/user/1/Posts</router-link>|
      <router-link :to='{name:"notes"}'>我的笔记</router-link>|
      <router-link :to='{name:"editor"}'>编辑</router-link>|
      <router-link :to="{name:'blog'}">博客</router-link>|
      <router-link :to='{name:"post"}'>Post</router-link>|

    </div>
    <!-- router-view 相当于路由组件的出口 -->
    <router-view> </router-view>
    <!-- Home -->
    <router-view name="main" class="main"></router-view>
    <router-view name="sideBar" class="sideBar"></router-view>

  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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
