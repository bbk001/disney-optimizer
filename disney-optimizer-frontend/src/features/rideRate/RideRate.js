import React, { useState } from 'react';
import { getRideInfo } from '../../utils/funcs';
import RideRateCompare from './RideRateCompare';

function RideRate({setReadyToRate, setReadyToPlan}) {
  const rideInfo = getRideInfo()
  const rideOrder = JSON.parse(localStorage.getItem('sorted-rides')).reverse()
  const [rideRateData, setRideRateData] = useState({i: 0, listOfRatings: [1000]});

  let mainRideRate;
  if (rideOrder.length < 2) {
    mainRideRate = 
      <button
        onClick={()=>{
          localStorage.setItem(
            'ride-ratings', 
            JSON.stringify(rideRateData.listOfRatings)
          )
          setReadyToPlan(true)
        }}
      >
        Continue
      </button>
  } else {
    mainRideRate = 
      <RideRateCompare 
        rideLeft={rideInfo[rideOrder[rideRateData.i]]}
        rideRight={rideInfo[rideOrder[rideRateData.i+1]]}
        setRideRightRating={minutes=>{
          const newListOfRatings = [...rideRateData.listOfRatings, rideRateData.listOfRatings[rideRateData.i]*(parseInt(minutes)+60)/120];
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
  }

  return (
    <div className='page'>
      <button 
        onClick={()=>{
          localStorage.removeItem('sorted-rides')
          localStorage.removeItem('tie-data')
          setReadyToRate(false)
        }}
        className='back'
      >&laquo; Back to Ride Sorting</button>
      {mainRideRate}
    </div>
  )
}

export default RideRate