<template>
  <div>
    <div>用户页面 {{$route.params.id}}</div>
    <div>用户页面 {{id}}-{{title}}</div>
    <button @click='goHome'>跳转到首页</button>
    <button @click='goBack'>后退</button>
    <!-- 子路由组件出口 -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  // 路由组件会复用的情况?

  // 当路由参数变化时 /user/1切换到/user/2 原来的组件实例会被复用.
  // 因为两个路由渲染了同个组件 复用高效
  created() {
    // console.log(this.$route.params.id);
    // console.log(this.$router);
  },
  methods: {
    goBack(){
      this.$router.go(-2);
    },
    goHome() {
      // 编程式导航
      // this.$router.push('/');
      // this.$router.push('name');
      this.$router.push({
        path:'/'
      });
      // this.$router.push({
      //  name:'user',
      //  params:{id:2}
      // });
      // this.$router.push({
      //   path:"/register",
      //   query:{plan:'123'}
      // })
    }
  },
  props:['id','title'],
  // 响应路由参数的变化
  // watch:{
  //     $route:(to,from)=>{
  //         console.log(to.params.id);
  //         // 发起ajax 请求后端接口数据 数据驱动视图

  //     }
  // }
  beforeRouteUpdate(to, from, next) {
    console.log(to.params.id);
    // 一定要调用next,不然会阻塞整个路由  放行
    next();
  }
};
</script>

<style lang="scss" scoped>
</style>