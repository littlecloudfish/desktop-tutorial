<template>
    <div>
        <input type="file" @change="onFileSelected">
        <el-button type="primary" @click="onUploadFile">Upload</el-button>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    
    data(){
        return{
            selectedFile: null,
        }
    },
    methods:{
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
            console.log(this.selectedFile.name)
        },
        onUploadFile(){
            const fd = new FormData();
            fd.append('pic', this.selectedFile, this.selectedFile.name)
            axios.post('http://127.0.0.1:1943/uploadimg',fd).then(res => {
                console.log(res)
            })
        }
    },

}
</script>
