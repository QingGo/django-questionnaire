<template>
  <div id="app">
    <myBroad></myBroad>
    <myNavigator></myNavigator>
    <transition name="slide-left">
      <router-view/>
    </transition>
    <ScrollTop></ScrollTop>
    <myFooter></myFooter>
    <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=1 height=1 src="//music.163.com/outchain/player?type=2&id=29805419&auto=1&height=32"></iframe>
  </div>
</template>

<script>
import myBroad from './components/broad.vue'
import myNavigator from './components/navigator.vue'
import myFooter from './components/footer.vue'
import ScrollTop from './components/ScrollTop.vue'

export default {
  name: 'App',
  components: {
    myBroad,
    myNavigator,
    ScrollTop,
    myFooter
  }
}
</script>

<style scoped>
div#app {
  background:url("./assets/grid.png") repeat-x;
  background-attachment:fixed
}
</style>
