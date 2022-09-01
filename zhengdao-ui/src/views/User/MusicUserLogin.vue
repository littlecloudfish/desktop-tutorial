<template>
  <el-row>
    <el-col :span="24">Input Username<div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
        <el-input v-model="input" placeholder="Please input" />
    <div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">Input Password<div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>
  <el-row>
    <el-col :span="24">
        <el-input v-model="input" placeholder="Please input" />
    <div class="grid-content ep-bg-purple-dark" /></el-col>
  </el-row>

  <el-row>
    <el-col :span="12">Forget Password<div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="12">Yes<div class="grid-content ep-bg-purple-light" /></el-col>
  </el-row>

</template>

<script>
export default{
  data(){
    return{
      username: '',
      validusername:true,
      password:'',
      secondpassword:'',
      validpassword:true,
      isloading:false,
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
  min-height: 36px;
}
</style>