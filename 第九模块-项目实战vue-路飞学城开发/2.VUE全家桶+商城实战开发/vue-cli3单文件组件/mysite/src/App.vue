<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>{{ title }}</h1>
    <!-- 展示购物车的列表 -->
  <ul>
    <li v-for="(item,index) in cartList" :key="index">
      <h3>{{ item.title}}</h3>
      <p>￥{{ item.price }}</p>
      <button @click="addCart(index)">添加购物车</button>
    </li>
  </ul>
  <my-cart :cart='cartList' :title='title'> </my-cart>
  </div>
</template>

<script>
import MyCart from './components/Cart';
export default {
  name: 'App',
  data(){
    return {
      // cartList:[
      //   {id:1,title:'Vue实战开发',price:188,active:true,count:1},
      //   {id:2,title:'React 实战开发',price:288,active:true,count:1}
      // ]
      cartList:[],
      title:'购物车'
    } 
  },
  async created(){
    // this.$http.get('/api/cartList').then(res=>{
    //     this.cartList = res.data.result;
    // }).catch(err=>{
    //   console.log(err)
    // })
    try {
      const res = await this.$http.get('/api/cartList');
      this.cartList = res.data.result;
    } catch(error){
      console.log(error)
    }
    
  },
  methods:{
    addCart(i){
      const good = this.cartList[i];
      this.$bus.$emit('addCart',good);
    }
  },
  components: {
    MyCart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
