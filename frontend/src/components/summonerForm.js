import React, { Component } from 'react'
import { Field, reduxForm, SubmissionError } from 'redux-form'
import { Form, FormControl, FormGroup, Alert, ControlLabel, HelpBlock, Button } from 'react-bootstrap'
import { Input, Message } from 'semantic-ui-react'
import { fetchLiveMatch } from '../actions/liveMatchActions'
import RegionRadioButtons from '../components/RegionRadioButtons'


function FieldGroup({ id, label, help, ...props }) {
  return (
    <FormGroup controlId={id}>
      <ControlLabel>{label}</ControlLabel>
      <FormControl {...props} />
      {help && <HelpBlock>{help}</HelpBlock>}
    </FormGroup>
  );
}

class SummonerForm extends Component {
  summonerInput({ input, meta: { touched, error}, ...custom}) {
    const hasError = touched && error !== undefined
    return (
      <div>
        {hasError &&
          <Alert bsStyle='danger'>  
            <h3>Error</h3>
            <p>{error}</p> </Alert>}
        <FieldGroup
          id="formControlsText"
          type="text"
          label=""
          placeholder="Summoner..."
          {...input} {...custom}
        />     
      </div>
    )
  }

  regionsInput({ input, meta: { touched, error}, ...custom}) {
    return (
      <div>
         <RegionRadioButtons {...input} {...custom} />   
      </div>
    )
  }

  

  submit ({summonerName, region }) {
    this.props.dispatch(fetchLiveMatch(summonerName, region))
  }

  render () {
    const { handleSubmit } = this.props
    return (
      <form onSubmit={handleSubmit(this.submit.bind(this))}>
        <Field name='summonerName' component={this.summonerInput} />
        <Field name='region' component={this.regionsInput} type='radio' />
        <br />
        <Button type='submit'>Submit</Button>
      </form>

    )
  }
}

const validate = values => {
  const { summonerName }  = values
  const errors = {}
  if (!summonerName || summonerName.trim() === '') {
    errors.summonerName = 'Summoner name required'
  }
  return errors
}

export default reduxForm({
  form: 'liveSummonerForm',
  validate
})(SummonerForm)