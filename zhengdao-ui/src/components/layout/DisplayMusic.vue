<template>
    <slot>
        <!-- <div v-for="item in posts" :key="item.id">
            {{postposition(item,1,1)}}
        </div> -->
        <div>{{postposition(props.posts,0).name}}</div>
        <div class="infinite-list-wrapper" style="overflow: auto">
            <ul
            v-infinite-scroll="load"
            class="list"
            :infinite-scroll-disabled="disabled"
            >
            <li v-for="i in count" :key="i" class="list-item">

                <el-row :gutter="20">
                <el-col :span="6" v-for="n in 3" :key="n" ><div class="grid-content ep-bg-purple" />
                <!-- {{ postposition(posts,3*(i-1)+n-1).name }} -->
                    
                    <el-skeleton style="width: 240px" :loading="loading" animated>
                        <template #template>
                            <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
                            <div style="padding: 14px">
                            <el-skeleton-item variant="h3" style="width: 50%" />
                            <div
                                style="
                                display: flex;
                                align-items: center;
                                justify-items: space-between;
                                margin-top: 16px;
                                height: 16px;
                                "
                            >
                                <el-skeleton-item variant="text" style="margin-right: 16px" />
                                <el-skeleton-item variant="text" style="width: 30%" />
                            </div>
                            </div>
                        </template>
                        <template #default>
                            <el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
                            <img
                                src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                class="image"
                            />
                            <div style="padding: 14px">
                                <span>Delicious hamburger</span>
                                <div class="bottom card-header">
                                <div class="time">{{ currentDate }}</div>
                                <el-button text class="button">Operation button</el-button>
                                </div>
                            </div>
                            </el-card>
                        </template>
                        </el-skeleton>
                
                </el-col>
                </el-row>
            
            
            </li>
            </ul>

            <p v-if="loading">Loading...</p>
            <p v-if="noMore">No more</p>
        </div>
    </slot>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
// import { Component, Prop, Vue } from 'vue-property-decorator'

const count = ref(10)
const loading = ref(false)
const noMore = computed(() => count.value >= 20)
const disabled = computed(() => loading.value || noMore.value)
const currentDate = new Date().toDateString()
const load = () => {
  loading.value = true
  setTimeout(() => {
    count.value += 2
    loading.value = false
  }, 2000)
}
// let posts=[
//   {
//     "cover_address": "/demopicture/example.png",
//     "id": 1,
//     "music_address": "/DEMOMUSIC/crimanal.mp3",
//     "name": "crimanal",
//     "post_date": "2022-08-17T20:13:19",
//     "user_id": 1
//   },
//   {
//     "cover_address": "/demopicture/example.png",
//     "id": 2,
//     "music_address": "/DEMOMUSIC/crimanal.mp3",
//     "name": "dangerous",
//     "post_date": "2022-08-17T20:13:19",
//     "user_id": 2
//   },]
function postposition(post,x){
    return post[x];
}

// export default defineComponent({
//     props:['posts'],
//     setup(){


//     },
// })

const props = defineProps({
    posts: Array,

})

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
  height: 350px;
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
  margin-bottom: 10;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

</style>