import React, { useState } from 'react';

function RideRateCompare({rideLeft, rideRight, setRideRightRating}) {
  const [minutes, setMinutes] = useState(45);

  return (
    <div>
      <div className='explainer tripLine'>
        If the line for <b>{rideLeft.rideName}</b> were 60 minutes how 
        short would the line for <b>{rideRight.rideName}</b> need to 
        be for you to ride it instead:
      </div>
        <input 
          type="number" 
          key="minTime" 
          value={minutes}
          max={60}
          min={0}
          step={1}
          onChange={newMinutes => setMinutes(newMinutes.target.value)}
        />
        <button onClick={() => setRideRightRating(minutes)}>Enter</button>
    </div>
  )
}

export default RideRateCompare