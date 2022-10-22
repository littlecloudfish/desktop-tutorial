<template>
    <el-row class="tac">
      <el-col :span="45"  >
        <el-menu
          active-text-color="#ffd04b"
          background-color="#0b1c2c"
          class="el-menu-vertical-demo"
          default-active="2"
          text-color="#fff"
          @open="handleOpen"
          @close="handleClose"
        >
        <router-link to="/" style="text-decoration: none; color: inherit;">
          <el-menu-item index="1">
            <span>
                  <el-button color="#103057"  type="primary" >
                    <el-icon><House /></el-icon>
                    Home
                  </el-button>
            </span>
          </el-menu-item>
        </router-link>
          <el-sub-menu index="2">
            <template #title>
              <span>
                  <el-button color="#103057" type="primary" >
                    <el-icon><location /></el-icon>
                    <router-link to="/MusicUser" style="text-decoration: none; color: inherit;">User</router-link>
                  </el-button>
              </span>
            </template>
            <el-menu-item-group title="Group One">
              <el-menu-item index="1-1">
                <router-link to="/about" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Medal /></el-icon>
                    My Favorite Music
                  </el-button>
                </router-link>
              </el-menu-item>
              <el-menu-item index="1-2">
                <router-link to="/about" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Medal /></el-icon>
                    My Favorite Singer
                  </el-button>
                </router-link>
              </el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="Group Two">
              <el-menu-item index="1-3">
                <router-link to="/about" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Medal /></el-icon>
                    My Publish
                  </el-button>
                </router-link>
              </el-menu-item>
            </el-menu-item-group>
            <el-menu-item index="1-4">
              <template #title>
                <router-link to="/about" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Medal /></el-icon>
                    My Publish
                  </el-button>
                </router-link>
              </template>
              <!-- <el-menu-item index="1-4-1">item one</el-menu-item> -->
            </el-menu-item>
          </el-sub-menu>
          
          <el-menu-item index="3">
            <router-link to="/MusicScoreBoard" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Medal /></el-icon>
                    Score Board
                  </el-button>
              </router-link>
          </el-menu-item>
          <el-menu-item index="4">
            <span>
              <router-link to="/about" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Sugar /></el-icon>
                    Singer
                  </el-button>
              </router-link>
            </span>
          </el-menu-item>
          <el-menu-item index="5">
            <span>
              <router-link to="/MusicType" style="text-decoration: none; color: inherit;">
                  <el-button color="#103057" type="primary" >
                    <el-icon><Grid /></el-icon>
                    Music Type
                  </el-button>
              </router-link>
            </span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </template>
  
  <script lang="ts" setup>
  
  const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  </script>

<style>
.el-menu{
  border-right: 0px;
}
</style>