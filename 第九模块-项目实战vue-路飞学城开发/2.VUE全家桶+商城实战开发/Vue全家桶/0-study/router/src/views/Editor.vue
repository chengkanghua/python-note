<template>
    <div>
        <h2>用户编辑页面</h2>
        <textarea v-model="content" name="content" id="" cols="30" rows="10"></textarea>
        <button @click="saveContent">保存</button>

        <ul>
            <li v-for="(item,index) in list" :key="index">
                <h3>{{item.title}}</h3>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                content:'',
                list:[]
            }
        },
        methods:{
            saveContent(){
                this.list.push({
                    title:this.content
                })
                // 清空文本输入框
                this.content='';
            }
        },
        beforeRouteEnter(to,from,next){
            console.log(this) //获得当前组件实例
            next(vm => {
                console.log(vm.content)
            })
        },
        watch:{
            '$route':()=>{

            }
        },
        beforeRouteUpdate(to,from,next){
            // 组件重用的时候 这个方法才起作用
            next();
        },
        beforeRouteLeave(to,from,next){
            if(this.content){

                alert('请确定保存信息之后再离开');
                next(false);
            }else{
                next()
            }

        }

    }
    
</script>

<style lang="scss" scoped>

</style>