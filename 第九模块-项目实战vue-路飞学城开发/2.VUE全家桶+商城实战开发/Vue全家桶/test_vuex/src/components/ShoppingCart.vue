<template>
  <div>
    <h2>我的购物车</h2>
    <ul>
      <li
        v-for="(item,index) in getCartList"
        :key="index"
      >{{item.title}} - {{item.price | currency}} x {{item.quantity}}</li>
    </ul>
    总价格:{{cartTotalPrice | currency}}
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "ShoppingCart", //组件名  注册全局组件时使用,
  computed: {
    ...mapGetters("cart", ["getCartList", "cartTotalPrice"])
  }
};
</script>

<style lang="scss" scoped>
</style>