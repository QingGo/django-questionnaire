<template>
<div class="navigator">
<div class="container" style="background-color: rgba(11, 214, 45, 0.555);">
    <ul class="nav nav-pills">
        <li class="nav-item active">
        <router-link :to="'/polls'" class="nav-link">
        所有问卷
        </router-link>
        </li>
        <li class="nav-item">
        <router-link :to="'/admin'" class="nav-link">
        管理页面
        </router-link>
        </li>
    </ul>
</div>
</div>
</template>

<script>
export default {
  name: 'navigator'
}
</script>
