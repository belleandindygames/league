import React, { Component } from 'react';
import '../App.css';
import CardLive from '../components/SummonerCardLive'
import SummonerForm from '../components/summonerForm'
import { Table } from 'react-bootstrap'
import { fetchLiveMatch } from '../actions/liveMatchActions'
import { fetchChampionInfo } from '../actions/generalActions'
import { connect } from 'react-redux'


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
    //this.props.dispatch(fetchLiveMatch("na", "wiggily"))
    this.props.dispatch(fetchChampionInfo())
  }
  submitForm() {

  }
  render() {
    const participants = this.props.match.participants
    const redTeam = participants.filter((p) => p.teamId === 200)
    const blueTeam = participants.filter((p) => p.teamId === 100)
    const mappedRedTeam = redTeam.map(summoner =><CardLive summonerInfo={summoner} region="na"/>)
    const mappedBlueTeam = blueTeam.map(summoner => <CardLive summonerInfo={summoner} region="na"/>)
   
    return (
      <div className="container">
        <h1 className="App-intro">Live Match</h1>
        <div>
          <SummonerForm />
        </div>
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
      </div>
    );
  }
}


 export default connect((store) => {
    return {
      match: store.liveMatch.match,
      champions: store.champions.champions,
    }
  })(LiveMatch)