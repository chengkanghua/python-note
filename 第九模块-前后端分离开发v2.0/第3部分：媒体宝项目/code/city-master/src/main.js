import Vue from 'vue'
import App from './App.vue'
import './plugins/cookie'
import router from './router'
import './plugins/axios'
import store from './store'
import './plugins/element.js'

import HighchartsVue from 'highcharts-vue'

Vue.use(HighchartsVue)

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
