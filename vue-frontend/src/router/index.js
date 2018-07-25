import Vue from 'vue'
import Router from 'vue-router'
import myIndex from '@/components/index'
import myDetail from '@/components/detail'
import myResult from '@/components/result'
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
      path: '/detail/:id',
      name: 'detail',
      component: myDetail
    },
    {
      path: '/result/:id',
      name: 'result',
      component: myResult
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
