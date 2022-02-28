
import Axios  from 'axios'
// 设置公共的url
Axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';

// 添加请求拦截器
Axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    if (localStorage.getItem('access_token')) {
    	// Axios.defaults.headers.common['Authorization'] = localStorage.getItem('access_token');
    	// console.log(config.headers);
    	config.headers.Authorization = localStorage.getItem('access_token')
		
    }
	return config

  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });


// 登录
export const  userLogin = (params)=>{
	// 这个参数至少有五个字段 username password  验证的三个字段
	return Axios.post('login',params).then(res=>res.data);
}
// 注册
export const register = (params)=>{
	return Axios.post('register',params).then(res=>res.data)
}
// 退出
export const logout = (params)=>{
	return Axios.post('logout',params).then(res=>res.data)
}







