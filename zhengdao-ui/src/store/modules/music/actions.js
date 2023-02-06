import axios from 'axios';
// import createUploader from '../../../compositions/file-uploader';
const backapi = process.env.VUE_APP_APIURL;
export default{
    // async musicinfo(context, payload){
    // const backapi = 'http://127.0.0.1:1943';
    // const musicnumber = payload;
    // try{
    //     const errmes =await axios({
    //         method: 'get',
    //         url: backapi+'/music/'+musicnumber
    //     }
    //     ).then(function(response){
    //         context.commit('setMusic',{
    //             musicid : response.data[0].id,
    //             cover_address : response.data[0].cover_address,
    //             music_address : response.data[0].music_address,
    //             musicname : response.data[0].name,
    //             post_date : response.data[0].post_date,
    //             user_id : response.data[0].user_id,
    //         });
    //     });
    // }catch(err){
    //     if (err.message == 'Request failed with status code 401'){
    //         console.log('called if');
    //         throw { message : "Wrong password or username" , number: 1000};
    //     }
    //     else {
    //         throw err;
    //     }
    // }
    // },
    //feb 1
    // async musicinfo(context, payload){
    //     const backapi = 'http://127.0.0.1:1943';
    //     const musicnumber = payload;
    //     try{
    //         const errmes =await axios({
    //             method: 'get',
    //             url: backapi+'/music/'+musicnumber
    //         }
    //         ).then(function(response){
    //             context.commit('setlistofmusicinfo',{
    //                 listofmusicinfo : response.data,
                    
    //             });
    //         });
    //     }catch(err){
    //         if (err.message == 'Request failed with status code 401'){
    //             console.log('called if');
    //             throw { message : "No music info display" , number: 308};
    //         }
    //         else {
    //             throw err;
    //         }
    //     }
    // },
    async musicinfo(context, payload){
        
        const musicnumber = payload;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/music/'+musicnumber
            }
            ).then(function(response){
                context.commit('setlistofmusicinfo',{
                    listofmusicinfo : response.data,
                    
                });
            });
        }catch(err){
            if (err.message == 'Request failed with status code 401'){
                console.log('called if');
                throw { message : "No music info display" , number: 308};
            }
            else {
                throw err;
            }
        }
    },
    async uploadmusic(context, payload){
    //    console.log('commit action'+ typeof payload.musicinfo,typeof payload.upfiles.value[0])
       const fd = new FormData()
       fd.append('musicinfo',JSON.stringify(payload.musicinfo))
       fd.append('createdate', payload.createdate.value)
       console.log(payload.upfiles.value[0].file)
       fd.append('imagefile',payload.upfiles.value[0].file,payload.upfiles.value[0].file.name)
       axios({
        method: 'post',
        url: backapi+'/uploadmusicinfo',
        data: fd,
        headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json;charset=UTF-8",
                  },
       }).then((response)=>{
        console.log(response)
       },(error)=>{
        console.log(error)
       })
    //    // const data ={
        //     username: payload.username,
        //     password: payload.password,
        // }
        // axios({
        //     method: 'post',
        //     url: backapi+'/uploadmusicinfo/',
        //     data:data,
        //     headers: {
        //         Accept: "application/json",
        //         "Content-Type": "application/json;charset=UTF-8",
        //       },
         
        // }).then((response) => {
        //     console.log(response);
        // }, (error) => {
        //     console.log(error);
        // });
   
    },
    async musiclyrics(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const musicnumber = payload;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/showlyrics/'+musicnumber
            }
            ).then(function(response){
                context.commit('setmusiclyrics',{
                    musiclyrics : response.data,
                    
                });
            });
        }catch(err){
            if (err.message == 'Request failed with status code 401'){
                console.log('called if');
                throw { message : "No music lyrics display" , number: 308};
            }
            else {
                throw err;
            }
        }
    
    },
    async musiclistinfo(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const searchtype = 4;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/listmusics/'+searchtype
            }
            ).then(function(response){

                context.commit('setlistofMusic',{
                    listofMusic : response.data,
                });

            });
        }catch(err){
            if (err.message == 'Request failed with status code 401'){
                console.log('called if');
                throw { message : "No List Display" , number: 308};
            }
            else {
                throw err;
            }
        }
    },
    async setmusicscore(context, payload){
        const url = 'http://127.0.0.1:1943/ratemusic'
        const data ={
            musicid: payload.musicid,
            musicscore: payload.musicscore,
        }
        axios({
            method: 'post',
            url: url,
            data:data,
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json;charset=UTF-8",
              },
         
        }).then((response) => {
            console.log(response);
        }, (error) => {
            console.log(error);
        });
   
    },
}
         