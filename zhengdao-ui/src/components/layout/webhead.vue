<template>
    <div class="affix-container">
      <el-affix target=".affix-container" :offset="80">
        <!-- <el-button type="primary">Target container</el-button> -->
        <el-autocomplete
            v-model="state"
            :fetch-suggestions="querySearchAsync"
            placeholder="Please input"
            @select="handleSelect">
            <template #prepend>
                <el-select v-model="select" placeholder="Select" style="width: 115px">
                <el-option label="Restaurant" value="1" />
                <el-option label="Order No." value="2" />
                <el-option label="Tel" value="3" />
                </el-select>
            </template>
            <template #append>
                <el-button :icon="Search" />
            </template>
        </el-autocomplete>    
      </el-affix>
      <b style="color:#FFFFFF">
        <router-link to="/about" style="text-decoration: none; color: inherit;" >
          Login
        </router-link>
        /
        <router-link to="/about" style="text-decoration: none; color: inherit;" >
          Register
        </router-link>
      </b>
    </div>
    
</template>


<script lang="ts" setup>
    import { onMounted, ref } from 'vue'
    import { Search } from '@element-plus/icons-vue'
    const select = ref('')
    const state = ref('')
    
    interface LinkItem {
      value: string
      link: string
    }
    
    const links = ref<LinkItem[]>([])
    
    const loadAll = () => {
      return [
        { value: 'vue', link: 'https://github.com/vuejs/vue' },
        { value: 'element', link: 'https://github.com/ElemeFE/element' },
        { value: 'cooking', link: 'https://github.com/ElemeFE/cooking' },
        { value: 'mint-ui', link: 'https://github.com/ElemeFE/mint-ui' },
        { value: 'vuex', link: 'https://github.com/vuejs/vuex' },
        { value: 'vue-router', link: 'https://github.com/vuejs/vue-router' },
        { value: 'babel', link: 'https://github.com/babel/babel' },
      ]
    }
    
    let timeout: NodeJS.Timeout
    // let timeout: Window.Timeout
    const querySearchAsync = (queryString: string, cb: (arg: any) => void) => {
      const results = queryString
        ? links.value.filter(createFilter(queryString))
        : links.value
    
      clearTimeout(timeout)
      timeout = setTimeout(() => {
        cb(results)
      }, 3000 * Math.random())
    }
    const createFilter = (queryString: string) => {
      return (restaurant: LinkItem) => {
        return (
          restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        )
      }
    }
    
    const handleSelect = (item: LinkItem) => {
      console.log(item)
    }
    
    onMounted(() => {
      links.value = loadAll()
    })
    </script>

  <style scoped>
  .affix-container {
    text-align: center;
    height: 60px;
    border-radius: 0px;
    /* background: var(--el-color-primary-light-9); */
    background-color: rgba(0,0,0,0.2);
  }
  b{
    padding-left: 70%;
  }
  </style>