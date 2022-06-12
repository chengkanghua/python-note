<template>
    <div>
        <!--顶部菜单-->
        <div>
            <el-menu class="el-menu-demo" mode="horizontal" background-color="#545c64"
                     :default-active="rootActiveRouter"
                     text-color="#fff" active-text-color="#ffd04b" router>
                <el-menu-item>媒体宝系统</el-menu-item>
                <el-menu-item index="Task" :route="{name:'ActivityList'}">任务宝</el-menu-item>
                <el-menu-item index="Msg" :route="{name:'Push'}">消息宝</el-menu-item>
                <el-menu-item index="Auth" :route="{name:'Auth'}">授权</el-menu-item>

                <el-submenu index="5" style="float: right">
                    <template slot="title">{{username}}</template>
                    <el-menu-item index="5-1">个人中心</el-menu-item>
                    <el-menu-item index="5-2">注销</el-menu-item>
                </el-submenu>
            </el-menu>
        </div>
        <div>
            <router-view></router-view>
        </div>


    </div>
</template>

<script>
    export default {
        name: "Layout",
        data() {
            return {
                rootActiveRouter: ""
            }
        },
        mounted() {
            // 获取当前的所有路由
            this.rootActiveRouter = this.$route.matched[1].name;
        },
        computed: {
            username() {
                return this.$store.state.username;
            }
        }
    }
</script>

<style scoped>

</style>
