<template>
    <div class="common-layout">
      <el-container>
        <el-header>
              <webhead></webhead> 
        </el-header>
        <el-main>
          <el-container>
            <el-aside >
              <sidenavi></sidenavi>
            </el-aside>
            <el-main class="inside-main">
              <div>
                <suspense timeout="100">
                  <EditProfile></EditProfile>
                </suspense>
              </div>
              
            </el-main>
          </el-container>
        </el-main>
        <bfooter>
  
        </bfooter>
      </el-container>
    </div>
  </template>
  <script lang="ts" setup>
  import sidenavi from '../../components/layout/sidenavi.vue';
  import webhead from '../../components/layout/webhead.vue';
  import bfooter from '../../components/layout/bottomfooter.vue';
  import EditProfile from '../../components/function/ProfileEdit.vue';
  import router from '@/router';
  
  const open = () =>{
    router.push({name:'PersonalEdit'})
  }
  
  
  </script>
  <style scoped>
  .el-aside{
    background-color: #0b1c2c;
  }
  .el-main{
    background-color: #0b1c2c;
    padding-right:50px;
    padding-left:50px;
    padding-block-start: 0px;
  }
  .el-main.inside-main{
    padding-left:20px;
    padding-right:150px;
  }
  .el-header{
    background-color: #0b1c2c;
  }
  .el-header{
    height:60px;
    padding-left: 0px;
    padding-right: 0px;
  }
   
  .common-layout{
    margin-bottom: 0px;
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
  
  </style>
  