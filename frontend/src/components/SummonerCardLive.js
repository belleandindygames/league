import React, { Component } from 'react'
import { connect } from 'react-redux'

class CardLive extends Component {
  render () {
    const champId = this.props.summonerInfo.championId
    const champs = this.props.champions
    const champ = champs.filter((c) => c.id === champId)
    const team = this.props.summonerInfo.teamId
    const name = this.props.summonerInfo.summonerName
    const imgKey = champ[0].key
    const champName = champ[0].name
    const wins = this.props.summonerInfo.wins
    const patch = "7.14.1" //this.props.summonerInfo.patch
    const runes = "Runes" // {this.props.summonerInfo.runes} // not implementd yet
    const currentRank = "current season rank" // {this.props.summonerInfo.rank} // not implemented
    const leaguePoints = 100 //{this.props.summonerInfo.lp} // not implemented

    return (
      <tr>
        <td>{name}</td>
        <td><SummonerImg imageKey={imgKey} patch={patch} />{champName}</td>
        <td>{wins}{team}</td>
        <td>{runes}</td>
        <td>{currentRank}({leaguePoints})</td>
      </tr>
    );
  }
}

export default connect((store) => {
  return {
    champions: store.champions.champions
  }
})(CardLive)

class SummonerImg extends Component {

  render () {
    const imageKey = this.props.imageKey
    const patch = this.props.patch
    const imageURL = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + imageKey + ".png"
    if (!imageKey) {
      return null
    }
    return (
      <img src={imageURL} alt={imageKey}></img>
    );
  }
}