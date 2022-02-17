<template>
    <div>
        <h2>登陆页面</h2>
        <input type="text" v-model="user">
        <input type="password" v-model="pwd">
        <button @click="handleLogin">登陆</button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                user:'',
                pwd:''
            }
        },
        methods:{
            handleLogin(){
                // 1获取用户名和密码  2与后端发生交互
                setTimeout(()=>{
                    let data = {
                        user:this.user
                    }
                    // 保存用户名到本地
                    localStorage.setItem('user',JSON.stringify(data));
                    // 跳转到我的笔记页面
                    this.$router.push({
                        // 跳转回之前需要登陆的页面
                        path: this.$route.query.redirect
                        // name: 'notes'
                    })
                },1000);
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>