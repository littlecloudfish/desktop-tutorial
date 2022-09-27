<template>
    <div class="common-layout">
    <el-container>
      <el-aside >
        <sidenavi></sidenavi>

      </el-aside>
      <el-main>
        <div>
            <picturepost></picturepost>
            <display-music :posts="posts"></display-music>
            <displayplayer></displayplayer>
        </div>
      </el-main>
    </el-container>
    <el-backtop :right="100" :bottom="100" />
  </div>
    
</template>
<script>
import displayplayer from '../components/layout/displayplayer.vue';
import picturepost from '../components/layout/picturepost.vue';
import sidenavi from '../components/layout/sidenavi.vue';


export default ({
    components:{
        displayplayer,
        picturepost,
        sidenavi,
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
