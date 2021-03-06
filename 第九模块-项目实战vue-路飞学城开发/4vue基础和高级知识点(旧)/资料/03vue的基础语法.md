#### vue的介绍

渐进式的JavaScript框架

    vue           react            angualr
    
    作者:尤雨溪    facebook         谷歌公司


    文档:中文  建议:如果你想学号vue  
    1.看视频  初步的了解vue  
    2.学vue的课 时刻看官网文档  https://cn.vuejs.org/

#### 前端框架和库的区别

##### 功能上的不同

                      ```javascript
jquery库：包含DOM(操作DOM)+请求，就是一块功能。

art-template库：模板引擎渲染，高性能的渲染DOM    (我们后端的一种模板  跟python的模板类似)

框架：大而全的概念，简易的DOM体验+请求处理+模板引擎

在KFC的世界里，库就是一个小套餐，框架就是全家桶。

                      ```



##### 代码上的不同

```javascript
一般使用库的代码，是调用某个函数或者直接使用抛出来的对象，我们自己处理库中的代码。
一般使用框架，其框架本身提供的好的成套的工具帮我们运行我们编写好的代码。
```



##### 框架的使用

- 初始化自身的一些行为
- 执行你所编写的代码
-  释放一些资源

#### nodejs

1.    去官网https://nodejs.org/en/download/ 下载 安装(傻瓜式安装)
2.    打开终端 cmd  :  执行`node -v`   如果出现版本号，证明安装node成功 ，跟安装python雷同

3.    下载完node之后，会自带包管理器 npm，好比 是python中 pip3包管理器。pip3 install xxx
4.    使用npm  
   1. 

    	1.要初始化npm的项目 :  
    	 
    	 npm init  --yes 自动生成一个package.json文件
    	      {
    	       "name": "vue_lesson",
    	       "version": "1.0.0",
    	       "description": "这是我的vue的第一个项目",
    	       "main": "index.js",
    	       "scripts": {
    	         "test": "echo \"Error: no test specified\" && exit 1"
    	       },
    	       "author": "mjj",
    	       "license": "ISC",
    	       "dependencies": {
    	         "vue": "^2.5.16"
    	       }
    	     }
    	  2.npm install vue --save
    	     npm install jquery --save
    	     
    	  3.下载包  npm  uninstall vue --save
    	  
    	  4.下载所有的依赖包 npm install
   

#### vue的起步

   - 引包:    <script type="text/javascript" src="./node_modules/vue/dist/vue.js"></script>
   - 创建实例化对象
     
```javascript
new Vue({
el:'#app',//目的地
data:{
    msg:"hello Vue"
}
});
/*
{{}}: 模板语法插值
    {{变量}}
    {{1+1}}
    {{'hello'}}
    {{函数的调用}}
    {{1==1?'真的':'假的'}}
*/
```

#### 指令系统

           ```javascript
v-text 等价于 {{}}   实现原理:innerText

v-html 	实现原理: innerHTML

表单控件的value (看后面)
           ```

#### v-if和v-show

```javascript

v-if 是“真正”的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。
v-if 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。
相比之下，v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。
一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。

//保存数组或者对象 格式
v-for = '(item,index) in menuList'
v-for = '(value,key) in object'
//item指的是数组中每项元素
```


    <a href="" class='box'></a>
    <img src="" alt="">
    使用v-bind:class = '{}||[]||变量名||常量' 对我们的页面中标签的属性进行绑定 所有的属性都可以进行绑定,注意只要使用了v-bind 后面的字符串一定是数据属性中的值


​        
```javascript

  // 1.事件源 2.事件  3.事件驱动程序

vue中使用v-on:click对当前DOM绑定click事件 注意:所有的原生js的事件使用v-on都可以绑定

v-if和v-on 来对页面中DOM进行操作

v-bind:class和v-on对页面中DOM的样式切换

v-bind和v-on

在vue中它可以简写: v-bind:         
:class 等价于 v-bind:class   
:src 等价于v-bind:src
:id 等价于v-bind:id
v-on:click   等价于 @click = '方法名'
```


```javascript
v-text  v-html  {{}}: 对页面的dom进行赋值运算   相当与js中innerText innerHTML

v-if = 'true':
//创建
var oP =   document.createElement('p')  ;
oDiv.appendChild(op)

v-if = 'false'
//销毁
oDiv.removeChild(op)
v-show = 'true'
oDiv.style.display = 'block'
v-show:'true'
oDid.style.display = 'none'

v-bind:class
oDiv.className += ' active'

/*
渐进式的JavaScript框架
做加法和做减法:大部分的人觉得做加法简单,做减法难
vue这个框架 将 做减法的事情都给咱们做了(难的部分)
学习简单的部分就能实现复杂的dom操作
*/
```

####  局部组件的使用

​            打油诗: 1.声子  2.挂子  3.用

   ```javascript

var App = {
    tempalte:`
      <div class='app'></div>`
};

//2.挂子

new Vue({
    el:"#app",
    //用子	
    template:<App />
    components:{
       App
    }

})

   ```





##### (1)父组件向子组件传递数据:通过Prop

​            Vheader

     ```javascript
1.在子组件自定义特性。props:['自定义的属性1','自定义属性2']

当一个值传递给一个 prop 特性的时候，它就变成了那个组件实例的一个属性,那么我们就可以像访问data中的值一样      
     ```

    2.要在父组件中导入的子组件内部 绑定自定义的属性 <Vheader :title = '父组件中data声明的数据属性'/>

> ​    注意:一个组件默认可以拥有任意数量的 prop，任何值都可以传递给任何 prop。

##### (2)如何从子组件传递数据到父组件

        1.给子组件中的某个按钮绑定原声事件,。我们可以调用内建的 this.$emit('自定义的事件名','传递的数据')，来向父级组件触发一个自定义的事件.
    
        2.在父组件中的子组件标签中 要绑定自定义的事件,

#####   全局组件的使用:

   ```javascript
Vue.component('全局组件的名字',{

    跟new Vue() 实例化对象中的options是一样，但是要注意：

    不管是公共组件还是局部组件 data必须是个函数 函数一定要返回 {}
})

   ```

      <slot> 元素作为承载分发内容的出口

#### 过滤器的使用

#####  局部过滤器

```javascript
 //1.注册局部过滤器 在组件对象中定义
filters:{

	'过滤器的名字':function(value){
	} 	
}
//2.使用过滤器 使用管道符 | 
{{price  | '过滤器的名字'}}
```

##### 全局过滤器

```javascript
// 注册全局的过滤器
//第一个参数是过滤器的名字，第二个参数是执行的操作

Vue.filter('reverse',function(value) {    
    return value.split('').reverse().join('');
});

//使用跟 局部过滤器一样
```

#### 计算属性computed和侦听器（watch）

##### 侦听的是单个属性

```javascript
watch:{

	数据属性的名字：function(value){

	},
	数据属性的名字2：function(value){

	}
}
```


##### 侦听多个属性:计算属性 computed 

{{str.split('').reverse().join('')}} 

```javascript
计算属性 :默认只有getter方法

data(){

  return {

    name:'alex',

    age:18

}

}

compuetd:{

      key:value

      计算属性的方法名:funtion(){

        return ${this.name}他的年龄是${this.age}岁

    }

}

var musicData = [

      {

        id:1,

        name:'于荣光 - 少林英雄',

        author:'于荣光',

        songSrc:'./static/于荣光 - 少林英雄.mp3'

      },

      {

        id:2,

        name:'Joel Adams - Please Dont Go',

        author:'Joel Adams',

        songSrc:'./static/Joel Adams - Please Dont Go.mp3'

      },

      {

        id:3,

        name:'MKJ - Time',

        author:'MKJ',

        songSrc:'./static/MKJ - Time.mp3'

      },

      {

        id:4,name:'Russ - Psycho (Pt. 2)',

        author:'Russ',

        songSrc:'./static/Russ - Psycho (Pt. 2).mp3'

      }

    ];

```



#### 生命周期(钩子函数)



```javascript
beforeCreate(){

// 组件创建之前

console.log(this.msg);

},

created(){

// 组件创建之后

// 使用该组件，就会触发以上的钩子函数，created中可以操作数据，发送ajax，并且可以实现vue==》页面的影响  应用：发送ajax请求

console.log(this.msg);

// this.msg = '嘿嘿黑';

},

beforeMount(){

// 装载数据到DOM之前会调用

console.log(document.getElementById('app'));

},

mounted(){

// 这个地方可以操作DOM

// 装载数据到DOM之后会调用 可以获取到真实存在的DOM元素，vue操作以后的DOM

console.log(document.getElementById('app'));

},

beforeUpdate(){

// 在更新之前，调用此钩子，应用：获取原始的DOM

console.log(document.getElementById('app').innerHTML);

},

updated(){

// 在更新之前，调用此钩子，应用：获取最新的DOM

console.log(document.getElementById('app').innerHTML);

},

beforeDestroy(){

console.log('beforeDestroy');

},

destroyed(){

console.log('destroyed');

},

activated(){

console.log('组件被激活了');

},

deactivated(){

console.log('组件被停用了');

}

```


```javascript
 // $属性： 
   // $refs获取组件内的元素
  // $parent:获取当前组件的父组件
  // $children:获取当前组件的子组件
  // $root:获取New Vue的实例化对象
  //$el:获取组件对象的DOM元素
```
#### 获取更新之后的dom添加事件的特殊情况

```javascript
$nextTick 是在下次Dom更新循环结束之后执行的延迟回调，在修改数据之后使用$nextTick ，	
	则可以在回调中获取更新之后的DOM



```


​    



