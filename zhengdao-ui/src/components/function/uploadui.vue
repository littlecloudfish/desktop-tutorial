<template>
  <!-- <Form :validation-schema="schema" @submit.prevent="onSubmit"> -->
  <Form :validation-schema="schema" @submit="onSubmit">
    <el-row>
      <el-col :span="24">Input Music Name</el-col>
    </el-row>
    <Field name="musicname" type="musicname" />
    <ErrorMessage name="musicname" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Gettr Link</el-col>
    </el-row>
    <Field name="musiclink" />
    <ErrorMessage name="musiclink" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Performer</el-col>
    </el-row>
    <Field name="performers" />
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
    <ErrorMessage name="Editor" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Songwriter</el-col>
    </el-row>
    <Field name="Songwriter" />
    <ErrorMessage name="Songwriter" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Producer</el-col>
    </el-row>
    <Field name="Producer" />
    <ErrorMessage name="Producer" />
    <el-row>
          <el-col style="color:white" :span="24">Input Music Lyrics</el-col>
    </el-row>
    <Field name="Lyrics" type="text"/>
    <ErrorMessage name="Lyrics" />
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
                <FilePreview v-for="file of files" :key="file.id" :file="file" tag="li" @remove="(thefile)=>removeFile(thefile)" />
            </ul>
        </DropZone>
    <!-- <button @click.prevent="uploadFiles(files)" class="upload-button">Submit</button> -->
    </div>
    <div class="block">
      <span class="demonstration">
        <el-row>
          <el-col style="color:white" :span="24">Music Created Date</el-col>
        </el-row>
      </span>
      <el-date-picker
        v-model="createdate"
        type="date"
        placeholder="Pick a day"
        size="large"
      />
    </div>
    <button class="upload-button">Submit</button>
  </Form>
  <!-- <button @click.prevent="onSubmit(schema)" class="upload-button">Submit</button> -->
</template>
<script lang="ts" setup>
import { Field, Form, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
import { ref } from 'vue'
import { ElMessageBox } from 'element-plus';
import type { Action } from 'element-plus';
import DropZone from './DropZone.vue';
import useFileList from '../../compositions/file-list';
import router from '@/router';
import FilePreview from './FilePreview.vue';
import { useStore } from 'vuex';
const createdate = ref('')
const store = useStore()
const {files, addFiles, removeFile} = useFileList()
function onInputChange(e) {
	addFiles(e.target.files)
	e.target.value = null // reset so that selecting the same file again will still cause it to fire this change
}
const schema = yup.object().shape({
  musicname: yup.string().required('Please Enter Your Music Name'),
  musiclink: yup.string().required('Please Enter Your Link').matches(/gettr.com/,'Must be gettr link'),
  performers: yup.string().default('null'),
  Composer:yup.string().default('null'),
  Editor:yup.string().default('null'),
  Songwriter:yup.string().default('null'),
  Producer:yup.string().default('null'),
  Lyrics:yup.string().default('null'),
});


function onSubmit(values) {
  
  console.log('ppe'+values.musicname)
  store.dispatch('music/uploadmusic',{musicinfo:values, upfiles: files, createdate: createdate})
  
  // uploadFiles// upload file

  // ElMessageBox.alert(values.name, 'Successfully Uploaded', {
  //   // if you want to disable its autofocus
  //   // autofocus: false,
  //   confirmButtonText:'One More Song',
  //   cancelButtonText:'oncemore',
  //   callback: (action: Action) => {
  //     if (action === 'confirm'){
  //       router.push({name:'MusicHome'})
  //     }
  //   },
  // })

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