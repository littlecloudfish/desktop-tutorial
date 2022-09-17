export default{
    setUser(state, payload){
        state.token = payload.token;
        // console.log(state.token);
        state.userId = payload.userid;
        state.tokenExpiration = payload.tokenExpiration;
    },
};