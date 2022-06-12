<template>
    <div style="padding: 20px;">
        <el-card class="box-card">
            <el-form :inline="true" class="demo-form-inline" size="small" :model="searchForm" ref="searchForm">
                <el-form-item label="标题" prop="title">
                    <el-input placeholder="标题" v-model="searchForm.title"></el-input>
                </el-form-item>

                <el-form-item label="类型" prop="category">
                    <el-select placeholder="类型" v-model="searchForm.category">
                        <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label"
                                   :value="item.value"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>

                <el-form-item>
                    <el-button size="small" type="primary" @click="clickSearch">筛选</el-button>
                    <el-button size="small" @click="resetSearchForm('searchForm')">重置</el-button>
                </el-form-item>

            </el-form>

        </el-card>

        <el-card class="box-card" style="margin-top: 25px;">
            <div slot="header" class="clearfix">
                <span><i class="el-icon-s-grid"></i> 消息列表</span>
                <el-button style="float: right;" type="primary" size="small" @click="clickAddDrawer">
                    <i class="el-icon-circle-plus-outline"></i> 新建推广码
                </el-button>
            </div>
            <div>
                <el-table :data="tableData" border style="width: 100%">
                    <el-table-column prop="date" label="日期"></el-table-column>
                    <el-table-column prop="name" label="姓名"></el-table-column>
                    <el-table-column prop="address" label="地址"></el-table-column>
                    <el-table-column label="二维码">

                        <template slot-scope="scope">
                            <el-popover
                                    placement="right"
                                    trigger="hover">
                                <div>
                                    <el-image
                                            style="width: 140px; height: 140px"
                                            :src="scope.row.url"
                                            fit="fit"></el-image>
                                </div>
                                <el-image slot="reference" style="width: 40px; height: 40px" :src="scope.row.url"
                                          fit="fit"></el-image>
                            </el-popover>

                        </template>

                    </el-table-column>
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>

                            <el-button @click="handleEditClick(scope.row)" type="text" size="small">编辑</el-button>


                            <el-popconfirm style="display: inline-block;margin-left: 10px;" title="这是一段内容确定删除吗？" @confirm="confirmDelete(scope.row)">
                                <el-button slot="reference" type="text" size="small">删除</el-button>
                            </el-popconfirm>

                        </template>
                    </el-table-column>
                </el-table>
            </div>
            <el-row type="flex" justify="end" style="margin-top: 30px;">
                <el-pagination
                        :total="page.totalCount"
                        :page-size="page.perPageSize"
                        background
                        layout="prev, pager, next,jumper"
                        @current-change="handleCurrentChange"
                >
                </el-pagination>
            </el-row>
        </el-card>


        <el-dialog title="提示" :visible.sync="dialogVisible" width="30%">
            <span>这是一段信息</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
              </span>
        </el-dialog>


        <el-drawer title="我是标题" :visible.sync="drawerVisible" :before-close="handleDrawerClose" direction="ltr">
            <div style="padding: 25px;">
                <el-form label-position="left" label-width="80px" :model="addForm" size="small">
                    <el-form-item label="活动名称" prop="x1">
                        <el-input autocomplete="off" v-model="addForm.x1"></el-input>
                    </el-form-item>
                    <el-form-item label="活动区域" prop="x2">
                        <el-select placeholder="请选择活动区域" v-model="addForm.x2">
                            <el-option label="区域一" value="shanghai"></el-option>
                            <el-option label="区域二" value="beijing"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item>
                        <el-button @click="dialogFormVisible = false">取 消</el-button>
                        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-drawer>

    </div>
</template>

<script>
    export default {
        name: "Promo",
        data() {
            return {
                drawerVisible: false,
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
                tableData: [
                    {
                        date: '2016-05-02',
                        name: '王小虎',
                        province: '上海',
                        city: '普陀区',
                        address: '上海市普陀区金沙江路 1518 弄',
                        zip: 200333,
                        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        status: 1
                    }, {
                        date: '2016-05-04',
                        name: '王小虎',
                        province: '上海',
                        city: '普陀区',
                        address: '上海市普陀区金沙江路 1517 弄',
                        zip: 200333,
                        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        status: 2
                    }, {
                        date: '2016-05-01',
                        name: '王小虎',
                        province: '上海',
                        city: '普陀区',
                        address: '上海市普陀区金沙江路 1519 弄',
                        zip: 200333,
                        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        status: 1
                    }, {
                        date: '2016-05-03',
                        name: '王小虎',
                        province: '上海',
                        city: '普陀区',
                        address: '上海市普陀区金沙江路 1516 弄',
                        zip: 200333,
                        url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                        status: 1
                    }],
                page: {
                    totalCount: 10000,
                    perPageSize: 20
                },
                dialogFormVisible: false,
                addForm: {
                    x1: "",
                    x2: ""
                },
                dialogVisible: false
            }
        },
        methods: {
            clickSearch() {
                console.log(this.searchForm);
            },
            resetSearchForm(formName) {
                this.$refs[formName].resetFields();
            },
            handleClick(row) {
                console.log(row);
                this.dialogVisible = true;
            },
            confirmDelete(row) {
                console.log("确定删除", row);
            },
            handleCurrentChange(page) {
                console.log("想要查看：", page);
            },
            clickAddDrawer() {
                this.drawerVisible = true;
            },
            handleDrawerClose(done) {
                console.log("要关闭了");
                done(); // 关闭
            },
            handleEditClick(row){
                console.log(row);
                this.drawerVisible = true;
            }
        }
    }
</script>

<style scoped>

</style>
