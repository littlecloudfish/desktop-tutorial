<template>
    <el-scrollbar>
        
            <div class="scrollbar-flex-content">
                <p v-for="item in listofuser" :key="item" class="scrollbar-demo-item">
                  <router-link :to="'MusicUser/'+item.id">
                      <div class="demo-basic--circle" > 
                          <el-row>
                              <el-avatar :size="60" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
                          </el-row>
                          <el-row>
                              {{item.fullname}}
                          </el-row> 
                    </div>
                  </router-link>
                </p>
            </div>
        
    </el-scrollbar>
</template>

<script async lang="ts" setup>
import { defineComponent } from 'vue'
import {useStore} from 'vuex'
import { inject } from 'vue'

// defineComponent({
//     setup() {
//     },
// })
const store = useStore();
await store.dispatch('userInfo/userlist');
const listofuser = await store.getters['userInfo/listofuser']
// for append
</script>


  <style scoped>
  .scrollbar-flex-content {
    display: flex;
  }
  .scrollbar-demo-item {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 150px;
    margin: 0px;
    text-align: center;
    border-radius: 4px;
    background: "0b1c2c"; /* change to 1  */
    color: var(--el-color-danger);
  }
 
  .demo-basic {
  text-align: center;

}

  .demo-basic--circle{
    background-color:"0b1c2c";
    width: auto;
} 
/*  
    .demo-basic .sub-title {
    margin-bottom: 10px;
    font-size: 14px;
    color: var(--el-text-color-secondary);
    }
    .demo-basic .demo-basic--circle,
    .demo-basic .demo-basic--square {
    display: flex;
    justify-content: space-between;
    align-items: center;
    }
    .demo-basic .block:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
    }
    .demo-basic .block {
    flex: 1;
    }
    .demo-basic .el-col:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
    } */


  </style>