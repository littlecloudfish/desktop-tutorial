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
              <el-row class="titleofpage">
                <el-icon><Headset /></el-icon>
                Music Play
              </el-row>
              <el-row class="audioborder">
                <!-- <play-music ></play-music> -->
                <el-col :span="200" >
                    <el-image style="width: 150px; height: 150px" src="https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg" fit="fill" />
                </el-col>
                <el-col :span="12">
                    <suspense timeout="100">
                        <musicaudio class="audiobar"></musicaudio>
                    </suspense>
                </el-col>
              </el-row>
              <el-row>
                  <el-col :span=200>
                    <suspense timeout="100">
                      <showmusicinfo></showmusicinfo>
                    </suspense>
                    <ratemusic></ratemusic>
                  </el-col>
                  <el-col :span="12">
                    <suspense timeout="100">
                      <showlyris></showlyris>
                    </suspense>
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
  import ratemusic from '../../components/function/ratemusic.vue'

  export default ({
      components:{
          sidenavi,
          webhead,
          bfooter,
          musicaudio,
          showmusicinfo,
          showlyris,
          ratemusic
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
  .titleofpage{
    color:beige;
    padding-top:1%;
    padding-bottom:1%;
  }
  .el-icon{
    color:deeppink;
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
  .audioborder{
    border-radius: 18px;
    padding-bottom: 3%;
    background:#0f2743;
  } 
  .audiobar{
    padding-left:50px;
    padding-top:3%;
  }
  .el-image{
    padding-top:20%;
    padding-left:10%;
  }
  </style>

