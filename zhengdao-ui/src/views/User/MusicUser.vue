<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        Aside

      </el-aside>
      <el-main>
        <display-music :posts="posts"></display-music>
      </el-main>
    </el-container>
  </div>
</template>
<script>
  import axios from 'axios'

  // "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzAwOTYxNywianRpIjoiODFlMzNhNjMtMjA5NS00MzhjLTk1ZWQtYzBkNzYyM2U4ZDI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTcsIm5iZiI6MTY2MzAwOTYxNywiY3NyZiI6IjY2ZmY0MjBhLWIwMTctNGYwNy05ODJhLTk4MzZlY2QwZDIxMCIsImV4cCI6MTY2MzAxMDUxN30.YNVzQK6PfGqUbZgGnR-D70aIeBPipiPBMQKb-46ttME"

  export default({
      
      setup() {

        const accesstoken =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MjkxMTU4NCwianRpIjoiNWRkOWE3ZGMtMzQyNi00YzRjLTkxODMtNmQ5ZTM1N2IwY2IwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTcsIm5iZiI6MTY2MjkxMTU4NCwiY3NyZiI6Ijg3MjlhZTY0LTBlYzEtNGRlMC1hZWYxLWZjZWE4NGI4OWRjNSIsImV4cCI6MTY2MjkxMjQ4NH0.yWYrtCNJbQ92b_s3xXSd5Gm78st9sa2R77zSUpB-YdE";
        const apiUrl = 'http://127.0.0.1:1943';
        axios.get(apiUrl+'/protected',{ headers:{"Authorization" : 'Bearer ${accesstoken}'}})
            .then(res => {
              console.log(res);
            })
            .catch(error)

  //       const authAxios = axios.create({
  //       baseURL: apiUrl,
  //       headers: {
  //         Authorization: 'Bearer ${eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9}' 
  //       },
  // })
  //       authAxios.get('/protected');

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
      beforecreated(){
          
      }
      // computed:{
      //   userinfo(){
      //       return this.$store.getters;
      //   },
    // }
  })
  </script>
  

