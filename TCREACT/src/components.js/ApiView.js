import React, { Component } from 'react'
import DataRender from './DataRender'

class ApiView extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         items : [],
         isloaded:false
      }
    }
    componentDidMount() {
        fetch(
"http://127.0.0.1:8000/api/")
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
        <div >
            
            <h1> Fetch data from an api in react </h1>  {
                items.map((item) => ( 
                <ol key = { item.id } >
                    <b>Test Case Num - </b> { item.tcnum }<br></br>
                    <b>Test Case Name - </b> { item.tcname }<br></br>
                    <DataRender namee = {item.tcdata} />

                    {/* <b>Test Case Data - </b>: { item.tcdata }<br></br> */}
                    <b>Created At - </b>{item.created_at}<br></br>
                    </ol>
                ))
            }
        </div>
    );
}
}

export default ApiView