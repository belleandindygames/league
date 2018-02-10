import React, { Component } from 'react';
import '../App.css';
import AboutCard from '../components/aboutcard'
import {Grid, Row, Col} from 'react-bootstrap'


class About extends Component {
  render() {
    return (
      <div>
         
        <div className="container">
        <h1 className="text-center">ABOUT US</h1>
         <Grid>
            <Row>
            <Col xs={12} md={3} ></Col>
              <Col xs={12} md={3} >
                <AboutCard name='Snowcola' 
                          imgurl='https://avatars3.githubusercontent.com/u/4368209?s=460&v=4' 
                          about='One guy who made this thing' />
              </Col>
              <Col xs={12} md={3} >
                <AboutCard name='bobbelly' 
                          imgurl='https://avatars2.githubusercontent.com/u/26680489?s=460&v=4' 
                          about='One guy who made this thing' />
              </Col>
              <Col xs={12} md={3} ></Col>
            </Row>
          </Grid>
        </div>
      </div>
    );
  }
}

export default About;
