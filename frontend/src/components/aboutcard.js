import React, { Component } from 'react'
import Image from 'react-bootstrap/es/Image'

export default class AboutCard extends Component {
  render () {
    const name = this.props.name
    const imgurl = this.props.imgurl
    const about = this.props.about

    if (!name) {
      return null
    }
    return (
      <div>
        <span className="text-center"><h2>{name}</h2>
        <Image className="center-block" src={imgurl} alt={name} circle width="128" height="128" />
        <p>{about}</p>
        </span>
      </div>
      
    );
  }
}