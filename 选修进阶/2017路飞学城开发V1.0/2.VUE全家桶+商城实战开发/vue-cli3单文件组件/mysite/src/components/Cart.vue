<template>
    <div>
        <!-- <h2>{{title}}</h2> -->
        <el-table
        ref="multipleTable"
        :data="cart"
        border
        tooltip-effect="dark"
        style="width: 50%"
        @selection-change="handleSelectionChange">
        <el-table-column type="selection" width="55"> </el-table-column>
        <el-table-column prop="title" label="课程" width="120"> </el-table-column>
        <el-table-column prop="price" label="价格" width="120"> </el-table-column>
        <el-table-column label="数量"  width="200">
            <template slot-scope="scope">
                <el-input-number v-model="scope.row.count"  :min="1" :max="100" label="描述文字"></el-input-number>
            </template>
        </el-table-column>
        <el-table-column label="总价" width="120"> 
            <template slot-scope="scope">
                ¥{{ scope.row.count * scope.row.price }}
            </template>
        </el-table-column>

  </el-table>
        <table border="1" >
            <tr>
                <th>#</th>
                <th>课程</th>
                <th>单价</th>
                <th>数量</th>
                <th>总价</th>
            </tr>
            <tr v-for="(c,index) in cart" :key="c.id">
                <td>
                    <input type="checkbox" v-model="c.active">
                </td>
                <td>{{c.title}}</td>
                <td>{{c.price}}</td>
                <td>
                    <button @click='substract(index)'>-</button>
                    {{c.count}}
                    <button @click='add(index)'>+</button>
                </td>
                <td>￥{{c.price*c.count}}</td>
            </tr>
            <tr>
                <td></td>
                <td colspan="2">{{ activeCount}}/{{count}}</td>
                <td colspan="2">￥{{ total }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        name:'Cart',
        props:['title'],
        data(){
            return {
                cart:JSON.parse(localStorage.getItem('cart')) || [],
                multipleSelection:[]
            }
        },
        watch:{
            cart:{
                handler(n){
                    this.setLocalData(n);
                },
                deep:true
            }
        },
        created(){
            this.$bus.$on('addCart',good=>{
               const ret = this.cart.find(v=>v.id===good.id);//返回符合条件的元素对象
               console.log(ret);
               if(!ret){
                   //购物车没有数据
                   this.cart.push(good);
               }else{
                   ret.count +=1;
               }
            })
        },
        computed:{
            count(){
                return this.cart.length
            },
            activeCount(){
                return this.cart.filter(v=>v.active).length
                // return this.multipleSelection.filter(v => v.active).length;
            },
            total(){
                // let sum = 0;
                // this.cart.forEach(c => {
                //     if(c.active){
                //         sum +=c.price*c.count;
                //     }
                // });
                // return sum;
                return this.cart.reduce((sum,c)=>{
                    if(c.active){
                        sum += c.price * c.count;
                    }
                    return sum;
                },0)
            }
        },
        methods: {
            handleSelectionChange(val) {
                this.multipleSelection = val;
                console.log(this.multipleSelection)
            },

            setLocalData(n){
                localStorage.setItem('cart',JSON.stringify(n));
            },
            remove(i){
                if(window.confirm('确定是否删除？')){
                    this.cart.splice(i,1);
                }
            },
            substract(i) {
               let count = this.cart[i].count;
               count > 1 ? this.cart[i].count -=1 : this.remove(i);
            },
            add(i){
                 this.cart[i].count++;
            },
            toggleSelection(rows) {
                if (rows) {
                rows.forEach(row => {
                    this.$refs.multipleTable.toggleRowSelection(row);
                });
                } else {
                this.$refs.multipleTable.clearSelection();
                }
            },
            

 
        },
    }
</script>

<style scoped>

</style>