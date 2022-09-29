<template>
    <el-scrollbar>
        
            <div class="scrollbar-flex-content">
                <p v-for="item in 10" :key="item" class="scrollbar-demo-item">
                    <div class="demo-basic--circle"> 
                        <el-row>
                            <el-avatar :size="60" :src="circleUrl" />
                        </el-row>
                        <el-row>
                            bigblueass
                        </el-row> 
                   </div>
                </p>
            </div>
        
    </el-scrollbar>
</template>
  
<script lang="ts" setup>
    import { reactive, toRefs } from 'vue'
    
    const state = reactive({
      circleUrl:
        'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
      
      sizeList: ['small', '', 'large'] as const,
    })
    
    const { circleUrl, sizeList } = toRefs(state)
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
    background: var(--el-color-danger-light-9); /* change to 1  */
    color: var(--el-color-danger);
  }
 
  .demo-basic {
  text-align: center;

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