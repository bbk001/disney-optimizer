import React from 'react';
import Plan from '../features/planList/Plan';
import WaitTimeLoad from '../features/waitTimeLoad/WaitTimeLoad';
import Scheduling from '../features/selectTiming/Scheduling';

function Planning() {
  return (
    <div className="App">
      <Scheduling />
      <WaitTimeLoad />
      <Plan />
    </div>
  );
}

export default Planning;