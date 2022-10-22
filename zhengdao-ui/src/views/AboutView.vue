<template>
  <div class="hello">
    <h1>{{ count }}</h1>
  </div>
</template>


<script>
export default {
  name: "HelloWorld", 
  data() {
    return {
      shopNumber: 2
    }
  },
  computed: {
    count: function() {
      return 'The shop number is ' 
    }
  }
};
</script>