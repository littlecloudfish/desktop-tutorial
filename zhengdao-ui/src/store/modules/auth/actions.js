import axios from 'axios'
export default {
    async login(context, payload){
        
        const url = 'http://127.0.0.1:1943/login'
        const data ={
            username: payload.username,
            password: payload.password,
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
            context.commit('setUser',{
                token: response.data.access_token,
                userId: payload.username,
            });
        }, (error) => {
            console.log(error);
        });

    },

    async signup(context, payload){
        console.log(payload.password);
        const url = 'http://127.0.0.1:1943/register'
        const data ={
            username: payload.username,
            password: payload.password,
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

};
