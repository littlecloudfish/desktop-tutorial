<template>
<div>
    <webhead></webhead>
    <RouterView/>
</div>

</template>
    
  <script>
  import webhead from '../../components/layout/webhead.vue';
  
  export default({
    components:{
          webhead
    }
  })
  </script>
  