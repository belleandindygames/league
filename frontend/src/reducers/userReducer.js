export default function reducer(state={
    user: {
      id: 1,
      name: "Anthony",
      age: 29,
    },
    fetched: false, 
    fetching: false, 
    error: null,
  }, action) {
    switch (action.type) {
      case "FETCH_USER": {
        return {...state, fetching: true}
      }
      case "FETCH_USER_REJECTED": {
        return {...state, fetching: false, error: action.payload}
      }
      case "FETCH_USER_FULFILLED": {
        return {
          ...state,
          fetched:  true,
          fetching: false, 
          user: action.payload,
        }
      }
      case "SET_USER_NAME": {
        return {
          ...state, 
          user: {...state.user, name: action.payload},
        }
      }
      case "SET_USER_AGE": {
        return {
          ...state, 
         user: {...state.user, age: action.payload},
        }
      }
      default: {
        break;
      }
    }
    return state
}