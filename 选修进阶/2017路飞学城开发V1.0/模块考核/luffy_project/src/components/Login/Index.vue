<template>
	<div class="app">
			<h3>Index</h3>
			<button @click="logoutHandler">退出</button>
	</div>
</template>

<script>
export default {
  name: 'Index',
  data(){
    return {}
  },
  methods:{
	  logoutHandler(){
		  let username = window.localStorage.getItem('username','')
		  let access_token = window.localStorage.getItem('access_token','')
		  let params = {
			  access_token:access_token
		  }
		  this.$http.logout(params)
		  .then(res=>{
			  console.log(res)
			  if(res.error === null){
				  this.$router.push({
					  name:"Login"
				  });
				  localStorage.removeItem('access_token')
				  localStorage.removeItem('username')
			  }
		  })
		  .catch(err=>{
			  console.log(err);
		  })

	  }
  },
  created(){
	  let access_token = window.localStorage.getItem("access_token","")
	  if(!access_token){
		  this.$router.push({
			  name:'Login'
		  })
	  }
  }	
};
</script>

<style lang="css" scoped>

</style>
