import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

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
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={()=>loadRides()}>Load Rides</button>
        <p>The first ride is {firstRide}.</p>
      </header>
    </div>
  );
}

export default App;
