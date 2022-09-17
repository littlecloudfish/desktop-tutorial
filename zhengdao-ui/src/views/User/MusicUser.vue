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
import { onBeforeMount } from '@vue/runtime-core';
import axios from 'axios'


  export default({
      
      setup() {

        // success
        // const accesstoken =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzE2NTI4NywianRpIjoiNzQwN2YxY2MtNjcwMC00MjZjLTkxNzItZWZmMjZkYTUwOThmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTcsIm5iZiI6MTY2MzE2NTI4NywiY3NyZiI6ImY3Y2YwNzI4LWI0N2YtNDMzZi05YTFlLTY5NGRmNGQ3NTA5MiIsImV4cCI6MTY2MzE2NjE4N30.bz89011IOb2Kda3XoJDlz59NwHBUtCppXhnK2HRJdX8";
        // const apiUrl = 'http://127.0.0.1:1943';
        
        // axios.get('http://127.0.0.1:1943/who_am_i', {
        //   headers: {
        //       Accept: 'application/json',
        //       Authorization: `Bearer ${accesstoken}`
        //       }
        // })
        // .then((res) => {
        //   console.log(res.data)
        // })
        // .catch((error) => {
        //   console.error(error)
        // })
        // ;




        // axios.get(apiUrl+'/protected',{ headers:{"Authorization" : 'Bearer $accesstoken'}})
        //     .then(res => {
        //       console.log(res);
        //     })
        //     .catch(error)
        // const options = {
        // method: 'get',
        // headers: {
        //   Authorization: `Bearer ${accesstoken}`,
        //   }
        // };
        // const response = fetch('http://127.0.0.1:1943/who_am_i', options);
        // console.log(response.json())
  //       const authAxios = axios.create({
  //       baseURL: apiUrl,
  //       headers: {
  //         Authorization: 'Bearer ${eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9}' 
  //       },
  // })
  //       authAxios.get('/protected');
          
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
  

