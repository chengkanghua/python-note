<template>
    <div style="padding: 20px;">
        <el-card class="box-card" shadow="never">
            <el-form :inline="true" class="demo-form-inline" size="small" :model="searchForm" ref="searchForm">

                <el-form-item label="当前任务" prop="category" style="margin-bottom: 0">
                    <el-select placeholder="全部任务" v-model="searchForm.task" @change="changeTask">
                        <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label"
                                   :value="item.value"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>


                <el-form-item label="推广码" prop="category" style="margin-bottom: 0">
                    <el-select placeholder="全部渠道" v-model="searchForm.category">
                        <el-option v-for="item in categoryOptions" :key="item.value" :label="item.label"
                                   :value="item.value"></el-option>
                        <el-option label="区域二" value="beijing"></el-option>
                    </el-select>
                </el-form-item>

            </el-form>

        </el-card>

        <el-row style="margin-top: 30px;" :gutter="20">
            <el-col :span="12">

                <el-row type="flex" justify="space-between" :gutter="20" style="flex-wrap: wrap">
                    <el-col :span="12">
                        <el-card shadow="never" class="stat-panel">
                            <div class="row">
                                <el-row type="flex" justify="space-between">
                                    <div>
                                        <div style="font-size: 40px;font-weight: bold">0</div>
                                        <div>今日新增</div>
                                    </div>
                                    <div>
                                        <i class="el-icon-attract" style="font-size: 60px;color: #0c8eff"></i>
                                    </div>
                                </el-row>
                                <el-row type="flex" justify="space-between">
                                    <div>昨日数据：0</div>
                                    <div>累计：23</div>
                                </el-row>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12">
                        <el-card shadow="never" class="stat-panel">
                            <div class="row">
                                <el-row type="flex" justify="space-between">
                                    <div>
                                        <div style="font-size: 40px;font-weight: bold">0</div>
                                        <div>今日新增</div>
                                    </div>
                                    <div>
                                        <i class="el-icon-attract" style="font-size: 60px;color: #0c8eff"></i>
                                    </div>
                                </el-row>
                                <el-row type="flex" justify="space-between">
                                    <div>昨日数据：0</div>
                                    <div>累计：23</div>
                                </el-row>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12" style="margin-top: 8px">
                        <el-card shadow="never" class="stat-panel">
                            <div class="row">
                                <el-row type="flex" justify="space-between">
                                    <div>
                                        <div style="font-size: 40px;font-weight: bold">0</div>
                                        <div>今日新增</div>
                                    </div>
                                    <div>
                                        <i class="el-icon-attract" style="font-size: 60px;color: #0c8eff"></i>
                                    </div>
                                </el-row>
                                <el-row type="flex" justify="space-between">
                                    <div>昨日数据：0</div>
                                    <div>累计：23</div>
                                </el-row>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="12" style="margin-top: 8px">
                        <el-card shadow="never" class="stat-panel">
                            <div class="row">
                                <el-row type="flex" justify="space-between">
                                    <div>
                                        <div style="font-size: 40px;font-weight: bold">0</div>
                                        <div>今日新增</div>
                                    </div>
                                    <div>
                                        <i class="el-icon-attract" style="font-size: 60px;color: #0c8eff"></i>
                                    </div>
                                </el-row>
                                <el-row type="flex" justify="space-between">
                                    <div>昨日数据：0</div>
                                    <div>累计：23</div>
                                </el-row>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>

            </el-col>
            <el-col :span="12">

                <el-card class="box-card" shadow="never">
                    <highcharts :options="opt1" style="height: 330px;min-width: 300px"></highcharts>
                </el-card>

            </el-col>
        </el-row>


        <el-row style="margin-top: 30px;" :gutter="20" type="flex" justify="space-between">
            <el-col :xs="12">
                <el-card class="box-card" shadow="never">
                    <div slot="header">
                        <span>xx统计情况</span>
                    </div>
                    <highcharts :options="opt2" style="height: 330px;min-width: 300px"></highcharts>
                </el-card>
            </el-col>
            <el-col :xs="12">
                <el-card class="box-card" shadow="never">
                    <div slot="header">
                        <span>裂变情况</span>
                    </div>
                    <highcharts :options="opt3" style="height: 330px;min-width: 300px"></highcharts>
                </el-card>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    export default {
        name: "Stat",
        data() {
            return {
                searchForm: {
                    task: "3",
                    category: ""
                },
                categoryOptions: [
                    {
                        value: '11',
                        label: '黄金糕'
                    }, {
                        value: '12',
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
                opt1: {
                    title: {
                        text: '2010 ~ 2016 年太阳能行业就业人员发展情况'
                    },
                    subtitle: {
                        text: '数据来源：thesolarfoundation.com'
                    },
                    yAxis: {
                        title: {
                            text: '就业人数'
                        }
                    },
                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle'
                    },
                    plotOptions: {
                        series: {
                            label: {
                                connectorAllowed: false
                            },
                            pointStart: 2010
                        }
                    },
                    series: [{
                        name: '安装，实施人员',
                        data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
                    }, {
                        name: '工人',
                        data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
                    }, {
                        name: '销售',
                        data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
                    }, {
                        name: '项目开发',
                        data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
                    }, {
                        name: '其他',
                        data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
                    }],
                    responsive: {
                        rules: [{
                            condition: {
                                maxWidth: 500
                            },
                            chartOptions: {
                                legend: {
                                    layout: 'horizontal',
                                    align: 'center',
                                    verticalAlign: 'bottom'
                                }
                            }
                        }]
                    }
                },
                opt2: {
                    chart: {
                        plotBackgroundColor: null,
                        plotBorderWidth: null,
                        plotShadow: false,
                        type: 'pie'
                    },
                    title: {
                        text: '2018 年浏览器市场份额'
                    },
                    tooltip: {
                        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
                    },
                    plotOptions: {
                        pie: {
                            allowPointSelect: true,
                            cursor: 'pointer',
                            dataLabels: {
                                enabled: false
                            },
                            showInLegend: true
                        }
                    },
                    series: [{
                        name: 'Brands',
                        colorByPoint: true,
                        data: [{
                            name: 'Chrome',
                            y: 61.41,
                            sliced: true,
                            selected: true
                        }, {
                            name: 'Internet Explorer',
                            y: 11.84
                        }, {
                            name: 'Firefox',
                            y: 10.85
                        }, {
                            name: 'Edge',
                            y: 4.67
                        }, {
                            name: 'Safari',
                            y: 4.18
                        }, {
                            name: 'Other',
                            y: 7.05
                        }]
                    }]
                },
                opt3: {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: '月平均降雨量'
                    },
                    subtitle: {
                        text: '数据来源: WorldClimate.com'
                    },
                    xAxis: {
                        categories: [
                            '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'
                        ],
                        crosshair: true
                    },
                    yAxis: {
                        min: 0,
                        title: {
                            text: '降雨量 (mm)'
                        }
                    },
                    tooltip: {
                        // head + 每个 point + footer 拼接成完整的 table
                        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                            '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                        footerFormat: '</table>',
                        shared: true,
                        useHTML: true
                    },
                    plotOptions: {
                        column: {
                            borderWidth: 0
                        }
                    },
                    series: [{
                        name: '东京',
                        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
                    }, {
                        name: '纽约',
                        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]
                    }, {
                        name: '伦敦',
                        data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]
                    }, {
                        name: '柏林',
                        data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]
                    }]
                }

            }
        }
    }
</script>

<style scoped>
    .stat-panel .row {
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
</style>
