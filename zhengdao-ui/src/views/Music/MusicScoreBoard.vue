<template>
    <div>
        <input type="file" @change="onFileSelected">
        <el-button type="primary" @click="onUploadFile">Upload</el-button>
    </div>
</template>

<script>
export default{
    data(){
        return{
            selectedFile: null,
        }
    },
    methods:{
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onUploadFile(){
            
        }
    },

}
</script>
