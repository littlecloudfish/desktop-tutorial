import axios from 'axios'

export default{
    async registeruser(context){
        const token = context.rootgetters.Token;
        // console.log('token info'+token);
    },
    async userlist(context, payload){
        const backapi = 'http://127.0.0.1:1943';
        const searchtype = 4;
        try{
            const errmes =await axios({
                method: 'get',
                url: backapi+'/listofuser/'+searchtype
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
}