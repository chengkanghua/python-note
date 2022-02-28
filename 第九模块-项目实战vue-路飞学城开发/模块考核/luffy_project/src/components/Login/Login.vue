<template>
        <div>
            <input v-model = 'username' type="text"  placeholder="用户名 / 手机号码" class="user">
            <input v-model = 'password' type="password" name="" class="pwd" placeholder="密码">
    
            <button class="login_btn" @click = 'loginHandler'>登录</button>

        </div>

</template>

<script>
export default {
  name: 'Login',
  data(){
    return {
        username:"",
        password:"",
    }
  },

  methods:{
    loginHandler(){
        let params = {
            username:this.username,
            password:this.password,
        }
        console.log(params)
        this.$http.userLogin(params)
        .then(res=>{
            console.log(res);
            if (res.error === null) {
                this.$router.push({
                    name:"Index"
                });
                localStorage.setItem('access_token', res.access_token);
                localStorage.setItem('username', res.username);
                this.$message(res.data)
                // localStorage.removeItem
                // localStorage.setItem('avatar',res.data.avatar);
                // localStorage.setItem('shop_cart_num',res.data.shop_cart_num);


                // dispacth action的行为
                // this.$store.dispatch('getUserInfo',res)
                

            }else{this.$message(res.error)}
            
        })
        .catch(err=>{
            console.log(err);
            
        })
    },
   
  },

};
</script>

<style lang="css" scoped>

</style>
