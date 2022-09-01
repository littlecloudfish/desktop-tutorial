<template>
  <div class="common-layout">
    <el-container>
        <el-aside width="200px">
        <!-- <el-row><el-col :span="6"><el-icon>Home<House /></el-icon></el-col></el-row>
        <el-row><el-col :span="6"><el-icon>New<House /></el-icon></el-col></el-row>
       -->
            <el-row><a href="/MusicUserUpload">Upload Music</a></el-row>
            <el-row><a href="/MusicUserUpload">User Information</a></el-row>

        </el-aside>
        <el-main>Main
            <!-- <el-row><el-icon><House /><a href="/about">Home</a></el-icon></el-row> -->
            
            <div class="infinite-list-wrapper" style="overflow: auto">
      <ul
        v-infinite-scroll="load"
        class="list"
        :infinite-scroll-disabled="disabled"
      >
        <li v-for="i in count" :key="i" class="list-item">
          <el-row :gutter="20">
            <el-col :span="6" v-for="n in 3" :key="n"><div class="grid-content ep-bg-purple" />{{i+n}}
                <el-skeleton style="width: 300px">
                  <template #template>
                  <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
                   <div style="padding: 14px">
                   <el-skeleton-item variant="p" style="width: 50%" />
                   <div
                      style="
                        display: flex;
                        align-items: center;
                        justify-items: space-between;
                      "
                    >
          <el-skeleton-item variant="text" style="margin-right: 16px" />
          <el-skeleton-item variant="text" style="width: 30%" />
        </div>
      </div>
      </template>
  </el-skeleton>
            </el-col>
          </el-row>
        </li>
      </ul>
      <p v-if="loading">Loading...</p>
      <p v-if="noMore">No more</p>
    </div>
        </el-main>
    </el-container>
  </div>
</template>
<style lang="scss">
.el-row {
  margin-bottom: 20px;
}
</style>
<!-- <script src="//unpkg.com/@element-plus/icons-vue"></script> -->


<script lang="ts" setup>
import { computed, ref } from 'vue'

const count = ref(6)
const loading = ref(false)
const noMore = computed(() => count.value >= 15)
const disabled = computed(() => loading.value || noMore.value)
const load = () => {
  loading.value = true
  setTimeout(() => {
    count.value += 2
    loading.value = false
  }, 3500)
}
</script>

<style>
.infinite-list-wrapper {
  height: 900px;
  text-align: center;
}
.infinite-list-wrapper .list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.infinite-list-wrapper .list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 400px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
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
  border-radius: 10px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

</style>
