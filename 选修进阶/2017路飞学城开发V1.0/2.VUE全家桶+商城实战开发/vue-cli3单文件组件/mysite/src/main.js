import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

// 导入element-ui  
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI)  // 全部倒入

// 按需导入
// import { Button,Table,TableColumn,InputNumber } from 'element-ui' 
// Vue.use(Button)
// Vue.use(Table)
// Vue.use(TableColumn)
// Vue.use(InputNumber)

Vue.config.productionTip = false
Vue.prototype.$http = axios;
Vue.prototype.$bus = new Vue();

new Vue({
  render: h => h(App),
}).$mount('#app')
