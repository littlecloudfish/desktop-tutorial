<template>
  <h2>Upload Music</h2>
  <form>
    <div>
      <el-row>
        <el-col :span="24">Input Music Name<div class="grid-content ep-bg-purple-dark" /></el-col>
      
        <el-col :span="20">
            <el-input v-model="musicname" placeholder="Please input Music Name" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
    </div>
    <div>
      <el-row>
        <el-col :span="24">Input Music Link<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="20">
            <el-input v-model="musiclink" placeholder="Please input Music Link" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
    </div> 
       <!-- <el-row>
        <el-col :span="24">Input Music Performers(DiscordId)<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">
            <el-input v-model="musicperformer" placeholder="Please input Performers" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="24">Input Music Composer(DiscordId)<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">
            <el-input v-model="input" placeholder="Please input Composer" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="24">Input Music Editor(DiscordId)<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">
            <el-input v-model="input" placeholder="Please input Editor" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="24">Input Music Songwriter(DiscordId)<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">
            <el-input v-model="input" placeholder="Please input Songwriter" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">Input Music Producer(DiscordId)<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="24">
            <el-input v-model="input" placeholder="Please input Producer" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row> -->
     <div>
      <el-row>
        <el-col :span="24">Input Music Release Date<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="20">
            <el-input v-model="releasedate" placeholder="Please input" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
    </div>
    <div>
      <el-row>
        <el-col :span="24">Input Music Lyrics<div class="grid-content ep-bg-purple-dark" /></el-col>
        <el-col :span="20">
            <el-input v-model="musiclyrics" placeholder="Please Input Lyrics" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>

    </div>
    <div>
      <el-row>
        <el-col :span="24">Input Music Cover Picture<div class="grid-content ep-bg-purple-dark" /></el-col>
        <input type="file"  @change="onFileSelected">
      </el-row>
      <el-row>
        <el-col :span="24">Input Music Mp3 file<div class="grid-content ep-bg-purple-dark" /></el-col>
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
        const fd = new FormData();
        fd.append('pic', this.selectedFile, this.selectedFile.name)
        fd.append('mp3', this.musicfile, this.musicfile.name)
        fd.append('musicname',this.musicname)
        try{
          await this.$store.dispatch('request/uploadmusicinfo',fd);
        }catch(err){
          this.error = err.message || "Fail to enter try again";
        }
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
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>