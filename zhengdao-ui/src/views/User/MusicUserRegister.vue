<template>
  <h2>Register an account </h2>
  <form >
    <div class="form-control">
      <el-row>
        <el-col :span="24">Input Username<div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="20">
            <el-input v-model.trim="username" placeholder="Please input Username" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <p v-if="!validusername">Username cannot be empty or start with space </p>

    </div>
    <div class="form-control">
      <el-row>
        <el-col :span="24">Input Password<div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="20">
            <el-input v-model="password" placeholder="Please input Password" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
    </div>
    <div class="form-control">
      <el-row>
        <el-col :span="24">Input Password Again<div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="20">
            <el-input v-model="secondpassword" placeholder="Please input Password Again" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <p v-if="!validpassword">One or more input fields are invalid. Please check your provided data.</p>
    </div>
    <div class="form-control">
      <el-row>
        <el-col :span="24">Input Email<div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="20">
            <el-input v-model="email" placeholder="Please input Email" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <p v-if="!validemail">Must be valid Email Address</p>

    </div>
    <div class="form-control">
      <el-row>
        <el-col :span="20">Input discord ID with #<div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <el-row>
        <el-col :span="20">
            <el-input v-model="discordId" placeholder="Please input discord ID with #" />
        <div class="grid-content ep-bg-purple-dark" /></el-col>
      </el-row>
      <p v-if="!validediscord">Must be DiscordID with #</p>

    </div>
    <div>
      <el-row>
        <el-button type="Success" round @click="submitresult" >Submit</el-button>  
      </el-row>
    </div>
  </form>
</template>



<script>
// import axios from 'axios'

export default{
  data(){
    return{
      username: '',
      validusername:true,
      password:'',
      secondpassword:'',
      validpassword:true,
      email:'',
      validemail:true,
      discordId:'',
      validediscord:true,
      error: null,
    };
  },
  methods:{
    submitresult(){
      if(this.secondpassword !==this.password ){
        this.validpassword = false;
        return;
      }
      this.validpassword = true;
      // console.log(this.validpassword)
      // console.log(this.password)
      // console.log(this.secondpassword)

      if(this.mode === 'login'){
        
      }else{
        this.$store.dispatch('signup',{
          username: this.username,
          password: this.password,
        });
      }
    
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
  min-height: 12px;
}
</style>