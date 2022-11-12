<template>

</template>

<script>
    export default {
        name: "Wallet",
        data(){
          return {
            token:"",
          }
        },
        created() {
          this.token = this.get_login_user();
          this.get_pay_result()
        },
        methods:{
           get_login_user(){
            // 获取登录用户
            return localStorage.user_token || sessionStorage.user_token;
          },
          get_pay_result(){
            // 判断是否是从支付页面返回
            if(!this.token){
              this.$router.push("/login");
              return false;
            }
            if(this.$route.query.out_trade_no){
              // 转发支付结果到服务端
              this.$axios.get(`${this.$settings.Host}/payments/alipay/result/`+location.search).then(response=>{

              }).catch(error=>{
                this.$message.error("支付结果处理有误！请及时联系客服工作人员！");
              });
            }
          }
        }
    }
</script>

<style scoped>

</style>
