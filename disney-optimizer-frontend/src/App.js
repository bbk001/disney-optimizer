import React, { useState } from 'react';
import './App.css';
import RideRate from './features/rideRate/RideRate';
import DeselectRides from './features/rideSelection/DeselectRides';
import RideSort from './features/rideSort/RideSort';
import Planning from './features/planning/Planning';

function RankingRides() {
  const [readyToPlan, setReadyToPlan] = useState(JSON.parse(localStorage.getItem('ride-ratings')));
  const [readyToRate, setReadyToRate] = useState(JSON.parse(localStorage.getItem('sorted-rides')));
  const [readyToSort, setReadyToSort] = useState(JSON.parse(localStorage.getItem('excluded-rides')));

  let body;
  if (readyToPlan) {
    body = <Planning setReadyToPlan={setReadyToPlan}/>
  } else if (readyToRate) {
    body = <RideRate setReadyToRate={setReadyToRate} setReadyToPlan={setReadyToPlan}/>
  } else if (readyToSort) {
    body = <RideSort setReadyToSort={setReadyToSort} setReadyToRate={setReadyToRate}/>
  } else {
    body = <DeselectRides setReadyToSort={setReadyToSort}/>
  }
  return (
    <div className='app-container'>
      {body}
    </div>
  )
}

export default RankingRides
