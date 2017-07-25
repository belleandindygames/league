import { combineReducers } from 'redux'

import tweets from "./tweetsReducer"
import user from "./userReducer"
import liveMatch from "./liveSummonerReducer"
import champions from "./championReducer"

export default combineReducers({
  tweets, 
  user,
  liveMatch,
  champions,
})