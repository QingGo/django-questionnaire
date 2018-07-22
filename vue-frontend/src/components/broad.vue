<template>
<div class="broad">
    <div class="container">
        <h1 class="page-header">
            <router-link :to="'/polls'">
            问卷助手
            </router-link>
        </h1>
    </div>
</div>
</template>

<script>
export default {
  name: 'broad'
}
</script>

<style scoped>
h1.page-header a {
  text-decoration:none;
}
div.broad {
  margin: 10px;
}
</style>
