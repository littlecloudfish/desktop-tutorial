import { createStore } from 'vuex';
import authModule from './modules/auth/index.js';
import userInfoModule from './modules/auth/index.js';

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
    userInfo: userInfoModule,
  }
})
