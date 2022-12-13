<template>
    <el-rate v-model="value"  allow-half :colors="colors" />
    <el-row>
        <el-button type="Success" round @click="submitresult" >Rate Music</el-button>  
    </el-row>
</template>
  
<script lang="ts" setup>
import { ref,inject } from 'vue'
import {useStore} from 'vuex'
const thismusicid = inject('musicid')
const store = useStore();
const value = ref()
const colors = ref(['#99A9BF', '#F7BA2A', '#FF9900'])
const submitresult=()=> {
    store.dispatch('music/setmusicscore', {'musicid':thismusicid,'musicscore':value.value})
    console.log(value.value)
}
</script>