import Vue from 'vue'
import VueCookie from 'vue-cookie'

Vue.use(VueCookie)


export const getToken = () => {
    return Vue.cookie.get("token")
}


export const getUserName = () => {
    return Vue.cookie.get("username")
}


export const setUserToken = (username, token) => {
    Vue.cookie.set('username', username, {expires: '7D'});
    Vue.cookie.set('token', token, {expires: '7D'});
}

export const clearUserToken = () => {
    Vue.cookie.delete('username');
    Vue.cookie.delete('token');
}

