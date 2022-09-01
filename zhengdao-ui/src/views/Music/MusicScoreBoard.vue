<template>
  <p v-if="isLoading">Loading...</p>
    <!-- <h2>{{ post[1][id] }} - {{ post[1][title] }}</h2>
    <p>{{ post[1][body] }}</p> -->

<div v-for="p in post" :key="p.id">
    <h2>{{ p.id }} - {{ p.title }}</h2>
    <p>{{ p.body }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: [],
      isLoading: false
    }
  },
  methods: {
    getPosts() {
      this.isLoading = true

      fetch('https://jsonplaceholder.typicode.com/posts/')
        .then(response => response.json())
        .then(data => {
          this.post = data
          this.isLoading = false
        })
    }
  },
  mounted() {
    this.getPosts()
  }
}
</script>



<!-- <template>
  <div id="app">
  <Posts  />
  </div>
</template>
<script>
import Posts from '../components/Posts.vue'
export default {
  name: 'App',
  components: {
    Posts
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->