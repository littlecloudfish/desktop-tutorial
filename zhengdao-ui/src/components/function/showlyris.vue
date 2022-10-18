<template>
    <div>
        <b style="white-space: pre;">{{lyris}}</b>
    </div>
</template>
<script async setup lang="ts">

import { defineComponent } from 'vue'
import {useStore} from 'vuex'
import { inject } from 'vue'

defineComponent({
    setup() {
        
    },
})
const store = useStore();
await store.dispatch('music/musiclyrics', inject('musicid'))
const lyris = await store.getters['music/musiclyrics']

</script>
