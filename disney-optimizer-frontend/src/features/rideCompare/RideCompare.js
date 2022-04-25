import React from 'react';
import './RideCompare.css'

function RideCompare({rideLeft, rideRight, pickLeft, pickRight}) {
  return (
    <div>
      <div>If the lines were the same length would you prefer to ride:</div>
      <button
        onClick={pickLeft}
      >
        {rideLeft.rideName}
      </button>
      <div className='or'>OR</div>
      <button
        onClick={pickRight}
      >
        {rideRight.rideName}
      </button>
    </div>
  )
}

export default RideCompare