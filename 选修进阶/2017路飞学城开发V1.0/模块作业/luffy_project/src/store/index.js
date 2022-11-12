import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

let store = new Vuex.Store({
	// 三大将
	state:{
		userInfo:{}
	},
	// 修改state的唯一方法 是提交mutations
	mutations:{
		setUserInfo(state,user){
			state.userInfo = user;
			// console.log(state.userInfo);
		},
		delUserInfo(state,){
			state.userInfo = {};	
		}
	},
	actions:{
		getUserInfo({commit},user){
			commit('setUserInfo',user);
		},
		delUserInfo({commit},){
			commit('delUserInfo',)

		}
	}
});
export default store;