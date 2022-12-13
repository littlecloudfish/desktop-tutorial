<template>
    <slot>
      <div v-if="posts.length === 0">
       <p style="color:white">No Music Display </p>
      </div>

      <div v-else>
        <div class="infinite-list-wrapper" style="overflow: auto">
            <ul
            v-infinite-scroll="load"
            class="list"
            :infinite-scroll-disabled="disabled"
            >
            <li v-for="i in count" :key="i" class="list-item"  >
              <div v-if="i != undefined && i != lengthofpost + 1">
                <el-row :gutter="20">
                <el-col :span="6" v-for="n in 4" :key="n" >
                    
                      <el-skeleton style="width: 240px" :loading="loading" animated>
                          <template #template >
                              <el-skeleton-item variant="image" style="width: 200px; height: 200px" />
                              <div style="padding: 14px">
                              <el-skeleton-item variant="h3" style="width: 50%" />
                              <div
                                  style="
                                  display: flex;
                                  align-items: center;
                                  justify-items: space-between;
                                  margin-top: 0px;
                                  height:0px;
                                  
                                  "
                              >
                                  <el-skeleton-item variant="text" style="margin-right: 16px" />
                                  <el-skeleton-item variant="text" style="width: 30%" />
                              </div>
                              </div>
                          </template>
                          <template #default  >
                              <el-card :body-style="{ padding: '0px', marginBottom: '0px', background: '#0b1c2c',  }">
                                <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(i-1)+n-1).id}}">
                                  <el-image style="width: 150px; height: 150px" :src="url+postposition(posts,4*(i-1)+n-1).id " :fit="scale-down" />
                                </router-link> 
                                <div style="padding: 25px">
                                    <span>{{ postposition(posts,4*(i-1)+n-1).name }}</span>
                                    <div class="bottom card-header">
                                    <div class="time">{{ postposition(posts,4*(i-1)+n-1).post_date }}</div>
                                    <el-button text class="button">
                                      <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(i-1)+n-1).id}}">
                                        open
                                      </router-link>
                                    </el-button>
                                    </div>
                                </div>
                              </el-card>
                          </template>
                          </el-skeleton>
                </el-col>
                </el-row>  
              </div>
              <!-- <div v-if="i == lengthofpost + 1 && remainder !=0" class="list-single-item">
                <el-row :gutter="20">
                    <el-col :span="6" v-for="n in remainder" :key="n" >
                          <el-skeleton style="width: 240px" :loading="loading" animated>
                              <template #template >
                                  <el-skeleton-item variant="image" style="width: 200px; height: 200px" />
                                  <div style="padding: 14px">
                                  <el-skeleton-item variant="h3" style="width: 50%" />
                                  <div
                                      style="
                                      display: flex;
                                      align-items: center;
                                      justify-items: space-between;
                                      margin-top: 0px;
                                      height:0px;
                                      
                                      "
                                  >
                                      <el-skeleton-item variant="text" style="margin-right: 16px" />
                                      <el-skeleton-item variant="text" style="width: 30%" />
                                  </div>
                                  </div>
                              </template>
                              <template #default  >
                                  <el-card :body-style="{ padding: '0px', marginBottom: '0px', background: '#0b1c2c',  }">
                                    
                                      <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(count)+n-1).id}}">
                                      <el-image style="width: 150px; height: 150px" :src="url+postposition(posts,4*(count)+n-1).id " :fit="scale-down" />
                                    </router-link> 
                                    <div style="padding: 25px">
                                        <span>{{ postposition(posts,4*(count)+n-1).name }}</span>
                                        <div class="bottom card-header">
                                        <div class="time">{{ postposition(posts,4*(count)+n-1).post_date }}</div>
                                        <el-button text class="button">
                                          <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(count)+n-1).id}}">
                                            open
                                          </router-link>
                                        </el-button>
                                        </div>
                                    </div>
                                  </el-card>
                              </template>
                              </el-skeleton>
                    </el-col>
                    </el-row>
              </div> -->
             
            </li>
                <li v-if="remainder !=0 && count == lengthofpost" class="list-single-item">
                  <div>
                    <el-row :gutter="20">
                    <el-col :span="3"></el-col>
                    <el-col :span="6" v-for="n in remainder" :key="n" >
                          <el-skeleton style="width: 240px" :loading="loading" animated>
                              <template #template >
                                  <el-skeleton-item variant="image" style="width: 200px; height: 200px" />
                                  <div style="padding: 14px">
                                  <el-skeleton-item variant="h3" style="width: 50%" />
                                  <div
                                      style="
                                      display: flex;
                                      align-items: center;
                                      justify-items: space-between;
                                      margin-top: 0px;
                                      height:0px;
                                      
                                      "
                                  >
                                      <el-skeleton-item variant="text" style="margin-right: 16px" />
                                      <el-skeleton-item variant="text" style="width: 30%" />
                                  </div>
                                  </div>
                              </template>
                              <template #default  >
                                  <el-card :body-style="{ padding: '0px', marginBottom: '0px', background: '#0b1c2c',  }">
                                    
                                      <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(count)+n-1).id}}">
                                      <el-image style="width: 150px; height: 150px" :src="url+postposition(posts,4*(count)+n-1).id " :fit="scale-down" />
                                    </router-link> 
                                    <div style="padding: 25px">
                                        <span>{{ postposition(posts,4*(count)+n-1).name }}</span>
                                        <div class="bottom card-header">
                                        <div class="time">{{ postposition(posts,4*(count)+n-1).post_date }}</div>
                                        <el-button text class="button">
                                          <router-link :to="{name:'MusicPlay',params:{id:postposition(posts,4*(count)+n-1).id}}">
                                            open
                                          </router-link>
                                        </el-button>
                                        </div>
                                    </div>
                                  </el-card>
                              </template>
                              </el-skeleton>
                    </el-col>
                    </el-row>
                  </div> 
                </li>
             
            </ul>
            <p v-if="noMore && ifremain " style="color:white">No more Display</p>
            <p v-if="loading">Loading...</p>
            
        </div>
      </div>
        
    </slot>
</template>

<script lang="ts" setup>
import { computed, ref, inject } from 'vue'
// import { Component, Prop, Vue } from 'vue-property-decorator'
const url = "http://127.0.0.1:1943/showmusicimage/"
const lengthofpost = Math.floor( props.posts.length/4 )
const remainder = props.posts.length%4
const ifremain = ref(true)
// const ifremain = computed(()=>{return remainder == 0;})
const count = ref(0)
const loading = ref(false)
const noMore = computed(() => { 
  return count.value >= lengthofpost;
  
}
)
const disabled = computed(() => { 

  return loading.value || count.value >= lengthofpost;
})
const currentDate = new Date().toDateString()
const load = () => {
  loading.value = true
  setTimeout(() => {
    if(count.value <= lengthofpost-2){
      count.value += 2
      loading.value = false
    }  
    else{
      count.value += 1
      loading.value = false
      noMore
      disabled
    }
  }, 2000)
}

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
  height: 600px;
  text-align: center;
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.infinite-list-wrapper .list {
  padding: 0;
  margin: 0;
  list-style: none;
  background: "0b1c2c"; 
  color: "0b1c2c";
}

.infinite-list-wrapper .list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 350px;
  /* background: var(--el-color-danger-light-1);
  color: var(--el-color-danger); */
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.infinite-list-wrapper .list-single-item{
  /* display: flex; */
  align-items: center;
  justify-content: center;
  height: 350px;
  /* background: var(--el-color-danger-light-1);
  color: var(--el-color-danger); */
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.infinite-list-wrapper .list-item + .list-item {
  margin-top: 0px;
}

.el-row {
  margin-bottom: 0px;
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 0px;
}

.grid-content {
  border-radius: 0px;
  min-height: 0px;
}
.list-item{
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.grid-content ep-bg-purple{
  background: "0b1c2c"; 
  color: "0b1c2c";
}
.el-card{
  border: 0px;
  border-radius: 0px;
}
.infinite-list-wrapper::-webkit-scrollbar{
  width: 5px;
}
/* .infinite-list-wrapper::-webkit-scrollbar-track{
  box-shadow: inset 0 0 5px grey; 
  border-radius: 10px;
} */
.infinite-list-wrapper::-webkit-scrollbar-thumb {
  background: rgba(82, 122, 180, 0.3); 
  border-radius: 10px;
}
/* .scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
} */
</style>