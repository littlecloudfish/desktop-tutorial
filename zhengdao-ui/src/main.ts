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
import BaseDialog from './components/ui/BaseDialog.vue';
import BaseButton from './components/ui/BaseButton.vue';
import axios from 'axios'
import VueAxios from 'vue-axios'
// import Vuetify from 'vuetify';
import AudioPlayer from '@liripeng/vue-audio-player'



const app = createApp(App)

app.use(ElementPlus).use(VueAxios, axios).use(store).use(AudioPlayer).use(router).use(AudioVisual).mount('#app')
app.component('PlayMusic',PlayMusic);
app.component('DisplayMusic',DisplayMusic);
app.component('BaseDialog',BaseDialog);
app.component('base-button', BaseButton);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }