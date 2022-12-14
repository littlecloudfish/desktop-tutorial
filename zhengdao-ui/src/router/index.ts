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
    path: '/MusicUser/:id',
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
    path: '/Personal',
    name: 'Personal',
    component: () => import('../views/User/MyProfile.vue') 
  },
  {
    path: '/PersonalEdit',
    name: 'PersonalEdit',
    component: () => import('../views/User/EditProfile.vue') 
  },
  {
    path: '/MusicPlay/:id',
    name: 'MusicPlay',
    component: () => import('../views/Music/MusicPlay.vue')
  },  
  {
    path: '/MusicSearch',
    name: 'MusicSearch',
    component: () => import('../views/Music/MusicSearch.vue'),
    children: [
      {
        path:'try',
        component: () => import('../views/Music/TryAlwaysPlay.vue'),
      }
    ] 
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
  {
    path: '/MusicType',
    name: 'MusicType',
    component: () => import('../views/Music/Musictype.vue') 
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/AboutView.vue') 
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
