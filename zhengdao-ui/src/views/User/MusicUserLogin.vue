<template>
  <base-dialog :show="!!error" title="An error occurred" @close="handleError">
      <p>{{ error }}</p>
  </base-dialog>
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
      <el-button type="Success" round @click="submitresult" >Login</el-button>  
      <!-- <el-button type="Success" round @click="forgetpassword" >Forget Passwords</el-button> -->
    </el-row>
    <el-row>
      <el-button type="Success" round  ><a href="/MusicUserRegister">Signup</a></el-button>  
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
      mode: 'Login',
    };
  },
  computed:{
    // submitButtonCaption(){
    //   if(this.mode === 'Login'){
    //     return 'Login';
    //   }else {
    //     return 'Signup';
    //   }
    // },
  },
  methods:{
    async submitresult(){
        this.isloading = true;
        const actionPaylod = {
          username: this.username,
          password: this.password,
        };
        try{
          await this.$store.dispatch('login',actionPaylod);
          // if (this.mode === 'Login'){
          //   await this.$store.dispatch('login',actionPaylod);}
          // else{
            // await this.$store.dispatch('signup', actionPayload); redirect to signup 
          // }
        }catch(err){
          this.error = err.message || 'Failed to authenticate, try later';
        }
        // token if not null then change page
        if (this.$store.getters.Token != null ){
          this.$router.push({name: 'MusicUser'});
        }
        this.isloading= false;

  },
  handleError(){
    this.error = null;
  },
  // forgetpassword(){

  //   }
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
