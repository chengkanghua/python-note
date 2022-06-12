<template>
    <div class="home">
        <div>
            <el-menu class="el-menu-demo" mode="horizontal" :default-active="rootActiveRouter"
                     background-color="#545c64"
                     text-color="#fff" active-text-color="#ffd04b" router>
                <el-menu-item>媒体宝系统</el-menu-item>

                <el-menu-item index="Task" :route="{name:'Activity'}">任务宝</el-menu-item>

                <el-menu-item index="Msg" :route="{name:'Push'}">消息宝</el-menu-item>

                <el-menu-item index="Auth" :route="{name:'Auth'}">公众号授权</el-menu-item>

                <el-submenu class="right">
                    <template slot="title">{{username}}</template>
                    <el-menu-item index="Info" :route="{name:'Info'}">个人信息</el-menu-item>
                    <el-menu-item index="Login" @click="goTo">注销</el-menu-item>
                </el-submenu>

            </el-menu>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'Home',
        components: {
            // HelloWorld
        }
    }
</script>
