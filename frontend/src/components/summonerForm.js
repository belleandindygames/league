import { Form, FormControl, FormGroup, Button } from 'react-bootstrap';
import React, { Component } from 'react'
import RegionRadioButtons from '../components/RegionRadioButtons'

export default class SummonerForm extends Component {
  render () {
    return (
      <Form inline>
    <FormGroup controlId="formInlineName">
      <FormControl type="text" placeholder="Summoner Name" />
    </FormGroup>
    {' '}
    <FormGroup controlId="formInlineRegion">
      {' '}
      <RegionRadioButtons />
    </FormGroup>
    {' '}
    <Button bsStyle="primary" type="submit">
      Search Live Games
    </Button>
  </Form>
    )
  }
}



