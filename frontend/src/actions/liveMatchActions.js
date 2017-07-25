import axios from 'axios'

export function fetchLiveMatch(region, summoner) {
  var url = "/app/api/live/".concat(region, "/", summoner, "/")
  console.log(url)
  return function(dispatch) {
      axios.get(url)
        .then((response) => {
          dispatch({type: "FETCH_LIVE_MATCH_FULFILLED", payload: response.data})
        })
        .catch((err) => {
          dispatch({type: "FETCH_LIVE_MATCH_REJECTED", payload: err})
        })
    }
}
      


