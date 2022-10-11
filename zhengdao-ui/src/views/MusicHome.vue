<template>
  <div class="common-layout">
    <el-container>
      <el-header>
            <webhead></webhead> 
            <picturepost></picturepost>
      </el-header>
      <el-main>
        <el-container>
          <el-aside >
            <sidenavi></sidenavi>
          </el-aside>
          <el-main class="inside-main"> 
            <div>
              <div v-if="dataready">
                <display-music :posts="posts"></display-music>
              </div>
                <displayplayer></displayplayer> 
            </div>
          </el-main>
        </el-container>
      </el-main>
      <bfooter>

      </bfooter>
    </el-container>
  </div>
</template>

<!-- <template>
    <div class="common-layout">
    <el-container>
      <el-aside >
        <sidenavi></sidenavi>

      </el-aside>
      <el-main>
        <div>
            <webhead></webhead>
            <picturepost></picturepost>
            <display-music :posts="posts"></display-music>
            <displayplayer></displayplayer>
        </div>
      </el-main>
    </el-container>
    <el-backtop :right="100" :bottom="100" />
  </div>
    
</template> -->
<script>
import displayplayer from '../components/layout/displayplayer.vue';
import picturepost from '../components/layout/picturepost.vue';
import sidenavi from '../components/layout/sidenavi.vue';
import webhead from '../components/layout/webhead.vue';
import bfooter from '../components/layout/bottomfooter.vue';

export default ({
    components:{
        displayplayer,
        picturepost,
        sidenavi,
        webhead,
        bfooter,
    },

    setup() {
        
    },
    data() {
        return{
            // posts:[
            //         {
            //             "cover_address": "/demopicture/example.png",
            //             "id": 1,
            //             "music_address": "/DEMOMUSIC/crimanal.mp3",
            //             "name": "crimanal",
            //             "post_date": "2022-08-17T20:13:19",
            //             "user_id": 1
            //         },
            //         {
            //             "cover_address": "/demopicture/example.png",
            //             "id": 2,
            //             "music_address": "/DEMOMUSIC/crimanal.mp3",
            //             "name": "dangerous",
            //             "post_date": "2022-08-17T20:13:19",
            //             "user_id": 2
            //         },]
              posts: null,
              dataready:false
            
        }
    },
    async beforeCreate(){
        this.$store.dispatch('music/musiclistinfo').then(() => {
            this.posts = this.$store.getters['music/listofMusic'];
            this.dataready = true;
        })
    },
})


</script>
<style scoped>
.el-aside{
  background-color: #0b1c2c;
}
.el-main{
  background-color: #0b1c2c;
  padding-right:150px;
  padding-left:150px;
}
.el-main.inside-main{
  padding-left:0px;
  padding-right:50px;
}
.el-header{
  background-color: #0b1c2c;
}
.el-header{
  height:600px;
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