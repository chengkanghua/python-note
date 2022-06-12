import Vue from 'vue'
import Vuex from 'vuex'
import {getUserName, getToken, setUserToken,clearUserToken} from "@/plugins/cookie"

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        username: getUserName(),
        token: getToken(),
    },
    mutations: {
        login: function (state, {username, token}) {
            state.username = username;
            state.token = token;
            // Vue.cookie.set("username",username);
            // Vue.cookie.set("token",token);
            setUserToken(username, token);
        },
        logout:function (state) {
            state.username = ""
            state.token = ""
            clearUserToken()
        }
    },
    actions: {},
    modules: {}
})
