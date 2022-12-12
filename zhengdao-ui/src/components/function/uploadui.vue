<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <el-row>
      <el-col :span="24">Input Music Name</el-col>
    </el-row>
    <Field name="musicname" type="musicname" />
    <ErrorMessage name="musicname" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Link</el-col>
    </el-row>
    <Field name="musiclink" />
    <ErrorMessage name="musiclink" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Performer</el-col>
    </el-row>
    <Field name="performers" />
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="performers" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Composer</el-col>
    </el-row>
    <Field name="Composer"  />
    <ErrorMessage name="Composer" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Editor</el-col>
    </el-row>
    <Field name="Editor" />
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="Editor" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Songwriter</el-col>
    </el-row>
    <Field name="Songwriter" />
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="Songwriter" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Producer</el-col>
    </el-row>
    <Field name="Producer" />
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="Producer" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Lyrics</el-col>
    </el-row>
    <Field name="Lyrics" type="text"/>
    <!-- <button onclick="switchVisibility()">show / hide</button> -->
    <ErrorMessage name="Lyrics" />
    <button>Submit</button>

  </Form>
</template>
<script lang="ts" setup>
import { Field, Form, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import YupPassword from 'yup-password';
import { ElMessage, ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import router from '@/router';
YupPassword(yup)


const schema = yup.object().shape({
  musicname: yup.string().required('Please Enter Your Music Name'),
  musiclink: yup.string().required('Please Enter Your Link'),
  performers: yup.string(),
  Composer:yup.string(),
  Editor:yup.string(),
  Songwriter:yup.string(),
  Producer:yup.string(),
  Lyrics:yup.string(),
});

//try successful button 
const open = () => {
  ElMessageBox.alert('This is a message', 'Title', {
    // if you want to disable its autofocus
    // autofocus: false,
    
    confirmButtonText: 'Login',
    // cancel-button-text:'oncemore',	
    cancelButtonText:'oncemore',
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
  ElMessageBox.alert(values.name, 'Successfully Uploaded', {
    // if you want to disable its autofocus
    // autofocus: false,
    confirmButtonText:'One More Song',
    cancelButtonText:'oncemore',
    callback: (action: Action) => {
      if (action === 'confirm'){
        router.push({name:'MusicHome'})
      }
    },
  })

}
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