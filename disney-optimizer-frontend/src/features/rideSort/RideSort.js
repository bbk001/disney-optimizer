import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { getRideInfo } from '../../utils/funcs';
import { resetPlanList } from '../planning/planList/planListSlice';
import RideCompare from './RideCompare';

function RideSort({setReadyToSort, setReadyToRate}) {
  const rideInfo = getRideInfo()
  const [insertSortData, setInsertSortData] = useState({
    i: 1, 
    j: 0, 
    key: Object.keys(rideInfo)[1], 
    list: Object.keys(rideInfo), 
    tieData: {},
    tieOrder: []
  });

  const dispatch = useDispatch()

  let mainRideSort; 
  if (Object.keys(rideInfo).length < 2) {
    mainRideSort =
      <button
        onClick={()=>{
          localStorage.setItem('sorted-rides', JSON.stringify([Object.keys(rideInfo)[0]]));
          localStorage.removeItem('tie-data');
          setReadyToRate(true)
        }}
      >
        Continue
      </button>
  } else {
    mainRideSort = 
      <RideCompare 
        rideLeft={rideInfo[insertSortData.key]}
        rideRight={rideInfo[insertSortData.list[insertSortData.j]]}
        pickLeft={()=> {
          if (insertSortData.i+1<insertSortData.list.length) {
            setInsertSortData({
              ...insertSortData,
              i: insertSortData.i+1, 
              j: insertSortData.i, 
              key: insertSortData.list[insertSortData.i+1]
            });
          } else {
            localStorage.setItem('sorted-rides', JSON.stringify(insertSortData.list));
            localStorage.setItem('tie-data', JSON.stringify(insertSortData.tieData));
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
              ...insertSortData,
              i: insertSortData.i+1, 
              j: insertSortData.i, 
              key: insertSortData.list[insertSortData.i+1], 
              list: newList,
            });
          }
        }}
        pickEither={()=> {
          let newTieData = {...insertSortData.tieData}
          newTieData[insertSortData.list[insertSortData.j]] = insertSortData.key
          const newTieOrder = [insertSortData.list[insertSortData.j], ...insertSortData.tieOrder];
          let newList = insertSortData.list
          newList.splice(insertSortData.j, 1)
          if (insertSortData.i<insertSortData.list.length) {
            setInsertSortData({
              i: insertSortData.i,
              j: insertSortData.i-1, 
              key: newList[insertSortData.i], 
              list: newList,
              tieData: newTieData,
              tieOrder: newTieOrder
            });
          } else {
            localStorage.setItem('sorted-rides', JSON.stringify(insertSortData.list));
            localStorage.setItem('tie-data', JSON.stringify({
              tieOrder: newTieOrder, 
              tieData: newTieData
            }));
            setReadyToRate(true)
          }
        }}
      />
  }
  return (
    <div className='page'>
      <button 
        onClick={()=>{
          dispatch(resetPlanList())
          setReadyToSort(false)
        }}
        className='back'
      >&laquo; Back to Ride Selection</button>
      {mainRideSort}
    </div>
  )
}

export default RideSort