<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <el-row>
          <el-col style="color:white" :span="24">Input Account Email</el-col>
    </el-row>
    <Field name="email" type="email" />
    <ErrorMessage name="email" />
    <el-row>
          <el-col style="color:white" :span="24">Input Account Name</el-col>
    </el-row>
    <Field name="name" />
    <ErrorMessage name="name" />
    <el-row>
          <el-col style="color:white" :span="24">Input Account Password(Password must at least 8 characters, and contains lowercase letter,uppercase letter,number and symbol)</el-col>
    </el-row>
    <Field name="password" />
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="password" />
    <el-row>
          <el-col style="color:white" :span="24">Input Account Password Again</el-col>
    </el-row>
    <Field name="passwordConfirmation" type="password" />
    <ErrorMessage name="passwordConfirmation" />
    <button>Submit</button>
    <el-button text @click="open">Click to open the Message Box</el-button>

  </Form>
</template>
<!-- 1aA@aaaaaaaa -->
<script lang="ts" setup>
import { Field, Form, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import YupPassword from 'yup-password';
import { ElMessage, ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import router from '@/router';
YupPassword(yup)


const schema = yup.object().shape({
  email: yup.string().email().required('Please Enter Your Email'),
  name: yup.string().required('Please Enter Your Name'),
  password: yup.string().password(),
  // password: yup.string().password(),
  passwordConfirmation: yup.string().oneOf([yup.ref('password'), null], 'Passwords must match')  

});

//try successful button 
const open = () => {
  ElMessageBox.alert('This is a message', 'Title', {
    // if you want to disable its autofocus
    // autofocus: false,
    confirmButtonText: 'Login',
    callback: (action: Action) => {
      if (action === 'confirm'){
        router.push({name:'MusicUserLogin'})

      }
    },
  })
};
// const passwordField = document.querySelector('#password')

// function switchVisibility() {
//   if (passwordField.getAttribute('type') === 'password') passwordField.setAttribute('type', 'text')
//   else passwordField.setAttribute('type', 'password')
// }
function onSubmit(values) {
  ElMessageBox.alert(values.name, 'Successfully Sign Up', {
    // if you want to disable its autofocus
    // autofocus: false,
    
    callback: (action: Action) => {
      // ElMessage({
      //   type: 'info',
      //   message: `action: ${action}`,
      // })
      if (action === 'confirm'){

      }
    },
  })
  // alert(JSON.stringify(values.name, null, 2),'1aA@aaaaaaaa');
}
</script>

<!-- <template>
    <h2 style="color:white">Register an account </h2>
    <form >
      <div class="form-control">
        <el-row>
          <el-col style="color:white" :span="24">Input Username</el-col>
        </el-row>
        <el-row>
          <el-col :span="20">
              <el-input v-model.trim="username" placeholder="Please input Username" />
          </el-col>
        </el-row>
        <p v-if="!validusername">Username cannot be empty or start with space </p>
      </div>
      <div class="form-control">
        <el-row>
          <el-col style="color:white" :span="24">Input Password</el-col>
        </el-row>
        <el-row>
          <el-col :span="20">
              <el-input v-model="password" placeholder="Please input Password" />
          </el-col>
        </el-row>
      </div>
      <div class="form-control">
        <el-row>
          <el-col style="color:white" :span="24">Input Password Again</el-col>
        </el-row>
        <el-row>
          <el-col :span="20">
              <el-input v-model="secondpassword" placeholder="Please input Password Again" />
          </el-col>
        </el-row>
        <p v-if="!validpassword">One or more input fields are invalid. Please check your provided data.</p>
      </div>
      <div class="form-control">
        <el-row>
          <el-col style="color:white" :span="24">Input Email</el-col>
        </el-row>
        <el-row>
          <el-col :span="20">
              <el-input v-model="email" placeholder="Please input Email" />
          </el-col>
        </el-row>
        <p v-if="!validemail">Must be valid Email Address</p>
  
      </div>
      <div class="form-control">
        <el-row>
          <el-col style="color:white" :span="20">Input discord ID with #</el-col>
        </el-row>
        <el-row>
          <el-col :span="20">
              <el-input v-model="discordId" placeholder="Please input discord ID with #" />
          </el-col>
        </el-row>
        <p v-if="!validediscord">Must be DiscordID with #</p>
  
      </div>
      <div>
        <el-row>
          <el-button type="Success" round @click="submitresult" >Submit</el-button>  
        </el-row>
      </div>
    </form>
  </template> -->
  
  
<!--   
  <script>
  // import axios from 'axios'
  import imageCompressor from 'vue-image-compressor';

  export default{
    components: { imageCompressor },

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
      
    },
   
    }

  }
  </script>
   -->
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