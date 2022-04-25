import React, { useState } from 'react';
import RideCompare from '../features/rideCompare/RideCompare';
import DeselectRides from '../features/rideSelection/DeselectRides';
import { getRideInfo } from '../utils/funcs';

function RankingRides() {
  const rideInfo = getRideInfo()
  const rideList = Object.keys(rideInfo)
  const [readyToRank, setReadyToRank] = useState(localStorage.getItem('ready-to-rank'));
  const [insertSortData, setInsertSortData] = useState({i: 1, j: 0, key: rideList[1], list: rideList});

  if (readyToRank) {
    return (
      <div>
        <button onClick={()=>{
          localStorage.setItem('ready-to-rank', false)
          setReadyToRank(false)
        }}>Back to Ride Selection</button>
        <RideCompare 
          rideLeft={rideInfo[insertSortData.key]}
          rideRight={rideInfo[insertSortData.list[insertSortData.j]]}
          pickLeft={()=> {
            if (insertSortData.i+1<rideList.length) {
              setInsertSortData({
                i: insertSortData.i+1, 
                j: insertSortData.i, 
                key: insertSortData.list[insertSortData.i+1], 
                list: insertSortData.list
              });
            } else {
              localStorage.setItem('sorted-rides', JSON.stringify(insertSortData.list))
            }
          }}
          pickRight={()=>{
            const j = insertSortData.j
            let newList = insertSortData.list
            newList[j+1] = insertSortData.list[j]
            newList[j] = insertSortData.key
            if (j>0) {
              setInsertSortData({
                ...insertSortData,
                j: j-1,
                list: newList
              });
            } else {
              setInsertSortData({
                i: insertSortData.i+1, 
                j: insertSortData.i, 
                key: insertSortData.list[insertSortData.i+1], 
                list: newList
              });
            }
          }}
        />
      </div>
    )
  } else {
    return (
      <DeselectRides setReadyToRank={setReadyToRank}/>
    )
  }
}

export default RankingRides