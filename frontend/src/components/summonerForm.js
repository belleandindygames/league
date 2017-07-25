import { Form, FormControl, FormGroup, Button, ButtonGroup } from 'react-bootstrap';
import React, { Component } from 'react'

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
      <ButtonGroup>
        <Button active>Radio 1
          <input ref="input1" type="radio" name="radioButtonSet" value='input1' standalone defaultChecked/>
        </Button>
        <Button>Radio 2
          <input ref="input2" type="radio" name="radioButtonSet" value='input2' standalone/>
        </Button>
      </ButtonGroup>
    </FormGroup>
    {' '}
    <Button bsStyle="primary" type="submit">
      Search Live Games
    </Button>
  </Form>
    )
  }
}