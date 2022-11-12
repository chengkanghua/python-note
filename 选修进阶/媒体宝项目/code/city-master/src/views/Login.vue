<template>
    <div class="main">
        <div class="loginBox">
            <div class="tabBoxSwitch">
                <ul class="tabBoxSwitchUl">
                    <li :class="tabSelected === index?'tab-active' : ''" v-for="(txt,index) in tabList" :key="index"
                        @click="tabSelected=index">{{txt}}
                    </li>
                </ul>
            </div>

            <div v-show="tabSelected===0">
                <el-form :model="userForm" :rules="userRules" ref="userForm">
                    <el-form-item prop="username" style="margin-top: 24px;" :error="userFormError.username">
                        <el-input v-model="userForm.username" placeholder="用户名或手机号"></el-input>
                    </el-form-item>
                    <el-form-item prop="password" :error="userFormError.password">
                        <el-input v-model="userForm.password" placeholder="密码" show-password></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button @click="submitForm('userForm')" type="primary" size="medium">登 录</el-button>
                    </el-form-item>
                </el-form>
            </div>

            <div v-show="tabSelected===1">
                <el-form :model="smsForm" :rules="smsRules" ref="smsForm">
                    <el-form-item prop="phone" style="margin-top: 24px;">
                        <el-input v-model="smsForm.phone" placeholder="手机号"></el-input>
                    </el-form-item>
                    <el-form-item prop="code">
                        <el-row type="flex" justify="space-between">
                            <el-input v-model="smsForm.code" placeholder="验证码"></el-input>
                            <el-button :disabled="btnSmsDisabled" @click="sendSmsCode" style="margin-left: 10px;">
                                {{btnSmsText}}
                            </el-button>
                        </el-row>

                    </el-form-item>
                    <el-form-item>
                        <el-button @click="submitForm('smsForm')" type="primary" size="medium">登 录</el-button>
                    </el-form-item>
                </el-form>
            </div>

        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                tabSelected: 0,
                tabList: ["密码登录", "免密码登录"],
                userForm: {
                    username: "",
                    password: ""
                },
                userFormError: {
                    username: "",
                    password: ""
                },
                userRules: {
                    username: [
                        {required: true, message: '请输入用户名或手机', trigger: 'blur'},
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur'},
                    ],
                },
                smsForm: {
                    phone: "",
                    code: ""
                },
                smsRules: {
                    phone: [
                        {required: true, message: '请输入手机号', trigger: 'blur'},
                        {pattern: /^1[3456789]\d{9}$/, message: '手机号格式错误', trigger: 'blur'},
                    ],
                    code: [
                        {required: true, message: '验证码', trigger: 'blur'},
                    ],
                },

                btnSmsDisabled: false,
                btnSmsText: "发送验证码"
            }
        },
        methods: {
            submitForm(formName) {
                // 清空原来的错误
                this.clearCustomFormError();

                // 执行验证规则
                this.$refs[formName].validate((valid) => {
                    if (!valid) {
                        //console.log("验证未通过");
                        return false;
                    }
                    // console.log("验证通过");
                    // 验证通过，向后端的API发送请求
                    this.axios.post("/base/auth/", this.userForm).then(res => {
                        // res.data = {code:1000, detail:"...."}
                        // res.data = {code:0, detail:"....", data:{ username:"用户名", token:"jwt"}}
                        if (res.data.code === 0) {
                            // 登录成功：写入cookie、写入state
                            this.$store.commit("login", res.data.data);
                            this.$router.push({path: "/"})
                            return
                        }
                        // 1000，字段错误，把相关错误信息现在标签上
                        if (res.data.code === 1000) {
                            // 不好弄，API获取数据，错误显示表单。
                            // detail = { username:['错误',] ,password: [11,22] }
                            this.validateFormFailed(res.data.detail);
                            return;
                        }
                        // 1001，整体错误，整体显示
                        if (res.data.code === 1001) {
                            this.$message.error(res.data.detail);
                        } else {
                            this.$message.error("请求失败");
                        }

                    });
                });
            },
            sendSmsCode() {
                this.$refs.smsForm.validateField("phone", (error) => {
                    if (error) {
                        return false;
                    }
                    // 验证通过拿到手机号，向后台发送请求 -> 发送验证码
                    // 禁用按钮
                    this.btnSmsDisabled = true;
                    // 设置倒计时
                    let txt = 60;
                    let interval = window.setInterval(() => {
                        txt -= 1;
                        this.btnSmsText = `${txt}秒后重发`
                        if (txt < 1) {
                            this.btnSmsText = "重新发送";
                            this.btnSmsDisabled = false;
                            window.clearInterval(interval);
                        }
                    }, 1000);

                })
            },
            validateFormFailed(errorData) {
                for (let fieldName in errorData) {
                    let error = errorData[fieldName][0];
                    this.userFormError[fieldName] = error;
                }
            },
            clearCustomFormError() {
                for (let key in this.userFormError) {
                    this.userFormError[key] = ""
                }

            },
        }
    }
</script>

<style scoped>
    .main {
        width: 100%;
        height: 100vh;
        background-color: #2E3E9C;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .loginBox {
        background-color: #FFFFFF;
        box-shadow: 0 1px 3px rgba(26, 26, 26, 0.1);
        border-radius: 2px;
        width: 380px;
        min-height: 200px;
        padding: 0 24px 20px;
    }


    .tabBoxSwitch .tabBoxSwitchUl {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .tabBoxSwitch .tabBoxSwitchUl li {
        display: inline-block;
        height: 60px;
        font-size: 16px;
        line-height: 60px;
        margin-right: 24px;
        cursor: pointer;
    }

    .tab-active {
        position: relative;
        color: #1a1a1a;
        font-weight: 600;
        font-synthesis: style;
    }


    .tab-active::before {
        display: block;
        position: absolute;
        bottom: 0;
        content: "";
        width: 100%;
        height: 3px;
        background-color: #0084ff;
    }
</style>
