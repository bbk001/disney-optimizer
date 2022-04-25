import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { getRideInfo } from '../../utils/funcs';
import { resetPlanList } from '../planning/planList/planListSlice';
import RideCompare from './RideCompare';

function RideSort({setReadyToSort, setReadyToRate}) {
  const rideInfo = getRideInfo()
  const rideList = Object.keys(rideInfo)
  const [insertSortData, setInsertSortData] = useState({i: 1, j: 0, key: rideList[1], list: rideList});

  const dispatch = useDispatch()

  return (
    <div className='page'>
      <button 
        onClick={()=>{
          dispatch(resetPlanList())
          setReadyToSort(false)
        }}
        className='back'
      >&laquo; Back to Ride Selection</button>
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
            setReadyToRate(true)
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
}

export default RideSort