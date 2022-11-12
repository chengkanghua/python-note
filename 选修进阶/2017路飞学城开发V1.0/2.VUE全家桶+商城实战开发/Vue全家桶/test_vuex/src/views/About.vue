<template>
  <div class="about">
    <h1>This is an about page</h1>
    {{myCount}} - {{user}}
    {{evenOrOdd}}
    <button @click="increment">+1</button>
    <button @click="decrement">-1</button>
    <button @click="incrementAsync">+1异步</button>
    <ProductList></ProductList>
    <hr>
    <!-- <ShoppingCart></ShoppingCart> -->
    <shopping-cart></shopping-cart>

  </div>
</template>
<script>
import { mapState, mapGetters, mapMutations, mapActions } from "vuex";
import ProductList from '@/components/ProductList'
// import ShoppingCart from '@/components/ShoppingCart'
export default {
  components: {
    ProductList,
    // ShoppingCart
  },
  computed: {
    // count() {
    //   return this.$store.state.count;
    // },
    // username(){
    //   return this.$store.state.username;
    // }
    // ...mapState(['count','username'])
    ...mapState({
      myCount: "count",
      user: "username"
    }),
    // evenOrOdd() {
    //   return this.$store.getters.evenOrOdd;
    // }
    ...mapGetters(['evenOrOdd'])
  },
  methods: {
    incrementAsync() {
      // 在组件内部提交数据 载荷形式分发
      // this.$store.dispatch('incrementAsync',{
      //   amount:10
      // });
      this.$store.dispatch({
        type:'incrementAsync',
        amount: 10
      })
    },
    // ...mapActions(['incrementAsync']),

    /* increment() {
      // dispatch触发actions中声明的方法(异步)
      // this.$store.dispatch('increment');
      this.$store.commit("increment");
    },
    decrement() {
      // this.$store.dispatch('decrement');
      this.$store.commit("decrement");
    } */
    ...mapMutations(['increment','decrement'])
  }
};
</script>

