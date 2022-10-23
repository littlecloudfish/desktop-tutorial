<template>

  <image-compressor
    :done="getFiles"
    :scale="scale"
    :quality="quality">
  </image-compressor>

</template>


<script>

  import imageCompressor from 'vue-image-compressor';

  export default {

    components: { imageCompressor },

    methods: {
      getFiles(obj){
        console.log(obj);
      }
    }
  };

</script>