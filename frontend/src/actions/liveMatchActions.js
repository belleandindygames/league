import axios from 'axios'

export function fetchLiveMatch(summoner, region) {
  if (region == undefined) {
    region ='na1'
  }
  var url = "/app/api/live/".concat(region, "/", summoner, "/")
  console.log(url, summoner, region)
  return {
    type: "GO_GET_SUMMONER_MATCH", 
    payload: {
      summoner, 
      region,
    },
  } /*
  return function(dispatch) {
      axios.get(url)
        .then((response) => {
          dispatch({type: "FETCH_LIVE_MATCH_FULFILLED", payload: response.data})
        })
        .catch((err) => {
          dispatch({type: "FETCH_LIVE_MATCH_REJECTED", payload: err})
        })
    }*/
}
      


