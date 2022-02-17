<template>
  <div class="post">
    <div v-if="loading" class="loading">Loading.....</div>
    <div v-if="error" class="error">{{error}}</div>
    <div v-if="post">
      <h3>标题:{{post.title}}</h3>
      <p>内容:{{post.body}}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: null,
      error: null,
      loading: false
    };
  },
// 导航完成之后获取数据
  created() {
    console.log(this.$https);
    this.getPostData();
  },
  watch: {
    $route: "getPostData"
  },
  methods: {
    async getPostData() {
      try {
        this.loading = true;
        const { data } = await this.$https.get("/api/post");
        this.loading = false;
        this.post = data;
      } catch (error) {
        this.error = error.toString();
      }
    }
  }
};
</script>

<style lang="scss" scoped>
</style>