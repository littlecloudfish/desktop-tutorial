import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'
import store from './store'
import App from './App.vue'
import AudioVisual from 'vue-audio-visual'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import PlayMusic from './components/function/PlayMusic.vue'
import DisplayMusic from './components/layout/DisplayMusic.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

const app = createApp(App)

app.use(ElementPlus).use(VueAxios, axios).use(store).use(router).use(AudioVisual).mount('#app')
app.component('PlayMusic',PlayMusic)
app.component('DisplayMusic',DisplayMusic)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }