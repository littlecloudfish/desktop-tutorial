export default{
    setMusic(state, payload){
        state.musicid = payload.musicid;
        state.cover_address = payload.cover_address;
        state.music_address = payload.music_address;
        state.name = payload.musicname;
        state.post_date = payload.post_date;
        state.user_id = payload.user_id;
    },
}
