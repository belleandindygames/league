import { Navbar, Nav, NavItem } from 'react-bootstrap';
import React, { Component } from 'react'
//import logo from '../logo.svg'
import  { LinkContainer } from 'react-router-bootstrap'




export default class SiteNav extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeKey: 1
    };
  }
  handleSelect(activeKey) {
   // this.setState.activeKey = this.eventKey.value;
   // console.log(this.eventKey.value)  
  }
  navigate() {
    
  }
  render() {
    
    return (
      <Navbar >
        <Navbar.Header>
          <Navbar.Brand>
            {/*<img src={logo} alt='League App Logo' height={32} width={32}/>*/}
            <LinkContainer to="/"><strong>League App | placeholder </strong></LinkContainer>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav bsStyle="pills" activeKey={this.state.activeKey} onSelect={this.handleSelect.bind(this)}>
            <LinkContainer to="/live"><NavItem eventKey={1}>Live Match Search</NavItem></LinkContainer>
            <LinkContainer to="/stats"><NavItem eventKey={2}>Summoner Stats</NavItem></LinkContainer>
            <LinkContainer to="/about"><NavItem eventKey={3}>About</NavItem></LinkContainer>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}