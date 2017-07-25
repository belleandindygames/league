export default function reducer(state={
    champions: {
    },
    fetching: false,
    fetched: false, 
    error: null,

  }, action) {

    switch (action.type) {
      case "FETCH_CHAMPIONS": {
        return {...state, fetching: true}
      }
      case "FETCH_CHAMPIONS_REJECTED": {
        return {...state, fetching: false, error: action.payload}
      }
      case "FETCH_CHAMPIONS_FULFILLED": {
        return {
          ...state,
          fetching: false,
          fetched: true, 
          champions: action.payload,
      }
    }
    default: {
      break;
    }
  }
  return state
}