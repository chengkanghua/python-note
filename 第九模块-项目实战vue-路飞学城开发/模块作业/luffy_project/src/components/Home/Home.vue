<template>

		<el-carousel indicator-position="outside" height = '400px'>
		    <el-carousel-item v-for="item in lunboImgs" :key="item.id">
		      <img :src="item.imgSrc" alt="">
		    </el-carousel-item>
		 </el-carousel>

</template>

<script>
export default {

  name: 'Home',
  data() {
    return {
    	lunboImgs:[
        {
          id:1,
          imgSrc:'https://hcdn2.luffycity.com/media/frontend/course/python-8days-camp.png'
        },
         {
          id:2,
          imgSrc:'https://hcdn2.luffycity.com/media/frontend/course/python-8days-camp.png'
         },
           {
            id:3,
            imgSrc:'https://hcdn2.luffycity.com/media/frontend/course/python-8days-camp.png'
          },
          {
            id:4,
            imgSrc:'https://hcdn2.luffycity.com/media/frontend/course/python-8days-camp.png'
          }
      ]
    };
  },
  created(){
    // console.log(localStorage);
  }
};
</script>

<style lang="css" scoped>

img{
	width: 100%;
}
</style>
