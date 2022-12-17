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
    <el-row>
        <el-col style="color:white" :span="24">Input Music Cover Picture</el-col>
    </el-row>
    
    <div>
        <DropZone class="drop-area" @files-dropped="addFiles" #default="{ dropZoneActive }">
            <label for="file-input">
                <span v-if="dropZoneActive">
                    <span>Drop Them Here</span>
                    <span class="smaller">to add them</span>
                </span>
                <span v-else>
                    <span>Drag Your Files Here</span>
                    <span class="smaller">
                        or <strong><em>click here</em></strong> to select files
                    </span>
                </span>

                <input type="file" id="file-input" multiple @change="onInputChange" />
            </label>
            <ul class="image-list" v-show="files.length">
                <FilePreview v-for="file of files" :key="file.id" :file="file" tag="li" @remove="removeFiles" />
            </ul>
        </DropZone>
    <button @click.prevent="uploadFiles(files)" class="upload-button">Upload Picture</button>
    </div>    
  </Form>
</template>
<script lang="ts" setup>
import { Field, Form, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import YupPassword from 'yup-password';
import { ElMessage, ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import DropZone from './DropZone.vue';
import useFileList from '../../compositions/file-list';
import createUploader from '../../compositions/file-uploader'

import router from '@/router';
YupPassword(yup)

const {files, addFiles, removeFiles} = useFileList()
function onInputChange(e) {
	addFiles(e.target.files)
	e.target.value = null // reset so that selecting the same file again will still cause it to fire this change
}
const { uploadFiles } = createUploader('YOUR URL HERE')




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
<style scoped lang="stylus">

.drop-area {
	width: 100%;
	max-width: 800px;
	margin: 0 auto;
	padding: 50px;
	background: #ffffff55;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
	transition: .2s ease;
	&[data-active=true] {
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
		background: #ffffffcc;
	}
}
label {
	font-size: 36px;
	cursor: pointer;
	display: block;
	span {
		display: block;
	}
	input[type=file]:not(:focus-visible) {
		// Visually Hidden Styles taken from Bootstrap 5
		position: absolute !important;
		width: 1px !important;
		height: 1px !important;
		padding: 0 !important;
		margin: -1px !important;
		overflow: hidden !important;
		clip: rect(0, 0, 0, 0) !important;
		white-space: nowrap !important;
		border: 0 !important;
	}
	.smaller {
		font-size: 16px;
	}
}
.image-list {
	display: flex;
	list-style: none;
	flex-wrap: wrap;
	padding: 0;
}
.upload-button {
	display: block;
	appearance: none;
	border: 0;
	border-radius: 50px;
	padding: 0.75rem 3rem;
	margin: 1rem auto;
	font-size: 1.25rem;
	font-weight: bold;
	background: #369;
	color: #fff;
	text-transform: uppercase;
}
button {
	cursor: pointer;
}
</style>