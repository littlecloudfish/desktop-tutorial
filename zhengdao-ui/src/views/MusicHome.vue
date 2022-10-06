<template>
  <div class="common-layout">
    <el-container>
      <el-header>
            <webhead>
              
            </webhead> 
            <picturepost></picturepost>
      </el-header>
      <el-main>
        <el-container>
          <el-aside >
            <sidenavi></sidenavi>
          </el-aside>
          <el-main>
            <div>
                <display-music :posts="posts"></display-music>
                <displayplayer></displayplayer>
            </div>
          </el-main>
        </el-container>
      </el-main>
      <el-footer>Footer create mode 100644 zhengdao-ui/node_modules/.cache/babel-loader/f6e4bce43e6d9099b737ca918452a5dc.json</el-footer>
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

export default ({
    components:{
        displayplayer,
        picturepost,
        sidenavi,
        webhead,
    },

    setup() {
        
    },
    data() {
        return{
            posts:[
                    {
                        "cover_address": "/demopicture/example.png",
                        "id": 1,
                        "music_address": "/DEMOMUSIC/crimanal.mp3",
                        "name": "crimanal",
                        "post_date": "2022-08-17T20:13:19",
                        "user_id": 1
                    },
                    {
                        "cover_address": "/demopicture/example.png",
                        "id": 2,
                        "music_address": "/DEMOMUSIC/crimanal.mp3",
                        "name": "dangerous",
                        "post_date": "2022-08-17T20:13:19",
                        "user_id": 2
                    },]

            
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

}
.el-header{
  height:600px;
}

</style>