import axios from 'axios';

export default{
    async musicinfo(context, payload){
    const backapi = 'http://127.0.0.1:1943';
    const musicnumber = 4;
    try{
        const errmes =await axios({
            method: 'get',
            url: backapi+'/music/'+musicnumber
        }
        ).then(function(response){
            context.commit('setMusic',{
                musicid : response.data[0].id,
                cover_address : response.data[0].cover_address,
                music_address : response.data[0].music_address,
                musicname : response.data[0].name,
                post_date : response.data[0].post_date,
                user_id : response.data[0].user_id,
            });
            // console.log(post_date);
        });
    }catch(err){
        if (err.message == 'Request failed with status code 401'){
            console.log('called if');
            throw { message : "Wrong password or username" , number: 1000};
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
                throw { message : "Wrong password or username" , number: 1000};
            }
            else {
                throw err;
            }
        }
    },
}
         
        // }).then((response) => {
        //     context.commit('setUser',{
        //         token: response.data.access_token,
        //         userId: payload.username,
        //     });
        // 0
        // : 
        // cover_address
        // : 
        // "/demopicture/example.png"
        // id
        // : 
        // 1
        // music_address
        // : 
        // "/DEMOMUSIC/crimanal.mp3"
        // name
        // : 
        // "crimanal"
        // post_date
        // : 
        // "2022-08-17T20:13:19"
        // user_id
        // : 
        // 1
        // [[Prototype]]
        // : 
        // Object
        // length
        // : 
        // 1
        // [[Prototype]]
        // : 
        // Array(0)