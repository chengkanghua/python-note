<template>
    <div>
        <el-menu class="sub-menu" mode="horizontal" :default-active="subActiveRouter" router>
            <el-menu-item index="Push" :route="{name:'Push'}"><i class="el-icon-coin"></i>消息推送</el-menu-item>
            <el-menu-item index="Sop" :route="{name:'Sop'}"><i class="el-icon-data-analysis"></i>SOP计划</el-menu-item>
        </el-menu>

        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        name: "MsgLayout",
        data() {
            return {
                subActiveRouter: ""
            }
        },
        mounted() {
            // 获取当前的所有路由
            this.subActiveRouter = this.$route.matched[2].name;
        }
    }
</script>

<style scoped>
    .sub-menu .el-menu-item {
        line-height: 40px;
        height: 40px;
        vertical-align: middle;
        font-size: 13px;
    }

    .sub-menu .el-menu-item i {
        margin-top: -3px;
    }
</style>
