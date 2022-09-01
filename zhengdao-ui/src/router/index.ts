import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/MusicHome.vue') 
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/MusicHome',
    name: 'MusicHome',
    component: () => import('../views/MusicHome.vue') 
  },
  {
    path: '/MusicUser',
    name: 'MusicUser',
    component: () => import('../views/User/MusicUser.vue') 
  },
  {
    path: '/MusicUserLogin',
    name: 'MusicUserLogin',
    component: () => import('../views/User/MusicUserLogin.vue') 
  },
  {
    path: '/MusicUserRegister',
    name: 'MusicUserRegister',
    component: () => import('../views/User/MusicUserRegister.vue') 
  },
  {
    path: '/MusicUserUpload',
    name: 'MusicUserUpload',
    component: () => import('../views/User/MusicUserUpload.vue') 
  },
  {
    path: '/MusicPlay',
    name: 'MusicPlay',
    component: () => import('../views/Music/MusicPlay.vue') 
  },
  {
    path: '/MusicSearch',
    name: 'MusicSearch',
    component: () => import('../views/Music/MusicSearch.vue') 
  },
  {
    path: '/MusicLatest',
    name: 'MusicLatest',
    component: () => import('../views/Music/MusicLatest.vue') 
  },
  {
    path: '/MusicScoreBoard',
    name: 'MusicScoreBoard',
    component: () => import('../views/Music/MusicScoreBoard.vue') 
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
