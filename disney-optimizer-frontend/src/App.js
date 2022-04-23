import React, { useState } from 'react';
import './App.css';
import Plan from './components/Plan';
//import Flatpickr from "react-flatpickr";

function App() {
  const [planList, setPlanList] = useState([]);

  function loadRides() {
    setPlanList([]);
    fetch('/default').then(res => res.json()).then(data => {
      setPlanList(data.planList);
    });
  }

  return (
    <div className="App">
      {/* <Flatpickr
        data-enable-time
        value={date}
        onChange={date => {
          this.setState({ date });
        }}
      /> */}
      <button onClick={()=>loadRides()}>Load Rides</button>
      <Plan plans={planList}/>
    </div>
  );
}

export default App;
