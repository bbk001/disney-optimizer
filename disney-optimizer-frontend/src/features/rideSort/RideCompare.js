import React from 'react';

function RideCompare({rideLeft, rideRight, pickLeft, pickRight}) {
  console.log(rideLeft)
  return (
    <div>
      <div className='explainer'>If the lines were the same length would you prefer to ride:</div>
      <button className='sort-option'
        onClick={pickLeft}
      >
        {rideLeft.rideName}
      </button>
      <div className='or'>OR</div>
      <button className='sort-option'
        onClick={pickRight}
      >
        {rideRight.rideName}
      </button>
    </div>
  )
}

export default RideCompare