<template>
    <!-- <div class="about">
      <h1>Not Found</h1>
    </div> -->
    <div>
      {{ currentAudioName || audioList[0].name }}
      <audio-player
        ref="audioPlayer"
        :audio-list="audioList.map(elm => elm.url)"
        :before-play="handleBeforePlay"
        theme-color="#ffff"
      />
      <!-- {{this.TryList}} -->
    </div>
  
  </template>
  <script>
  export default {
    inject:['musicid'],
    data() {
      return {
        currentAudioName: '',
        // musicid: 5,
        audioList: [
          {
            name: 'audio1',
            url: "http://127.0.0.1:1943/enjoymusic/5"
          },
          {
            name: 'audio2',
            url: 'http://127.0.0.1:1943/enjoymusic/6'
          }
        ],
        TryList:null,
      }
    },
  
    methods: {
      // Something to do before playing
      handleBeforePlay(next) {
        // There are a few things you can do here...
        this.currentAudioName = this.audioList[this.$refs.audioPlayer.currentPlayIndex].name
  
        next() // Start playing
      }
    },
    // async setup(){
    //     await  this.$store.dispatch('music/musicinfo',this.musicid);
    //     console.log(this.$store.getters['music/listofmusicinfo'])
    //     this.TryList = this.$store.getters['music/listofmusicinfo'];
    // },
    async created(){
        await  this.$store.dispatch('music/musicinfo',this.musicid);
        console.log(this.$store.getters['music/listofmusicinfo']);
        this.TryList = this.$store.getters['music/listofmusicinfo'];
        // console.log(this.musicid)
        // console.log(...mapGetters(['MusicUserid',]))
      },
  }
  </script>