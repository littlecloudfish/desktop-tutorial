<script> 
  import {useStore} from 'vuex'
  import {inject} from 'vue'
  export default {
    inject:['id'],
    async setup (){
        const store = useStore()
        await store.dispatch('astorefunction', inject('id'))
        const trylist = await store.getters['astoregettr']
        const audioList = [{
            name:trylist[0].name,
            url:url+trylist[0].id
        },
        {
            name:'hello',
            url:'http://127.0.0.1:5000'
        }
    ]
        return{
            trylist,
            audioList,
        }
    },
    data() {
      return {
        currentAudioName: '',
        otherList:[],
        dataready:false,
      }
    },
    methods: {
    },
    async beforeUpdate(){
        this.otherList = audioList;
      },
    
  }
</script> 