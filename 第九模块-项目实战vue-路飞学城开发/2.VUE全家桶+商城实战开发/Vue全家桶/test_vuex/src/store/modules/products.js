import Axios from 'axios'
export default {
    namespaced: true,
    state: {
        products: []
    },
    getters: {

    },
    mutations: {
        getAllProducts(state, products) {
            state.products = products
        },
        decrementProductInventory(state, { id }) {
            const product = state.products.find(item => item.id === id);
            product.inventory--;
        }
    },
    actions: {
        async getAllProducts({ commit }) {
            // 发送请求 获取数据 提交mutation
            try {
                const res = await Axios.get('/api/products');
                const results = res.data.results
                commit('getAllProducts', results);

            } catch (error) {
                console.log(error);

            }
        }

    }
}