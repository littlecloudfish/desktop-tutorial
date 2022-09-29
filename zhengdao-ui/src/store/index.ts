import { createStore } from 'vuex';
import authModule from './modules/auth/index.js';
import userinfoModule from './modules/userinfo/index.js';
import requestModule from './modules/request/index.js';
import musicModule from './modules/music/index.js';

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth: authModule,
    userInfo: userinfoModule,
    request: requestModule,
    music: musicModule,
  }
})
