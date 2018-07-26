<template>
<div class="navigator">
<div class="container">
    <ul class="nav nav-pills">
        <li class="nav-item active">
        <router-link :to="'/polls'" class="nav-link">
        所有问卷
        </router-link>
        </li>
        <li class="nav-item">
        <a :href="'http://'+base_url+'/admin'" class="nav-link" target="_blank">
        管理页面
        </a>
        </li>
        <li class="nav-item">
        <a :href="'http://'+base_url+'/polls/api'" class="nav-link" target="_blank">
        API一览
        </a>
        </li>
    </ul>
</div>
</div>
</template>

<script>
export default {
  name: 'navigator',
  data: function () {
    return {
      base_url: process.env.BASE_URL
    }
  }
}
</script>

<style scoped>
.container {
  background-color: rgba(11, 214, 45, 0.555);
}
</style>
