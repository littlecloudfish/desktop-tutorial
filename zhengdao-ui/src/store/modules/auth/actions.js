import axios from 'axios'
export default {
    // login(){

    // },
    async signup(context, payload){
        console.log(payload.password);
        // const response = await fetch('http://127.0.0.1:1943/register',{
        //     method:'POST',
        //     body: JSON.stringify({
        //         username: payload.username,
        //         password: payload.password,
        //     })
        // });
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
    //     axios
    //         .post(url, data,{
    //             headers: {
    //               Accept: "application/json",
    //               "Content-Type": "application/json;charset=UTF-8",
    //             },
                
    // })
        // .then(({data}) => {
        //     console.log(data);
        // })
        // const responseData = await response.json();
        // console.log(response)
        // context.commit('setUser',{
        //     token: responseData.idToken
        // })
    },

};