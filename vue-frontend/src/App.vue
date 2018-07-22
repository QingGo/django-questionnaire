<template>
  <div id="app">
    <myBroad></myBroad>
    <myNavigator></myNavigator>
    <router-view/>
    <myFooter></myFooter>
  </div>
</template>

<script>
import myBroad from './components/broad.vue'
import myNavigator from './components/navigator.vue'
import myFooter from './components/footer.vue'
export default {
  name: 'App',
  components: {
    myBroad,
    myNavigator,
    myFooter
  }
}
</script>
