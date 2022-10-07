<template>
    <div>
        <play-music ></play-music>
    </div>
</template>

<script>

export default ({
    setup() {
        
    },
    data(){
        // return{
        //     musicid:null
        // }
    },
    created(){
    //   this.musicid=this.$route.params.id;  
    },
    provide(){
        return{
            musicid: this.$route.params.id
        }
    },
})
</script>


