<template>
    <div style="padding: 20px;">
        <el-row type="flex" justify="end">
            <el-button type="success" size="small"><i class="el-icon-setting"></i> 保存</el-button>
        </el-row>
        <el-tabs tab-position="left" v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="活动设置" name="tab1">活动设置</el-tab-pane>
            <el-tab-pane label="参与公众号" name="tab2">参与公众号</el-tab-pane>
            <el-tab-pane label="奖励设置" name="tab3">奖励设置</el-tab-pane>
            <el-tab-pane label="海报设置" name="tab4">海报设置</el-tab-pane>
            <el-tab-pane label="进度消息" name="tab5">进度消息</el-tab-pane>
            <el-tab-pane label="其他消息" name="tab6">其他消息</el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
    export default {
        name: "ActivityCreate",
        data() {
            return {
                activeName: "tab2"
            }
        },
        created() {
            const loading = this.$loading({
                lock: true,
                text: '努力加载中',
                spinner: 'el-icon-loading'
            });

            setTimeout(() => {
                loading.close();
            }, 2000);
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            }
        }
    }
</script>

<style scoped>

</style>
