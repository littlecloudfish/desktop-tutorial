<template>
  <Form :validation-schema="schema" @submit="onSubmit">
    <el-row>
          <el-col style="color:white" :span="24">Input Username</el-col>
    </el-row>
    <Field name="username" type="username" />
    <ErrorMessage name="username" />
    <el-row>
          <el-col style="color:white" :span="24">Input Password</el-col>
    </el-row>
    <Field name="passwordConfirmation" type="password" />
    <ErrorMessage name="passwordConfirmation" />
    <el-row>
    <button>Submit</button>
    </el-row>

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
  username: yup.string().required('Please Enter Your username'),
  passwordConfirmation: yup.string().required('Please Enter Your Password')  

});


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
        router.push({name:'MusicHome'})
      }
    },
  })
  // alert(JSON.stringify(values.name, null, 2),'1aA@aaaaaaaa');
}
</script>


  <style scoped lang="scss">
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