<template>
  <el-row>
    <el-col :span="24">Input Username<div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
        <el-input v-model="username" placeholder="Please input Username" />
    <div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">Input Password<div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
        <el-input v-model="password" placeholder="Please input Password" />
    <div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <p v-if="!validpassword">Username or Password are invalid. Please check your provided data.</p>

  <div>
    <el-row>
      <el-button type="Success" round @click="forgetpassword" >Forget Passwords</el-button>  
    </el-row> 
    <el-row>
      <el-button type="Success" round @click="submitresult" >Login</el-button>  
    </el-row>
  </div>
</template>

<script>
export default{
  data(){
    return{
      username: '',
      validusername:true,
      password:'',
      validpassword:true,
      isloading:false,
      error: null,
    };
  },
  methods:{
    submitresult(){
      

      // if(this.mode === 'login'){
        
      // }else{
      //   this.$store.dispatch('signup',{
      //     username: this.username,
      //     password: this.password,
      //   });
      // }
        this.$store.dispatch('login',{
          username: this.username,
          password: this.password,
        });
  },
    forgetpassword(){

    }
  },
}
</script>

<style lang="scss">
.el-row {
  margin-bottom: 20px;
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
