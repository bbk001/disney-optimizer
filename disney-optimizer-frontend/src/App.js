import React, { useState } from 'react';
import './App.css';
//import Flatpickr from "react-flatpickr";

function App() {
  const [firstRide, setFirstRide] = useState('');

  function loadRides() {
    setFirstRide('loading..');
    fetch('/default').then(res => res.json()).then(data => {
      setFirstRide(data.planList[0].rideName);
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
      <p>The first ride is {firstRide}.</p>
    </div>
  );
}

export default App;
