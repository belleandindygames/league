import React, { Component } from 'react'
import '../App.css';
import LiveSummonerForm from '../components/summonerForm'

function mapStateToProps(state) {
  return {
    form: state.form
  }
}

class SummonerStats extends Component {
  render() {
    return (
      <div>
       
        <div className="container">
            <LiveSummonerForm /> 
          <p className="App-intro">
            Stats edit <code>src/App.js</code> and save to reload.
          </p>
        </div>
      </div>
    );
  }
}

export default SummonerStats;
