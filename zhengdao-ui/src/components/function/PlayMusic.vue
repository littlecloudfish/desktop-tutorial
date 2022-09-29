<template>
    <div>
        <slot>
            <av-bars
                :outline-width="0"
                :progress-width="6"
                :outline-meter-space="6"
                :playtime="true"
                :symmetric="true"
                :caps-color="lime"
                :bar-color="['#FFF','rgb(102, 255, 51)','rgb(153, 102, 255)']"
                playtime-font="18px Monaco"
                audio-src="/DEMOMUSIC/crimanal.mp3">
            </av-bars>
            <el-rate v-model="value" allow-half />
        </slot>
    </div>
    <el-button type="Success" round @click="showcom" >Login</el-button> 

</template>

<script>
import { mapGetters } from 'vuex'
export default{

    setup(){
        // this.$store.dispatch('music/musicinfo')
        
    },
    created(){
        this.$store.dispatch('music/musicinfo');
        
        // console.log(...mapGetters(['MusicUserid',]))
    },
    data(){
        return{
            value:null
        };
    },
    methods:{
        
        showcom(){
        console.log(this.$store.getters['music/Musicaddress']);
        
        }
    },
    

}
</script>

