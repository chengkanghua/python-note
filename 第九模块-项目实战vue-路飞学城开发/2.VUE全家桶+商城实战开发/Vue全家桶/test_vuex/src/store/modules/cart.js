export default {
    namespaced: true,
    state: {
        cartList: [],
        count: 0
    },
    getters: {
        getCount(state) {
            return state.count
        },
        // 获取购物车的数据
        getCartList(state, getters, rootState) {
            return state.cartList.map(({ id, quantity }) => {
                const product = rootState.products.products.find(item => item.id === id);
                return {
                    title: product.title,
                    price: product.price,
                    quantity
                }
            })
        },
        cartTotalPrice(state, getters) {
            return getters.getCartList.reduce((total, product) => {
                return total + product.price * product.quantity
            }, 0);
        }


    },
    mutations: {
        // 第一此添加该商品到购物车
        pushProductToCart(state, { id, quantity }) {
            state.cartList.push({
                id,
                quantity
            })
        },
        // 购物车中已有数据 只改变当前的数量
        incrementCartItemQuantity(state, { id }) {
            const product = state.cartList.find(item => item.id === id);
            product.quantity++;
        }
    },
    actions: {
        addProductToCart({ commit, state }, product) {
            if (product.inventory > 0) { //   有库存
                const cartItem = state.cartList.find(item => item.id === product.id);
                console.log(cartItem);

                if (!cartItem) {
                    //   购物车无数据 新添加到购物车
                    commit('pushProductToCart', { id: product.id, quantity: 1 })
                } else {
                    //购物车中已有数据
                    commit('incrementCartItemQuantity', { id: product.id });
                }
                // 如果想提交另一个模块中的方法，那么需要第三个参数{root:true}
                commit('products/decrementProductInventory', { id: product.id },{root:true})
            }

        }
    }
}