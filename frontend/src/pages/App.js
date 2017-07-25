import React, { Component } from 'react'
import '../App.css'
import { connect } from 'react-redux'
import  { fetchUser } from "../actions/userActions"
import { fetchTweets } from "../actions/tweetsActions"
import { fetchChampionInfo } from  "../actions/generalActions"

class App extends Component {
  componentWillMount() {
    //this.props.dispatch(fetchUser())
  }

  fetchTweets() {
    this.props.dispatch(fetchTweets())
  }

  render() {
    console.log(this.props)
    const { user, tweets } = this.props

    if (!tweets.length) {
      return <button onClick={this.fetchTweets.bind(this)}>load tweets</button>
    }
    const mappedTweets = tweets.map(tweet => <li>{tweet.text}</li>)
    return (
      <div>
        <h1>{this.props.user.name}</h1>
        <ul>{mappedTweets}</ul>
      </div>
    )
      
    }
      
    
    }
  

  export default connect((store) => {
    return {
      user: store.user.user,
      userFetched: store.user.fetched,
      tweets: store.tweets.tweets,
      champions: store.champions.champion,
    }
  })(App)
 
