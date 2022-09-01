<template>
  <div></div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      formData: {
        userId: '1',
        title:  'Article title',
        body:   'Article body content'
      },
      url:'https://jsonplaceholder.typicode.com/posts',
    }
  },
  mounted() {
    axios
      .post(this.url, this.formData)
      .then((response) => console.log(response))
  }
}
</script>