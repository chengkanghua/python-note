<template>
    <div>
        <h3>Page页面</h3>
    </div>
</template>

<script>
    export default {
        created () {
            // console.log(this.$route);
            const {id,title} = this.$route.query;
            console.log(id,title);
            // 与后端发生交互
        },
    }
</script>

<style lang="scss" scoped>

</style>