import React from 'react';
import Plan from './planList/Plan';
import WaitTimeLoad from './waitTimeLoad/WaitTimeLoad';
import Scheduling from './selectTiming/Scheduling';

function Planning({setReadyToPlan}) {
  return (
    <div className="page">
      <button 
        onClick={()=>{
          localStorage.removeItem('ride-ratings')
          setReadyToPlan(false)
        }}
        className='back'
      >&laquo; Back to Ride Rating</button>
      <Scheduling />
      <WaitTimeLoad />
      <Plan />
    </div>
  );
}

export default Planning;