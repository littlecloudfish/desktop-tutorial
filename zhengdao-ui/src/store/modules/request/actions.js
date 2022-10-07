import axios from 'axios'

export default {
    // async contactCoach(context, payload) {
    //   const newRequest = {
    //     userEmail: payload.email,
    //     message: payload.message
    //   };
    //   const response = await fetch(
    //     `https://vue-http-demo-85e9e.firebaseio.com/requests/${payload.coachId}.json`,
    //     {
    //       method: 'POST',
    //       body: JSON.stringify(newRequest)
    //     }
    //   );
  
    //   const responseData = await response.json();
  
    //   if (!response.ok) {
    //     const error = new Error(
    //       responseData.message || 'Failed to send request.'
    //     );
    //     throw error;
    //   }
  
    //   newRequest.id = responseData.name;
    //   newRequest.coachId = payload.coachId;
  
    //   context.commit('addRequest', newRequest);
    // },
  async fetchRequests(context) {
      const accesstoken = context.rootGetters.Token;
      // console.log(accesstoken);
      const apiUrl = 'http://127.0.0.1:1943';
      axios.get(apiUrl+'/who_am_i', {
        headers: {
            Accept: 'application/json',
            Authorization: `Bearer ${accesstoken}`
            }
      })
      .then((res) => {
        console.log(res.data)
      })
      .catch((error) => {
        console.error(error)
      });

  },
  async uploadmusic(context, payload){
    // console.log(payload)
    const accesstoken = context.rootGetters.Token;
    axios({
      method:'POST',
      url: 'http://127.0.0.1:1943/uploadmusic',
      data: payload,
      headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${accesstoken}`
          }
    }).then(res => {
        console.log(res)
    })
    .catch((error)=>{
      console.error(error)
    })

  },
  // test
  async uploadmusicinfo(context, payload){
    // console.log(payload)
    const accesstoken = context.rootGetters.Token;
    axios({
      method:'POST',
      url: 'http://127.0.0.1:1943/uploadmusicinfo',
      data: payload,
      headers: {
          Accept: 'application/json',
          Authorization: `Bearer ${accesstoken}`
          }
    }).then(res => {
        console.log(res)
    })
    .catch((error)=>{
      console.error(error)
    })

  }

    // async fetchRequests(context) {
    //   const coachId = context.rootGetters.userId;
    //   const token = context.rootGetters.token;
    //   const response = await fetch(
    //     `https://vue-http-demo-85e9e.firebaseio.com/requests/${coachId}.json?auth=` +
    //       token
    //   );
    //   const responseData = await response.json();
  
    //   if (!response.ok) {
    //     const error = new Error(
    //       responseData.message || 'Failed to fetch requests.'
    //     );
    //     throw error;
    //   }
  
    //   const requests = [];
  
    //   for (const key in responseData) {
    //     const request = {
    //       id: key,
    //       coachId: coachId,
    //       userEmail: responseData[key].userEmail,
    //       message: responseData[key].message
    //     };
    //     requests.push(request);
    //   }
      
    //   context.commit('setRequests', requests);
    // }
  };