export default{
    Musicid(state){
        return state.musicid;
    },
    Coveraddress(state){
        return state.cover_address;
    },
    Musicaddress(state){
        return state.music_address;
    },
    Musicname(state){
        return state.name;
    },
    Postdate(state){
        return state.postdate;
    },
    MusicUserid(state){
        // console.log("ss")
        return state.user_id;
    },
    listofMusic(state){
        return state.listofmusic;
    },
    listofmusicinfo(state){
        return state.listofmusicinfo;
    },
    musiclyrics(state){
        return state.musiclyrics.lyrics;
    }
}
