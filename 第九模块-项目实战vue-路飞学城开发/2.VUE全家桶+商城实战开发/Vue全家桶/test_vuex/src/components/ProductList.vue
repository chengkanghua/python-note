<template>
  <div>
    <h2>我的商铺</h2>
    <ul>
      <li
        v-for="(product) in products"
        :key="product.id"
      >{{product.title}} - {{product.price | currency}} - {{product.inventory}}
       <br>
      <button :disabled='!product.inventory' @click='addProductToCart(product)'>加入购物车</button>
      </li>
     
    </ul>
  </div>
</template>

<script>
import { mapState,mapActions } from "vuex";
export default {
  computed: {
    ...mapState("products", ["products"])
  },
  created() {
    this.$store.dispatch("products/getAllProducts");
  },
  methods: {
    ...mapActions('cart',['addProductToCart'])
  },
  
};
</script>

<style lang="scss" scoped>
</style>