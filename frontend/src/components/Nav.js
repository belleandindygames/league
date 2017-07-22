import { Navbar, Nav, NavItem, NavbarBrand, NavDropdown, MenuItem } from 'react-bootstrap';
import React, { Component } from 'react'
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
  render() {
    return (
      <Navbar>
        <NavbarBrand>
          <a href='/'>League App | placeholder </a>
        </NavbarBrand>
        <Nav bsStyle="pills" activeKey={this.state.activeKey} onSelect={this.handleSelect.bind(this)}>
          <LinkContainer to="/live"><NavItem eventKey={1} ahref="/#/live">Live Match Search</NavItem></LinkContainer>
          <LinkContainer to="/stats"><NavItem eventKey={2} ahref="/#/stats">Summoner Stats</NavItem></LinkContainer>
          <LinkContainer to="/about"><NavItem eventKey={3} ahref="/#/about/">About</NavItem></LinkContainer>
     

        </Nav>
      </Navbar>
    );
  }
}