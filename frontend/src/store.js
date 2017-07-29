import { applyMiddleware, createStore }  from 'redux'
import { createLogger } from 'redux-logger'
import thunk from 'redux-thunk'
import promise from 'redux-promise-middleware'


import reducer from './reducers'

const logger = createLogger()
const middleware = applyMiddleware(promise(), thunk, logger)


/* eslint-disable no-underscore-dangle */
export default createStore(
  reducer, 
  /* preloadedState, */
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
    middleware,
)
/* eslint-enable */