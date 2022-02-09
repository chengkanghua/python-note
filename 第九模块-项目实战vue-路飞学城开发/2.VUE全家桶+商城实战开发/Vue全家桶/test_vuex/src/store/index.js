import Vue from 'vue'
// 1.导入模块
import Vuex from 'vuex'

// 2.使用当前的插件
Vue.use(Vuex)
import cart from './modules/cart'
import products from './modules/products'
import createLogger from 'vuex/dist/logger'

const store = new Vuex.Store({
  plugins: [createLogger()],
  state: { //当前的状态
    count: 0,
    username: '小马哥'
  },
  getters: {
    evenOrOdd(state) {
      return state.count % 2 === 0 ? '偶数' : '奇数';
    }
  },
  mutations: { //声明同步的方法
    increment(state) {
      // 修改状态
      state.count++
    },
    decrement(state) {
      state.count--
    },
    incrementAsync(state,amount) {
      state.count+=amount;
    }

  },
  actions: { //声明异步的方法
    // increment({commit}){
    //   // commit mutations中声明的方法
    // 修改状态的唯一方法是提交mutation
    //   commit('increment')
    // },
    // decrement({commit}) {
    //   commit('decrement')
    // }
    incrementAsync({ commit },{amount}) {
      setTimeout(() => {
        commit('incrementAsync',amount)
      }, 1000);
    }

  },
  modules: {
    cart,
    products
  }
})
export default store;
