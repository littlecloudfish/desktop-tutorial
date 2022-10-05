<template>
    <div>
        <input type="file" @change="onFileSelected">
        <input type="file" @change="onMusicFileSelected">
        <el-button type="primary" @click="onUploadFile">Upload</el-button>
    </div>
</template>

<script>
import axios from 'axios';
export default{
    
    data(){
        return{
            selectedFile: null,
            musicfile: null,
        }
    },
    methods:{
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
            console.log(this.selectedFile.name)
        },
        onMusicFileSelected(event){
            this.musicfile = event.target.files[0]  //not sure 0 or 1
            console.log(this.musicfile.name)
        },
        onUploadFile(){
            const fd = new FormData();
            fd.append('pic', this.selectedFile, this.selectedFile.name)
            fd.append('mp3', this.musicfile, this.musicfile.name)
            axios.post('http://127.0.0.1:1943/uploadimg',fd).then(res => {
                console.log(res)
            })
        }
    },

}
</script>
