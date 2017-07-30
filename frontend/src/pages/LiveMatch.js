import React, { Component } from 'react';
import '../App.css';
import CardLive from '../components/SummonerCardLive'
import { Table } from 'react-bootstrap'
//import { fetchLiveMatch } from '../actions/liveMatchActions'
import { fetchChampionInfo } from '../actions/generalActions'
import { connect } from 'react-redux'
import LiveSummonerForm from '../components/summonerForm'


const matchTableHeader = (
  <thead>
    <tr>
      <th>Name</th>
      <th>Champion</th>
      <th>Wins</th>
      <th>Runes</th>
      <th>Ranking</th>
    </tr>
  </thead>
)
class LiveMatch extends Component {
  componentWillMount() {

    this.props.dispatch(fetchChampionInfo())
  }
  submitForm() {

  }
  render() {
    const participants = this.props.match.match.participants
    const redTeam = participants.filter((p) => p.teamId === 200)
    const blueTeam = participants.filter((p) => p.teamId === 100)
    const mappedRedTeam = redTeam.map(summoner =><CardLive summonerInfo={summoner} region="na"/>)
    const mappedBlueTeam = blueTeam.map(summoner => <CardLive summonerInfo={summoner} region="na"/>)
    const { fetched, fetching } = this.props.match
  
   
    return (
      <div className="container">
        <h1 className="App-intro">Live Match</h1>
        <div>
          <LiveSummonerForm />
        </div>
        { fetched &&
        <div>
          <Table hover bordered responsive>
            {matchTableHeader}
            <tbody>
              {mappedRedTeam}
            </tbody>
          </Table>
          <Table hover bordered responsive>
            {matchTableHeader}
            <tbody>
              {mappedBlueTeam}
            </tbody>
          </Table>
        </div>}
        { fetching && 
        <h2>Loading...</h2>}
      </div>
    );
  }
}


 export default connect((store) => {
    return {
      match: store.liveMatch,
      champions: store.champions.champions,
    }
  })(LiveMatch)