//import logo from './logo.svg';
import './App.css';
//import ApiView from './components.js/ApiView';
import ListView from './components.js/ListView';
import Header from './components.js/Header';
// import HomePage from './components.js/HomePage';

function App() {
  return (
    <div >
      <div className='forheader'>

            <Header></Header>
            </div>
            <br></br>

    <div className="App1">
      {/* <HomePage></HomePage> */}
   {/* <ApiView /> */}
   <ListView/>
    </div>
    </div>
  );
}

export default App;
