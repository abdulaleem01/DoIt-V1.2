import React, { Component } from 'react'
//import DataRender from './DataRender'
//import NewTest from './NewTest'
import DetailView from './DetailView'
import './Mystyles.css'




class ListView extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         items : [],
         isloaded:false,
         isclick:'',
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
        const { isclick, items } = this.state;
        if (isclick !== '') return <div>
            {/* <h1> Pleses wait some time.... </h1> </div> ; */}
            <DetailView idd= {isclick} back = {()=>this.setState({isclick:''})}></DetailView>
            </div>

   
        return (
        <div className='forlistdiv'>
            
            {/* <h1> Fetch data from an api in react </h1>  { */}
            {
                items.map((item) => ( 
                <ol key = { item.id } >
                    <div className='fordivcontainer' onClick={()=>this.setState({isclick:item.id})}>
                    <b>Test Case Num - </b> { item.tcnum }<br></br>
                    <b>Test Case Name - </b> { item.tcname }<br></br>
                    </div>

                    {/* <DataRender namee = {item.tcdata} /> */}

                    {/* <b>Test Case Data - </b>: { item.tcdata }<br></br> */}
                    {/* <b>Created At - </b>{item.created_at}<br></br> */}
                    </ol>
                ))
            }
            </div>
    );
}
}

export default ListView