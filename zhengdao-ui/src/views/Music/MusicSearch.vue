<template>
    <el-button type="Success" round @click="showcom" >Login</el-button> 

<el-main v-if="dataready">
    <display-music :posts="posts"></display-music>
</el-main>
<!-- <div v-if="dataready" >{{posts}}</div> -->
</template>


<script>

export default({
    setup() {
    },
    data() {
        return{
            // posts:[
            //         {
            //             "cover_address": "/demopicture/example.png",
            //             "id": 1,
            //             "music_address": "/DEMOMUSIC/crimanal.mp3",
            //             "name": "crimanal",
            //             "post_date": "2022-08-17T20:13:19",
            //             "user_id": 1
            //         },
            //         {
            //             "cover_address": "/demopicture/example.png",
            //             "id": 2,
            //             "music_address": "/DEMOMUSIC/crimanal.mp3",
            //             "name": "dangerous",
            //             "post_date": "2022-08-17T20:13:19",
            //             "user_id": 2
            //         },],
            posts : null,
            dataready : false,
            
        }
    },
    async beforeCreate(){
        this.$store.dispatch('music/musiclistinfo').then(() => {
            this.posts = this.$store.getters['music/listofMusic'];
            this.dataready = true;
        })
    },
    created(){    },
    methods : {
        showcom(){
            console.log(this.$store.getters['music/listofMusic']);
            this.posts=this.$store.getters['music/listofMusic']
        }
    },
    mounted(){ },
    computed:{},
    
})
</script>
