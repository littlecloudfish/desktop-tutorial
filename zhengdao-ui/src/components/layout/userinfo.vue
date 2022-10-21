<template>
        <div>
          <p style = "color:beige">Music Name:</p>
          <p style = "color:beige; padding-bottom:3px;">{{ currentAudioName || audioList[0].name }}</p>
        </div>
    <!-- {{audioList[0].url}} -->
</template>
 <script> 
  import {useStore} from 'vuex'
  import {inject} from 'vue'
  import {computed} from 'vue'
  import {mapGetters} from 'vuex'
  export default {
    inject:['userid'],
    async setup (){
        const store = useStore()
        await store.dispatch('music/musicinfo', inject('useris'))
        const trylist = await store.getters['music/listofmusicinfo']
        
        return{
            trylist,
            audioList,

        }
    },
    data() {
      return {
        currentAudioName: '',
        
        otherList:[],
        dataready:false,
      }
    },
    methods: {
     
    },
    async beforeUpdate(){
        this.otherList = audioList;
      },
    
  }
  </script>

  <style scoped>
 
  </style>