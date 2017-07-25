import axios from 'axios'

export function fetchChampionInfo(region, champId) {
  var url = "/app/api/champions/"
    return function(dispatch) {
      axios.get(url)
        .then((response) => {
          dispatch({type: "FETCH_CHAMPIONS_FULFILLED", payload: response.data})
        })
        .catch((err) => {
          dispatch({type: "FETCH_CHAMPIONS_REJECTED", payload: err})
        })
  }
} 

