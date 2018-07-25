<template>
  <div id="app">
    <myBroad></myBroad>
    <myNavigator></myNavigator>
    <transition name="slide-left">
      <router-view/>
    </transition>
    <ScrollTop></ScrollTop>
    <myFooter></myFooter>
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
