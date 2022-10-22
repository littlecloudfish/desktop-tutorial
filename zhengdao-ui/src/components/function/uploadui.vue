<template>
    <h2>Upload Music</h2>
    <form>
      <div>
        <el-row>
          <el-col :span="24">Input Music Name</el-col>
        
          <el-col :span="20">
              <el-input v-model.trim="musicname" placeholder="Please input Music Name" />
          </el-col>
        </el-row>
      </div>
      <!-- <div>
        <el-row>
          <el-col :span="24">Input Music Link</el-col>
          <el-col :span="20">
              <el-input v-model="musiclink" placeholder="Please input Music Link" />
          </el-col>
        </el-row>
      </div>  -->
         <!-- <el-row>
          <el-col :span="24">Input Music Performers(DiscordId)</el-col>
          <el-col :span="24">
              <el-input v-model="musicperformer" placeholder="Please input Performers" />
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">Input Music Composer(DiscordId)</el-col>
          <el-col :span="24">
              <el-input v-model="input" placeholder="Please input Composer" />
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">Input Music Editor(DiscordId)</el-col>
          <el-col :span="24">
              <el-input v-model="input" placeholder="Please input Editor" />
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">Input Music Songwriter(DiscordId)</el-col>
          <el-col :span="24">
              <el-input v-model="input" placeholder="Please input Songwriter" />
          </el-col>
          <el-col :span="24">Input Music Producer(DiscordId)</el-col>
          <el-col :span="24">
              <el-input v-model="input" placeholder="Please input Producer" />
          </el-col>
        </el-row> -->
       <div>
        <el-row>
          <el-col :span="24">Input Music Release Date</el-col>
          <!-- <el-col :span="20">
              <el-input v-model="releasedate" placeholder="Please input" />
          </el-col> -->
        <div class="demo-date-picker">
          <div class="block">
            <el-date-picker
              v-model="value1"
              type="date"
              placeholder="Pick a day"
              size="large"
              format="YYYY/MM/DD"
              value-format="YYYY-MM-DD"
            />
          </div>
        </div>
        </el-row>
      </div>
      <div>
        <el-row>
          <el-col :span="24">Input Music Lyrics</el-col>
          <el-col :span="20">
            <el-input v-model="musiclyrics" 
              :autosize="{ minRows: 5, maxRows: 100 }"
              placeholder="Please Input Lyrics"
              type="textarea"
               />
          </el-col>
        </el-row>
      </div>
      <div>
        <el-row>
          <el-col :span="24">Input Music Cover Picture</el-col>
          <input type="file"  @change="onFileSelected">
        </el-row>
        <el-row>
          <el-col :span="24">Input Music Mp3 file</el-col>
          <input type="file" @change="onMusicFileSelected">
        </el-row>
      </div>
      <div>
        <el-row>
          <el-button type="primary" round @click="submitresult" >Submit</el-button>  
        </el-row>
      </div>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default{
    data(){
      return{
        musicname: '',
        validmusicname:true,
        musiclink:'',
        validmusiclink:true,
        musiclyrics:'',
        validelyrics:true,
        musicperformer:'',
        validmusicperformer:true,
        releasedate:'',
        error: null,
        value1: null,
      };
    },
    methods:{
      // async submitresult(){
      //   const fd = new FormData();
      //   fd.append('pic', this.selectedFile, this.selectedFile.name)
      //   fd.append('mp3', this.musicfile, this.musicfile.name)
      //   try{
      //     await this.$store.dispatch('request/uploadmusic',fd);
      //   }catch(err){
      //     this.error = err.message || "Fail to enter try again";
      //   };
      async submitresult(){
        console.log(this.musiclyrics)
        //   const fd = new FormData();
        //   fd.append('pic', this.selectedFile, this.selectedFile.name)
        //   fd.append('mp3', this.musicfile, this.musicfile.name)
        //   fd.append('musicname',this.musicname)
        //   fd.append('releasedate',this.value1)
        //   try{
        //     await this.$store.dispatch('request/uploadmusic',fd);
        //   }catch(err){
        //     this.error = err.message || "Fail to enter try again";
        //   }
      },
      onFileSelected(event){
              this.selectedFile = event.target.files[0]
          },
      onMusicFileSelected(event){
          this.musicfile = event.target.files[0]  //not sure 0 or 1
      },
  
      },
  
  };
  </script>
  
  <style lang="scss">
  .el-row {
    margin-bottom: 3px;
  }
  .el-row:last-child {
    margin-bottom: 0;
  }
  .el-col {
    color:bisque ;
    padding-top: 0px;
    padding-bottom: 0px;;
  }
  .el-input{
    padding-bottom: 0px;
    padding-top:0px;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  </style>