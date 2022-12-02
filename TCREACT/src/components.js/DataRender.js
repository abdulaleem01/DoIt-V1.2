import React from 'react'
import './Mystyles.css'


function DataRender(props) {
    let arr = []
    var new1 = props.namee;
    let l=''; 
let tt='';
//let c1 = '';
let t1 = '';
let cc = 1;
//let c1 = '';

// function hellw(numm,data1) {
//     return (
//       <div >
//      <h1>{numm} {data1}</h1>
//       </div>
//     );
//   }

    //const new1 = props.namee;
    //const Greet = (dataa) => {
       
        for (let n of new1) {

            l+=n;
            if (n === '^'){
                tt = l.replace('^','');
                //console.log(cc,tt);
                arr.push({num:cc,data:tt})
                //hellw(cc,tt)

                l = '';
                //c1 = cc;
                cc+=1;
                // return (
                //    <div>DataRender 
                //        <h1>{c1} {tt}</h1>
                //    </div>
                //  )
                //return tt
            };
            if (n === '~'){
                t1 = l.replace('~','')

                //console.log(cc,t1);
                arr.push({num:cc,data:t1})

                l = '';
                // return (
                //     <div>DataRender 
                //         <h1>{new1}</h1>
                //     </div>
                //   )
                //return t1
    }
}
//console.log(arr)
return(
    <div className='foritemdata'>
        

        {arr.map((item,i) => (
            <div key={i} className='neww'>
        <p ><span className='stepname'><b>Step{item.num}:</b></span> <br></br>{item.data}</p></div>
      ))}
    </div>
)
}

// return (
//     <div>DataRender -{new1}
//     </div>
//   )
    
//    //Greet(new1);
// }


export default DataRender