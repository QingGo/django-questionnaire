import Vue from 'vue'
import Router from 'vue-router'
import myIndex from '@/components/index'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    { path: '',
      redirect: '/polls'},
    {
      path: '/polls',
      name: 'index',
      component: myIndex
    },
    {
      path: '/default',
      name: 'HelloWorld',
      component: HelloWorld
    },
    { path: '*',
      redirect: '/polls'
    }
  ]
})
