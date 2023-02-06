export default{
    setMusic(state, payload){
        state.musicid = payload.musicid;
        state.cover_address = payload.cover_address;
        state.music_address = payload.music_address;
        state.name = payload.musicname;
        state.post_date = payload.post_date;
        state.user_id = payload.user_id;
    },
    setlistofMusic(state, payload){
        state.listofmusic = payload.listofMusic; 
    },
    setlistofmusicinfo(state, payload){
        state.listofmusicinfo = payload.listofmusicinfo;
    },
    setmusiclyrics(state, payload){
        state.musiclyrics = payload.musiclyrics;
    },
    // setmusicscore(state, payload){
    //     state.musicscore=payload.musicscore
    // }
    // setuploadmusic(state, payload){
    //     state.uploadmusicinfo = payload.uploadmusicinfo;
    // }
}
