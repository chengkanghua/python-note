module.exports = {
    devServer:{
        //  每次修改这个文件一定要重启服务才能生效 npm run serve
        // mock数据模拟
        before(app,server){
            //接口
            app.get('/api/cartList',(req,res)=>{
                res.json({
                    result:[
                        {id:1,title:'Vue实战开发',price:188,active:true,count:1},
                        {id:2,title:'React 实战开发',price:288,active:true,count:1}
                    ]
                })
            })
        }
    }

}
