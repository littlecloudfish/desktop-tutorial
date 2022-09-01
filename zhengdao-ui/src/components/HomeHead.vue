<template>
  <header>
    <nav>
          <el-breadcrumb separator=" ">
            <el-breadcrumb-item :to="{ path: '/' }"><el-button type="primary" >MountainMusic</el-button></el-breadcrumb-item>
            <el-breadcrumb-item>
              <div class="flex flex-wrap items-center">
                <el-dropdown>
                  <el-button type="primary" >
                    <a href="/about">User</a>
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item><a href="/about">My Favorite Music</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">My Favorite Singers</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">My Publish</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">Upload </a></el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
              </el-dropdown>
              </div>
            </el-breadcrumb-item>
            <el-breadcrumb-item><el-button type="primary" >Search</el-button></el-breadcrumb-item>
            <el-breadcrumb-item><el-button type="primary" >Latest Music</el-button></el-breadcrumb-item>
            <el-breadcrumb-item>
              <div class="flex flex-wrap items-center">
                <el-dropdown>
                  <el-button type="primary" >
                    <a href="/about">ScoreBoard</a>
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item><a href="/about">Forever Legend</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">Hottest Users</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">Monthly Score</a></el-dropdown-item>
                      <el-dropdown-item><a href="/about">Weekly Score</a></el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
              </el-dropdown>
              </div>
            </el-breadcrumb-item>
          </el-breadcrumb>
      </nav>
    <router-view/>
  </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeHead',
  props: {
    msg: String,
  },
});
</script>

<style scoped lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>