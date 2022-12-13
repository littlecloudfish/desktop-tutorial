<template>
    <div class="infinite-list-wrapper" style="overflow: auto">
      <ul
        v-infinite-scroll="load"
        class="list"
        :infinite-scroll-disabled="disabled"
      >
        <li v-for="i in count" :key="i" class="list-item">
            <el-col v-for="j in 8" :span="4">
                <el-button>{{typearray[i+j]}}</el-button>
            <div class="grid-content ep-bg-purple" /></el-col>
        </li>
      </ul>
      <p v-if="loading">Loading...</p>
      <p v-if="noMore">No more</p>
    </div>
</template>
  
<script lang="ts" setup>
import { computed, ref } from 'vue'
 

const count = ref(3)
const loading = ref(false)
const noMore = computed(() => count.value >= 20)
const disabled = computed(() => loading.value || noMore.value)
const load = () => {
loading.value = true
setTimeout(() => {
    count.value += 2
    loading.value = false
}, 2000)
}
const typearray = ['aa','sdfdaffdfs','dsfsdfsfds','fdsfdsf','ffffffffff','ffdqwewqeqw','sdvdfgerert','dfgqwexcvdfg','dsfytrehtya','dftgeerter','tytreqdfvdg','sdafgyhwer']
</script>

<style>
.infinite-list-wrapper {
height: 600px;
text-align: center;
margin-top: 0.1%;
}
.infinite-list-wrapper .list {
padding: 0;
margin-top: 5%;
list-style: none;
}

.infinite-list-wrapper .list-item {
display: flex;
align-items: center;
justify-content: center;
height: 50px;
background: rgba(0, 0, 0, 0);
color: rgba(0, 0, 0, 0);
}
.infinite-list-wrapper .list-item + .list-item {
margin-top: 10px;
}
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>