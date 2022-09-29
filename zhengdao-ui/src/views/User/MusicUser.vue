<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        Aside

      </el-aside>
      <el-main>
        <el-button type="Success" round @click="getaccesstoken" >Login</el-button> 
        <!-- <display-music :posts="posts"></display-music> -->
      </el-main>
    </el-container>
  </div>
</template>
<script>
// import { onBeforeMount } from '@vue/runtime-core';
// import axios from 'axios'


  export default({
      
      setup() {

        
          
          },
      methods:{
        getaccesstoken(){
          // this.$store.dispatch('userInfo/registeruser');

         }
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
      created(){
        // this.$store.dispatch('userInfo/registeruser');
        this.$store.dispatch('request/fetchRequests')


      },
      beforeMount(){
        // this.$store.dispatch('userInfo/registeruser');
      }
      // computed:{
      //   userinfo(){
      //       return this.$store.getters;
      //   },
    // }
  })
  </script>
  

