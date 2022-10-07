<template>
    <div>
        <slot>
            <av-bars
                :outline-width="0"
                :progress-width="6"
                :outline-meter-space="6"
                :playtime="true"
                :symmetric="true"
                fft-size="2048"
                type="frequ"
                :caps-color="lime"
                :bar-color="['#FFF','rgb(102, 255, 51)','rgb(153, 102, 255)']"
                playtime-font="18px Monaco"
                cors-anonym="true"
                :audio-src="'http://127.0.0.1:1943/enjoymusic/'+this.musicid">
            </av-bars> 
            <el-rate v-model="value" allow-half /> 
            <!-- <audio controls>
                <source src="http://127.0.0.1:1943/enjoymusic/6" type="audio/ogg">
                <source src="http://127.0.0.1:1943/enjoymusic/6" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio> -->
        </slot>
    </div>
    <el-button type="Success" round @click="showcom" >login</el-button> 

</template>

<script>
import { mapGetters } from 'vuex'
export default{
    inject:['musicid'],
    data(){
        return{
            value:null
        };
    },
    setup(){
        // this.$store.dispatch('music/musicinfo')
    },
    created(){
        this.$store.dispatch('music/musicinfo');
        // console.log(this.musicid)
        // console.log(...mapGetters(['MusicUserid',]))
    },
    methods:{
        showcom(){
        console.log(this.$store.getters['music/Musicaddress']);
        
        }
    },
}
</script>

