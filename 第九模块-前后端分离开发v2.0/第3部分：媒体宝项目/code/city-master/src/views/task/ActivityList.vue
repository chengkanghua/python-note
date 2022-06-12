<template>
    <div style="padding: 20px">
        <router-link :to="{name:'ActivityCreate'}">
            <el-button type="primary" size="small"><i class="el-icon-circle-plus-outline"></i> 新建活动</el-button>
        </router-link>

        <el-row style="margin-top: 25px;">
            <el-form :inline="true" class="demo-form-inline" size="small" :model="searchForm" ref="searchForm">


                <el-form-item label="活动状态" prop="category">
                    <el-select placeholder="全部状态" v-model="searchForm.category">
                        <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label"
                                   :value="item.value"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>

                <el-form-item label="公众号" prop="category">
                    <el-select placeholder="全部公众号" v-model="searchForm.category">
                        <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label"
                                   :value="item.value"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>

                <el-form-item label="活动名称" prop="title">
                    <el-input placeholder="活动名称" v-model="searchForm.title"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button size="small" type="primary">筛选</el-button>
                    <el-button size="small">重置</el-button>
                </el-form-item>

            </el-form>

        </el-row>

        <el-row :gutter="20">
            <el-col style="width: 240px;margin-bottom: 20px;" v-for="(o, index) in 12" :key="o">
                <el-card :body-style="{ padding: '0px' }">
                    <img style="height: 160px;width: 100%;"
                         src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                         class="image">
                    <div style="padding: 14px;">
                        <span>好吃的汉堡{{index}}</span>
                        <el-row style="margin-top: 8px;">
                            <el-button icon="el-icon-search" size="mini" circle></el-button>
                            <el-button icon="el-icon-edit" size="mini" circle></el-button>
                            <el-button icon="el-icon-check" size="mini" circle></el-button>
                            <el-button icon="el-icon-message" size="mini" circle></el-button>
                        </el-row>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "ActivityList",
        data() {
            return {
                searchForm: {
                    title: "",
                    category: ""
                },
                categoryOptions: [
                    {
                        value: '1',
                        label: '黄金糕'
                    }, {
                        value: '2',
                        label: '双皮奶'
                    }, {
                        value: '3',
                        label: '蚵仔煎'
                    }, {
                        value: '4',
                        label: '龙须面'
                    }, {
                        value: '5',
                        label: '北京烤鸭'
                    }],
                currentDate: new Date()
            }
        },
        created() {
            this.axios.get("/base/test/").then(res => {
                console.log("请求成功", res);
            }).catch(reason => {
                console.log('请求失败', reason);
                return reason;
            })
        }

    }
</script>

<style scoped>

    .image {
        width: 100%;
        display: block;
    }

</style>
