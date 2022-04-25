import React, { useState } from 'react';
import { getRideInfo } from '../../utils/funcs';
import RideRateCompare from './RideRateCompare';

function RideRate({setReadyToRate, setReadyToPlan}) {
  const rideInfo = getRideInfo()
  const rideOrder = JSON.parse(localStorage.getItem('sorted-rides')).reverse()
  const [rideRateData, setRideRateData] = useState({i: 0, listOfRatings: [1000]});

  return (
    <div>
      <button onClick={()=>{
        localStorage.removeItem('sorted-rides')
        setReadyToRate(false)
      }}>Back to Ride Sorting</button>
      <RideRateCompare 
        rideLeft={rideInfo[rideOrder[rideRateData.i]]}
        rideRight={rideInfo[rideOrder[rideRateData.i+1]]}
        setRideRightRating={minutes=>{
          const newListOfRatings = [...rideRateData.listOfRatings, rideRateData.listOfRatings[rideRateData.i]*(parseInt(minutes)+30)/90];
          if (rideRateData.i+2<rideOrder.length) {
            setRideRateData({
              i: rideRateData.i+1,
              listOfRatings: newListOfRatings
            })
          } else {
            localStorage.setItem(
              'ride-ratings', 
              JSON.stringify(newListOfRatings.reverse())
            )
            setReadyToPlan(true)
          }
        }}
      />
    </div>
  )
}

export default RideRate