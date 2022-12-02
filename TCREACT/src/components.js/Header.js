import React, { Component } from 'react'
import './Mystyles.css'


class Header extends Component {
  render() {
    return (
      <div className='forheader'>
        <ul className='frheaderul'>
  <li className='lis'><a className='fra' href="#home">DoIt V1.2</a></li>
  <li className='lis'><a className='fra' href="#home">WorkSpace</a></li>
  <li className='lis'><a className='fra' href="#home">About</a></li>


  

  <li className='lisl'><a className='fra' href="#home">Log In</a></li>
  <li className='lisl'><a className='fra' href="#home">Sign up</a></li>

  

  
</ul>
      </div>
    )
  }
}

export default Header