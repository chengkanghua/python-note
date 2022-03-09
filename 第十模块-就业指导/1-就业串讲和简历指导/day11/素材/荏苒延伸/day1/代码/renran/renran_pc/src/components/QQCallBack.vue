<template>
    <div class="sign">
    <div class="logo"><a href="/"><img src="/static/image/nav-logo.png" alt="Logo"></a></div>
    <div class="main">


      <h4 class="title">
        <div class="normal-title">
            <a :class="status==1?'active':''" @click="status=1">已有账号</a>
            <b>·</b>
            <a :class="status==2?'active':''" @click="status=2">没有账号</a>
        </div>
      </h4>
      <div class="js-sign-in-container" v-if="status==1">
        <form action="" method="post">
            <div class="input-prepend restyle js-normal">
              <input placeholder="登录账号或手机号或邮箱" type="text" v-model="username">
              <i class="iconfont ic-user"></i>
            </div>
            <div class="input-prepend">
              <input placeholder="密码" type="password" v-model="password">
              <i class="iconfont ic-password"></i>
            </div>
            <div class="forget-btn">
              <router-link to="/find_password">通过邮箱找回密码?</router-link>
            </div>
            <button class="sign-in-button" type="button" @click.prevent="show_captcha">
              <span></span>登录
            </button>
        </form>
      </div>
      <div class="js-sign-in-container" v-if="status==2">
        <form class="new_user" id="new_user" action="" accept-charset="UTF-8" method="post">
          <div class="input-prepend restyle">
              <input placeholder="你的昵称" type="text" value="" v-model="qq_nickname" id="user_nickname">
            <i class="iconfont ic-user"></i>
          </div>
            <div class="input-prepend restyle no-radius js-normal">
                <input placeholder="手机号" type="tel" v-model="mobile" id="user_mobile_number">
              <i class="iconfont ic-phonenumber"></i>
            </div>
          <div class="input-prepend restyle no-radius security-up-code js-security-number" v-if="is_show_sms_code">
              <input type="text" v-model="sms_code" id="sms_code" placeholder="手机验证码">
            <i class="iconfont ic-verify"></i>
            <a tabindex="-1" class="btn-up-resend js-send-code-button"  href="javascript:void(0);" id="send_code" @click.prevent="send_sms">{{sms_code_text}}</a>
          </div>
          <input type="hidden" name="security_number" id="security_number">
          <div class="input-prepend">
            <input placeholder="设置密码" type="password" v-model="password" id="user_password">
            <i class="iconfont ic-password"></i>
          </div>
          <input type="submit" name="commit" value="注册" class="sign-up-button" id="sign_up_btn" @click.prevent="show_captcha">
          <p class="sign-up-msg">点击 “注册” 即表示您同意并愿意遵守荏苒<br> <a target="_blank" href="">用户协议</a> 和 <a target="_blank" href="">隐私政策</a> 。</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "QQCallBack",
        data(){
          return {
            status: 1, // 当前用户是否拥有了平台账号
            username: "",
            password: "",
            mobile:"",
            sms_code:"",
            sms_code_text:"发送验证码",
            is_show_sms_code:false,
            openid:"",
            qq_avatar: "",
            qq_nickname: "",
          }
        },
        created() {
          this.get_qq_user_info();
        },
        watch: {
          mobile() {
            if (/^1[3-9]\d{9}$/.test(this.mobile)) {
              this.is_show_sms_code = true;
            } else {
              this.is_show_sms_code = false;
            }
          }
        },
        methods:{
          get_qq_user_info(){
            // 获取QQ登录用户的信息
            this.$axios.get(`${this.$settings.Host}/oauth/qq/info/`,{
              params:{
                code: this.$route.query.code
              }
            }).then(response=>{
              let data = response.data;
              if(data.status){
                let info = data.user_info;
                // 登录成功
                localStorage.removeItem("user_token");
                localStorage.removeItem("user_id");
                localStorage.removeItem("user_name");
                localStorage.removeItem("user_avatar");
                localStorage.removeItem("user_nickname");
                sessionStorage.user_token = info.token;
                sessionStorage.user_id = info.id;
                sessionStorage.user_name = info.username;
                sessionStorage.user_avatar = info.avatar;
                sessionStorage.user_nickname = info.nickname;

                this.$confirm('登录成功, 欢迎回来！', '提示', {
                  confirmButtonText: '返回首页',
                  cancelButtonText: '返回上一页',
                  type: 'success'
                }).then(() => {
                  this.$router.push("/");
                }).catch(() => {
                  this.$router.go(-1);
                });

              }else{
                this.status = 2;
                this.openid = data.data;
                this.qq_avatar = data.avatar;
                this.qq_nickname = data.nickname;
              }

            }).catch(error=>{
              this.$message.error("QQ登录异常！");
            })
          },
          send_sms(){
                if( !/1[1-9]{2}\d{8}/.test(this.mobile) ){
                  return false;
                }

                // 如果 sms_code_text 不是文本,而是数字,则表示当前手机号码还在60秒的发送短信间隔内
                if(this.sms_code_text != "发送验证码"){
                  return false;
                }

                // 发送短信
                let _this = this;
                this.$axios.get(`${_this.$settings.Host}/users/sms/${_this.mobile}/`).then(response=>{
                  // 显示发送短信以后的文本倒计时
                  let time = 60;
                  let timer = setInterval(()=>{
                    --time;
                    if(time <=1){
                      // 如果倒计时为0,则关闭当前定时器
                      _this.sms_code_text = "发送验证码";
                      clearInterval(timer);
                      time = 60;
                    }else{
                        _this.sms_code_text = time+"秒";
                    }
                  },1000);

                }).catch(error=>{
                  console.log(error);
                })
            },
          show_captcha(){

              // 验证数据！
              if(this.status == 1){ // 用户选择了已有账号
                if(this.username.length<1 || this.password.length<1){
                  this.$message.error("账号或密码必须填写");
                  return false; // 阻止代码继续往下执行
                }
              }else{ // 用户选择了没有账号
                if( !/1[1-9]{2}\d{8}/.test(this.mobile) ){
                  this.$message.error("手机号码格式有误！");
                  return false;
                }

                if(this.sms_code.length<1 || this.qq_nickname.length<1){
                  this.$message.error("昵称或者验证码必须填写！");
                  return false;
                }

              }

              // 验证码
              let self = this;
              // 生成一个验证码对象
              var captcha1 = new TencentCaptcha(this.$settings.TC_captcha.app_id, function(res) {
                if (res.ret === 0) {
                  // api服务端校验验证码的结果
                  self.$axios.get(`${self.$settings.Host}/users/captcha/`,{
                    params:{
                      ticket: res.ticket,
                      randstr: res.randstr,
                    }
                  }).then(response=>{
                    // 进行登录处理
                    self.bind_account();
                  }).catch(error=>{
                    self.$message.error("验证码校验错误！");
                  })
                }
              });

              // 显示验证码
              captcha1.show();
            },
          bind_account(){
              // 绑定账号
              let data = {
                  "status": this.status, // 值为１,则属于已有平台账号绑定QQ，值为2，则属于新建用户绑定QQ
                  "username":this.username,
                  "password":this.password,
                  "openid": this.openid,
                  "mobile": this.mobile,
                  "sms_code": this.sms_code,
                  "nickname": this.qq_nickname,
                  "avatar": this.qq_avatar,
              };

              this.$axios.post(this.$settings.Host+"/oauth/qq/login/",data).then(response=>{
                    // 使用浏览器本地存储保存token
                    if (this.remember_me) {
                      // 记住登录
                      sessionStorage.removeItem("user_token");
                      sessionStorage.removeItem("user_id");
                      sessionStorage.removeItem("user_name");
                      sessionStorage.removeItem("user_avatar");
                      sessionStorage.removeItem("user_nickname");
                      localStorage.user_token = response.data.token;
                      localStorage.user_id = response.data.id;
                      localStorage.user_name = response.data.username;
                      localStorage.user_avatar = response.data.avatar;
                      localStorage.user_nickname = response.data.nickname;
                    } else {
                      // 未记住登录
                      localStorage.removeItem("user_token");
                      localStorage.removeItem("user_id");
                      localStorage.removeItem("user_name");
                      localStorage.removeItem("user_avatar");
                      localStorage.removeItem("user_nickname");
                      sessionStorage.user_token = response.data.token;
                      sessionStorage.user_id = response.data.id;
                      sessionStorage.user_name = response.data.username;
                      sessionStorage.user_avatar = response.data.avatar;
                      sessionStorage.user_nickname = response.data.nickname;
                    }

                    this.$confirm('登录成功, 欢迎回来！', '提示', {
                      confirmButtonText: '返回首页',
                      cancelButtonText: '返回上一页',
                      type: 'success'
                    }).then(() => {
                      this.$router.push("/");
                    }).catch(() => {
                      this.$router.go(-1);
                    });

                }).catch(error=>{
                    this.$message.error("登录失败！账号或密码错误！");
                    this.username = "";
                    this.password = "";
                })
            },
        }
    }
</script>

<style scoped>
input{
  outline: none;
}
*, :after, :before {
    box-sizing: border-box;
}
.sign {
	height: 100%;
	min-height: 750px;
	text-align: center;
	font-size: 14px;
	background-color: #f1f1f1
}

.sign:before {
	content: "";
	display: inline-block;
	height: 85%;
	vertical-align: middle
}

.sign .disable,.sign .disable-gray {
	opacity: .5;
	pointer-events: none
}

.sign .disable-gray {
	background-color: #969696
}

.sign .tooltip-error {
	font-size: 14px;
	line-height: 25px;
	white-space: nowrap;
	background: none
}

.sign .tooltip-error .tooltip-inner {
	max-width: 280px;
	color: #333;
	border: 1px solid #ea6f5a;
	background-color: #fff
}

.sign .tooltip-error .tooltip-inner i {
	position: static;
	margin-right: 5px;
	font-size: 20px;
	color: #ea6f5a;
	vertical-align: middle
}

.sign .tooltip-error .tooltip-inner span {
	vertical-align: middle;
	display: inline-block;
	white-space: normal;
	max-width: 230px
}

.sign .tooltip-error.right .tooltip-arrow-border {
	border-right-color: #ea6f5a
}

.sign .tooltip-error.right .tooltip-arrow-bg {
	left: 2px;
	border-right-color: #fff
}

.sign .slide-error {
	position: relative;
	padding: 10px 0;
	border: 1px solid #c8c8c8;
	border-radius: 4px
}

.sign .slide-error i {
	position: static!important;
	margin-right: 10px;
	color: #ea6f5a!important;
	vertical-align: middle
}

.sign .slide-error span {
	font-size: 15px;
	vertical-align: middle
}

.sign .slide-error div {
	margin-top: 10px;
	font-size: 13px
}

.sign .slide-error a {
	color: #3194d0
}

.sign .js-sign-up-forbidden {
	color: #999;
	padding: 80px 0 100px
}

.sign .js-sign-up-container .slide-error {
	border-bottom: none;
	border-radius: 0
}

.sign .logo {
	position: absolute;
	top: 56px;
	margin-left: 50px
}

.sign .logo img {
	width: 100px
}

.sign .main {
	width: 400px;
	margin: 60px auto 0;
	padding: 50px 50px 30px;
	background-color: #fff;
	border-radius: 4px;
	box-shadow: 0 0 8px rgba(0,0,0,.1);
	vertical-align: middle;
	display: inline-block
}

.sign .reset-title,.sign .title {
	margin: 0 auto 50px;
	padding: 10px;
	font-weight: 400;
	color: #969696
}

.sign .reset-title a,.sign .title a {
	padding: 10px;
	color: #969696
}

.sign .reset-title a:hover,.sign .title a:hover {
	border-bottom: 2px solid #ea6f5a
}

.sign .reset-title .active,.sign .title .active {
	font-weight: 700;
	color: #ea6f5a;
	border-bottom: 2px solid #ea6f5a
}

.sign .reset-title b,.sign .title b {
	padding: 10px
}

.sign .reset-title {
	color: #333;
	font-weight: 700
}

.sign form {
	margin-bottom: 30px
}

.sign form .input-prepend {
	position: relative;
	width: 100%
}

.sign form .input-prepend input {
	width: 100%;
	height: 50px;
	margin-bottom: 0;
	padding: 4px 12px 4px 35px;
	border: 1px solid #c8c8c8;
	border-radius: 0 0 4px 4px;
	background-color: hsla(0,0%,71%,.1);
	vertical-align: middle
}

.sign form .input-prepend i {
	position: absolute;
	top: 14px;
	left: 10px;
	font-size: 18px;
	color: #969696
}

.sign form .input-prepend span {
	color: #333
}

.sign form .input-prepend .ic-show {
	top: 18px;
	left: auto;
	right: 8px;
	font-size: 12px
}

.sign form .geetest-placeholder {
	height: 44px;
	border-radius: 4px;
	background-color: hsla(0,0%,71%,.1);
	text-align: center;
	line-height: 44px;
	font-size: 14px;
	color: #999
}

.sign form .restyle {
	margin-bottom: 0
}

.sign form .restyle input {
	border-bottom: none;
	border-radius: 4px 4px 0 0
}

.sign form .no-radius input {
	border-radius: 0
}

.sign form .slide-security-placeholder {
	height: 32px;
	background-color: hsla(0,0%,71%,.1);
	border-radius: 4px
}

.sign form .slide-security-placeholder p {
	padding-top: 7px;
	color: #999;
	margin-right: -7px
}

.sign .overseas-btn {
	font-size: 14px;
	color: #999
}

.sign .overseas-btn:hover {
	color: #2f2f2f
}

.sign .remember-btn {
	float: left;
	margin: 15px 0
}

.sign .remember-btn span {
	margin-left: 5px;
	font-size: 15px;
	color: #969696;
	vertical-align: middle
}

.sign .forget-btn {
	float: right;
	position: relative;
	margin: 15px 0;
	font-size: 14px
}

.sign .forget-btn a {
	color: #999
}

.sign .forget-btn a:hover {
	color: #333
}

.sign .forget-btn .dropdown-menu {
	top: 20px;
	left: auto;
	right: 0;
	border-radius: 4px
}

.sign .forget-btn .dropdown-menu a {
	padding: 10px 20px;
	color: #333
}

.sign #sign-in-loading {
	position: relative;
	width: 20px;
	height: 20px;
	vertical-align: middle;
	margin-top: -4px;
	margin-right: 2px;
	display: none
}

.sign #sign-in-loading:after {
	content: "";
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	background-color: transparent
}

.sign #sign-in-loading:before {
	content: "";
	position: absolute;
	top: 50%;
	left: 50%;
	width: 20px;
	height: 20px;
	margin: -10px 0 0 -10px;
	border-radius: 10px;
	border: 2px solid #fff;
	border-bottom-color: transparent;
	vertical-align: middle;
	-webkit-animation: rolling .8s infinite linear;
	animation: rolling .8s infinite linear;
	z-index: 1
}

.sign .sign-in-button,.sign .sign-up-button {
	margin-top: 20px;
	width: 100%;
	padding: 9px 18px;
	font-size: 18px;
	border: none;
	border-radius: 25px;
	color: #fff;
	background: #42c02e;
	cursor: pointer;
	outline: none;
	display: block;
	clear: both
}

.sign .sign-in-button:hover,.sign .sign-up-button:hover {
	background: #3db922
}

.sign .sign-in-button {
	background: #3194d0
}

.sign .sign-in-button:hover {
	background: #187cb7
}

.sign .btn-in-resend,.sign .btn-up-resend {
	position: absolute;
	top: 7px;
	right: 7px;
	width: 100px;
	height: 36px;
	font-size: 13px;
	color: #fff;
	background-color: #42c02e;
	border-radius: 20px;
	line-height: 36px
}

.sign .btn-in-resend {
	background-color: #3194d0
}

.sign .sign-up-msg {
	margin: 10px 0;
	padding: 0;
	text-align: center;
	font-size: 12px;
	line-height: 20px;
	color: #969696
}

.sign .sign-up-msg a,.sign .sign-up-msg a:hover {
	color: #3194d0
}

.sign .overseas input {
	padding-left: 110px!important
}

.sign .overseas .overseas-number {
	position: absolute;
	top: 0;
	left: 0;
	width: 100px;
	height: 50px;
	font-size: 18px;
	color: #969696;
	border-right: 1px solid #c8c8c8
}

.sign .overseas .overseas-number span {
	margin-top: 17px;
	padding-left: 35px;
	text-align: left;
	font-size: 14px;
	display: block
}

.sign .overseas .dropdown-menu {
	width: 100%;
	max-height: 285px;
	font-size: 14px;
	border-radius: 0 0 4px 4px;
	overflow-y: auto
}

.sign .overseas .dropdown-menu li .nation-code {
	width: 65px;
	display: inline-block
}

.sign .overseas .dropdown-menu li a {
	padding: 6px 20px;
	font-size: 14px;
	line-height: 20px
}

.sign .overseas .dropdown-menu li a::hover {
	color: #fff;
	background-color: #f5f5f5
}

.sign .more-sign {
	margin-top: 50px
}

.sign .more-sign h6 {
	position: relative;
	margin: 0 0 10px;
	font-size: 12px;
	color: #b5b5b5
}

.sign .more-sign h6:before {
	left: 30px
}

.sign .more-sign h6:after,.sign .more-sign h6:before {
	content: "";
	border-top: 1px solid #b5b5b5;
	display: block;
	position: absolute;
	width: 60px;
	top: 5px
}

.sign .more-sign h6:after {
	right: 30px
}

.sign .more-sign ul {
	margin-bottom: 10px;
	list-style: none
}

.sign .more-sign ul li {
	margin: 0 5px;
	display: inline-block
}

.sign .more-sign ul a {
	width: 50px;
	height: 50px;
	line-height: 50px;
	display: block
}

.sign .more-sign ul i {
	font-size: 28px
}

.sign .more-sign .ic-weibo {
	color: #e05244
}

.sign .more-sign .ic-wechat {
	color: #00bb29
}

.sign .more-sign .ic-qq_connect {
	color: #498ad5
}

.sign .more-sign .ic-douban {
	color: #00820f
}

.sign .more-sign .ic-more {
	color: #999
}

.sign .more-sign .weibo-loading {
	pointer-events: none;
	cursor: pointer;
	position: relative
}

.sign .more-sign .weibo-loading:after {
	content: "";
	position: absolute;
	left: 0;
	top: 0;
	width: 100%;
	height: 100%;
	background-color: #fff
}

body.reader-night-mode .sign .more-sign .weibo-loading:after {
	background-color: #3f3f3f
}

.sign .more-sign .weibo-loading:before {
	content: "";
	position: absolute;
	top: 50%;
	left: 50%;
	width: 20px;
	height: 20px;
	margin: -10px 0 0 -10px;
	border-radius: 10px;
	border: 2px solid #e05244;
	border-bottom-color: transparent;
	vertical-align: middle;
	-webkit-animation: rolling .8s infinite linear;
	animation: rolling .8s infinite linear;
	z-index: 1
}

@keyframes rolling {
	0% {
		-webkit-transform: rotate(0deg);
		transform: rotate(0deg)
	}

	to {
		-webkit-transform: rotate(1turn);
		transform: rotate(1turn)
	}
}

@-webkit-keyframes rolling {
	0% {
		-webkit-transform: rotate(0deg)
	}

	to {
		-webkit-transform: rotate(1turn)
	}
}

.sign .reset-password-input {
	border-radius: 4px!important
}

.sign .return {
	margin-left: -8px;
	color: #969696
}

.sign .return:hover {
	color: #333
}

.sign .return i {
	margin-right: 5px
}

.sign .icheckbox_square-green {
	display: inline-block;
	*display: inline;
	vertical-align: middle;
	margin: 0;
	padding: 0;
	width: 18px;
	height: 18px;
	background: url(/static/image/green.png) no-repeat;
	border: none;
	cursor: pointer;
	background-position: 0 0
}

.sign .icheckbox_square-green.hover {
	background-position: -20px 0
}

.sign .icheckbox_square-green.checked {
	background-position: -40px 0
}

.sign .icheckbox_square-green.disabled {
	background-position: -60px 0;
	cursor: default
}

.sign .icheckbox_square-green.checked.disabled {
	background-position: -80px 0
}


.geetest_panel_box>* {
	box-sizing: content-box
}

@media (max-width:768px) {
	body {
		min-width: 0
	}

	.sign {
		height: auto;
		min-height: 0;
		background-color: transparent
	}

	.sign .logo {
		display: none
	}

	.sign .main {
		position: absolute;
		left: 50%;
		margin: 0 0 0 -200px;
		box-shadow: none
	}
}
</style>
