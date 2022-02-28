
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
// 课程分类列表api
export const categoryList =  ()=> {
	return Axios.get('course/category').then(res=>res.data);
}
// https://www.luffycity.com/api/v1/courses/?sub_category=0
// 全部课程列表
export const  allCategoryList = (categoryId)=>{
	return Axios.get(`course/list?category=${categoryId}`).then(res=>res);
}

// 课程详情
export const coursedetail = (courseid)=>{
	return Axios.get(`course/detail/${courseid}`).then(res=>res);
}

// geetest接口
// export const geetest = ()=>{
// 	return Axios.get(`captcha_check/`).then(res=>res.data);
// }

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

// 加入购物车的接口
export const shopCart = (params)=>{
	return Axios.post('shop/shopping_car',params).then(res=>res.data);
}
// 购物车的数据
export const shopCartList = (user_name)=>{
	return Axios.get(`shop/shopping_car/${user_name}`).then(res=>res.data);
}
// 删除购物车
export const delCartList = (params)=>{
	return Axios.delete('shop/shopping_car',params).then(res=>res.data);
}





