import React from 'react';
import Plan from './planList/Plan';
import WaitTimeLoad from './waitTimeLoad/WaitTimeLoad';
import Scheduling from './selectTiming/Scheduling';

function Planning({setReadyToPlan}) {
  return (
    <div className="App">
      <button onClick={()=>{
        localStorage.removeItem('ride-ratings')
        setReadyToPlan(false)
      }}>Back to Ride Rating</button>
      <Scheduling />
      <WaitTimeLoad />
      <Plan />
    </div>
  );
}

export default Planning;