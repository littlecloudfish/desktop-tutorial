export default{
    async registeruser(context){
        const token = context.rootgetters.Token;
        console.log('token'+token);
    },
}