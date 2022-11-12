<template>
	<div>
		<h2>hello world 单页面组件</h2>
	</div>
</template>
<script>
	export default{
		data(){
			return {msg:'vue-cli3开发但文件组件'}
		}
	}
</script>
// scoped表示css样式只对当前组件生效
<style scoped> 
	h3{
		color:red;
	}
</style>









