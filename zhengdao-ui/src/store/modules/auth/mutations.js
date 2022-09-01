export default{
    setUser(state, payload){
        // console.log(payload)
        state.token = payload.token;
        state.UserId = payload.userid;
        state.tokenExpiration = payload.tokenExpiration;
    },
};