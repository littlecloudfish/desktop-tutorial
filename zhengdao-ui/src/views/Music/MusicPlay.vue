<template>
    <div class="common-layout">
      <el-container>
        <el-header>
              <webhead></webhead> 
        </el-header>
        <el-main>
          <el-container>
            <el-aside >
              <sidenavi></sidenavi>
            </el-aside>
            <el-main class="inside-main"> 
              <el-row>
                <!-- <play-music ></play-music> -->
                <el-col :span="120">
                    <el-image style="width: 100px; height: 100px" src="https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg" fit="fill" />
                </el-col>
                <el-col :span="12">
                    <suspense timeout="100">
                        <musicaudio></musicaudio>
                    </suspense>
                </el-col>
              </el-row>
              <el-row>
                  <el-col :span="120">
                    <showmusicinfo></showmusicinfo>
                  </el-col>
                  <el-col :span="12">
                    <showlyris></showlyris>
                  </el-col>
              </el-row>
            </el-main>
          </el-container>
        </el-main>
        <bfooter>
  
        </bfooter>
      </el-container>
    </div>
  </template>
  <script>
  import sidenavi from '../../components/layout/sidenavi.vue';
  import webhead from '../../components/layout/webhead.vue';
  import bfooter from '../../components/layout/bottomfooter.vue';
  import musicaudio from '../../components/function/musicaudio.vue';
  import showmusicinfo from '../../components/function/showmusicinfo.vue'
  import showlyris from '../../components/function/showlyris.vue'

  export default ({
      components:{
          sidenavi,
          webhead,
          bfooter,
          musicaudio,
          showmusicinfo,
          showlyris
      },
  
      setup() {
          
      },
      data() {
          return{
                posts: null,
                dataready:false,
                tryList:null,
          }
      },
    //   beforeRouteEnter(to, from, next){
    //     next(vm=>vm.setData())
    //   },
      methods:{
        // setData(){
        //     this.$store.dispatch('music/musicinfo',this.$route.params.id).then(() => {
        //       this.tryList = this.$store.getters['music/listofmusicinfo'];
        //       console.log(this.tryList)
        //       this.dataready = true;
        //   });
        // }
      },
      async beforeCreate(){
        //   this.$store.dispatch('music/musiclistinfo').then(() => {
        //       this.posts = this.$store.getters['music/listofMusic'];
        //       this.dataready = true;
        //   });
        //   this.$store.dispatch('music/musicinfo',this.$route.params.id).then(() => {
        //       this.tryList = this.$store.getters['music/listofmusicinfo'];
        //       console.log(this.tryList)
        //       this.dataready = true;
        //   });

      },
      provide(){
        return{
            musicid: this.$route.params.id,
            // trylist: this.tryList,
        }
    },
  })
  

  </script>
  <style scoped>
  .el-aside{
    background-color: #0b1c2c;
  }
  .el-main{
    background-color: #0b1c2c;
    padding-right:50px;
    padding-left:50px;
    padding-block-start: 0px;
  }
  .el-main.inside-main{
    padding-left:20px;
    padding-right:150px;
  }
  .el-header{
    background-color: #0b1c2c;
  }
  .el-header{
    height:60px;
    padding-left: 0px;
    padding-right: 0px;
  }
   
  .common-layout{
    margin-bottom: 0px;
  }
  
  .scrollbar-demo-item {
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 150px;
      height: 150px;
      margin: 0px;
      text-align: center;
      border-radius: 4px;
      background: "0b1c2c"; /* change to 1  */
      color: var(--el-color-danger);
    }
  
  </style>

