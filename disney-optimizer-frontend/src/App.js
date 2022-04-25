import React, { useState } from 'react';
import RideRate from './features/rideRate/RideRate';
import DeselectRides from './features/rideSelection/DeselectRides';
import RideSort from './features/rideSort/RideSort';
import Planning from './features/planning/Planning';

function RankingRides() {
  const [readyToPlan, setReadyToPlan] = useState(JSON.parse(localStorage.getItem('ride-ratings')));
  const [readyToRate, setReadyToRate] = useState(JSON.parse(localStorage.getItem('sorted-rides')));
  const [readyToSort, setReadyToSort] = useState(JSON.parse(localStorage.getItem('excluded-rides')));

  if (readyToPlan) {
    return (
      <Planning setReadyToPlan={setReadyToPlan}/>
    )
  } else if (readyToRate) {
    return (
      <RideRate setReadyToRate={setReadyToRate} setReadyToPlan={setReadyToPlan}/>
    )
  } else if (readyToSort) {
    return (
      <RideSort setReadyToSort={setReadyToSort} setReadyToRate={setReadyToRate}/>
    )
  } else {
    return (
      <DeselectRides setReadyToSort={setReadyToSort}/>
    )
  }
}

export default RankingRides
