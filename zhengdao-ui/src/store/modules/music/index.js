import mutations from './mutations.js';
import actions from './actions.js';
import getters from './getters.js';

export default{
    namespaced: true,
    state(){
        return{
            musicid: null,
            cover_address: null,
            music_address: null,
            name: null,
            post_date: null,
            user_id: null,
            listofmusic: [],
            listofmusicinfo:[],
        };
    },
    mutations,
    actions,
    getters,
};