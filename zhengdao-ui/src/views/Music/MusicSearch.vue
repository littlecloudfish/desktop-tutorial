<template>
<el-main>
    <display-music :posts="posts"></display-music>
</el-main>
</template>


<script>

export default({
    
    setup() {
        
    },
    data() {
        return{
            posts:[
                    {
                        "cover_address": "/demopicture/example.png",
                        "id": 1,
                        "music_address": "/DEMOMUSIC/crimanal.mp3",
                        "name": "crimanal",
                        "post_date": "2022-08-17T20:13:19",
                        "user_id": 1
                    },
                    {
                        "cover_address": "/demopicture/example.png",
                        "id": 2,
                        "music_address": "/DEMOMUSIC/crimanal.mp3",
                        "name": "dangerous",
                        "post_date": "2022-08-17T20:13:19",
                        "user_id": 2
                    },]

            
        }
    },
    
})
</script>
