import React, { Component } from 'react'
//import DataRender from './DataRender'
import DataRender from './DataRender'
import './Mystyles.css'

class DetailView extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         items : [],
         isloaded:false
      }
    }
    componentDidMount() {
        fetch(
`http://127.0.0.1:8000/api/single/${this.props.idd}`)
            .then((res) => res.json())
            .then((json) => {
                this.setState({
                    items: json,
                    DataisLoaded: true
                });
            })
    }
    render() {
        const { DataisLoaded, items } = this.state;
        if (!DataisLoaded) return <div>
            <h1> Pleses wait some time.... </h1> </div> ;
   
        return (
        <div className='forss'>
            <button onClick={()=> this.props.back()} className = 'btn1'>{`<`}</button>
            <p></p>
            <div className='srss'>
            
            <p className='frp'> <span className='srp'>Test Case No - </span> {items.tcnum}</p>
            <p className='frp'> <span className='srp'>Test Case Name -</span>  {items.tcname}</p>
            <p className='frp'> <span className='srp'>Created At -</span> Date : {items.created_at.slice(0,10)} Time : {items.created_at.slice(11,19)}</p>  
            </div>
            <br></br>
            {/* <h1> Fetch data from an api in react {items.tcdata}</h1> */}
            <DataRender namee = {items.tcdata}></DataRender>

  
  
  
            
        </div>
    );
}
}

export default DetailView