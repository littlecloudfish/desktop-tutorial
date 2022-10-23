import axios from 'axios'

export default{
    async registeruser(context){
        const token = context.rootgetters.Token;
        // console.log('token info'+token);
    },
    async userlist(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const usernumber = 4;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/listofuser/'+usernumber
            }
            ).then(function(response){

                context.commit('setlistofUser',{
                    listofuser : response.data,
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
    async personinfo(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const usernumber = payload;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/userinfo/'+usernumber
            }
            ).then(function(response){

                context.commit('setpersoninfo',{
                    personinfo : response.data,
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
    async personmusic(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const searchtype = payload;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/records/'+searchtype
            }
            ).then(function(response){

                context.commit('serpersonmusic',{
                    personmusic : response.data,
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