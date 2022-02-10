<template>
    <div>
        <h1>Page</h1>
    </div>
</template>

<script>
    export default {
        created(){
            // console.log(this.$route)
            const {id,title} = this.$route.query;
            console.log(id,title)
        }
    }
</script>

<style lang="scss" scoped>

</style>