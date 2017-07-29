import React, { Component } from 'react'
import ToggleButtonGroup from 'react-bootstrap/es/ToggleButtonGroup'
import ToggleButton from 'react-bootstrap/es/ToggleButton'



export default class RegionRadioButtons extends Component {
  render() {

    return (
      <ToggleButtonGroup type="radio" name="options" defaultValue={"na1"} {...this.props}>
          <ToggleButton value={"na1"}>NA </ToggleButton>
          <ToggleButton value={"euw1"}>EUW </ToggleButton>
          <ToggleButton value={"kr"}>KR  </ToggleButton>
          <ToggleButton value={"la2"}>LAN </ToggleButton>
          <ToggleButton value={"la1"}>LAS </ToggleButton>
          <ToggleButton value={"br1"}>BR  </ToggleButton>
          <ToggleButton value={"tr1"}>TUR </ToggleButton>
          <ToggleButton value={"ru"}>RUS </ToggleButton>
          <ToggleButton value={"oc1"}>OCE</ ToggleButton>
          <ToggleButton value={"jp1"}>JP  </ToggleButton>
      </ToggleButtonGroup>
    )
  }
}