import React from 'react';
import './App.css';
import Plan from './features/planList/Plan';
import WaitTimeLoad from './features/waitTimeLoad/WaitTimeLoad';
import Scheduling from './features/selectTiming/Scheduling';
//import Flatpickr from "react-flatpickr";

function App() {

  return (
    <div className="App">
      {/* <Flatpickr
        data-enable-time
        value={date}
        onChange={date => {
          this.setState({ date });
        }}
      /> */}
      <Scheduling />
      <WaitTimeLoad />
      <Plan />
    </div>
  );
}

export default App;
