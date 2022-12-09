<template>
    <!-- <div class="about">
      <h1>Not Found</h1>
    </div> -->
        <div>
          <p style = "color:beige">Music Name:</p>
          <p style = "color:beige; padding-bottom:3px;">{{ currentAudioName || audioList[0].name }}</p>
          <audio-player
              ref="audioPlayer"
              :audio-list="this.audioList.map(elm => elm.url)"
              theme-color="#ffff"
          />
        </div>
    <!-- {{audioList[0].url}} -->
</template>
 <script> 
  import {useStore} from 'vuex'
  import {inject} from 'vue'
  import {computed} from 'vue'
  import {mapGetters} from 'vuex'
  export default {
    inject:['musicid'],
    async setup (){
        const store = useStore()
        await store.dispatch('music/musicinfo', inject('musicid'))
        const trylist = await store.getters['music/listofmusicinfo']
        const audioList = [{
            name:trylist[0].name,
            url:'http://127.0.0.1:1943/enjoymusic/'+trylist[0].id
        },
        {
            name:'hello',
            url:'http://127.0.0.1:1943/enjoymusic/6'
        }
    ]
        // useStore().dispatch('music/musicinfo', inject('musicid')).then(
        // useStore().getters['music/listofmusicinfo']
        // )

        // useStore().dispatch('music/musicinfo', inject('musicid')).then(
        //  computed(()=> useStore().getters['music/listofmusicinfo'])
            // useStore().getters['music/listofmusicinfo']
        // )
        
        // console.log( useStore().getters('music/listofmusicinfo'))
        // console.log(useStore().getters[music/listofmusicinfo])
        return{
            trylist,
            audioList,
            // trylist: useStore().getters['music/listofmusicinfo']
            // trylist:[inject('musicid')]
            // return{
            // trylist: computed(()=>store.getters['music/listofmusicinfo'])
        // }
        }
    },
    data() {
      return {
        currentAudioName: '',
        // audioList: [
        //   {
        //     name: 'test',
        //     url: "test"
        //   },
        // ],
        // audioList:[],
        // TryList:null,
        // audioList: thisisthelist,
        
        otherList:[],
        dataready:false,
      }
    },
    // beforeRouteEnter(to, from,next){
    //     next(vm=>vm.setData())
    // },
    methods: {
      handleBeforePlay(next) {
        //There are a few things you can do here...
        this.currentAudioName = this.otherList[this.$refs.audioPlayer.currentPlayIndex].name
        next() 
      },
    //   async setData(){
    //     console.log('callsetdate')
    //     await  this.$store.dispatch('music/musicinfo',this.musicid);
    //     this.TryList = await this.$store.getters['music/listofmusicinfo'];
    //   }
    },
    
    async beforeUpdate(){
        this.otherList = audioList;
        // console.log('injected data '+this.trylist);
        // await  this.$store.dispatch('music/musicinfo',this.musicid);
        // console.log(this.$store.getters['music/listofmusicinfo']);
        // this.TryList = await this.$store.getters['music/listofmusicinfo'];
        // this.audioList[0] =  {
        //     name:this.TryList[0].name,
        //     url:'http://127.0.0.1:1943/enjoymusic/'+this.TryList[0].id ,
        // };
        // console.log(this.musicid)
        // console.log(...mapGetters(['MusicUserid',]))
      },
    
  }
  </script>

  <style scoped>
 
  </style>