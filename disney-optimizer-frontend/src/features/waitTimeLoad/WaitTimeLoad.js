import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { setLoading, updateData, resetData } from './waitTimePredictsSlice';
import { isUpToDate } from '../../utils/funcs'
import { parkClose, parkOpen } from '../../utils/consts';

const fullRideInfo = require('../../utils/fullRideInfo.json');

export function loadWaitTimes(dispatch, doy) {
  const arrive = parkOpen;
  const depart = parkClose;
  let someRideInfo = {};
  let counter = 0;
  dispatch(resetData());
  for (const key in fullRideInfo.keys()) {
    someRideInfo[key] = fullRideInfo[key];
    counter+=1;
    if (counter%5==0) {
      const requestRidePredictOptions = {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          arrive: arrive,
          depart: depart,
          doy: doy,
          rideDict: someRideInfo
        })
      };
      someRideInfo = {};
      dispatch(setLoading());
      fetch('/api/requestRidePredict', requestRidePredictOptions).then(res => res.json()).then(data => {
        dispatch(updateData({data, doy}));
      });
    }
  }
}

function WaitTimeLoad() {
  const lastWTUpdate = useSelector((state) => state.waitTimePredicts.lastUpdate);
  const loading = useSelector((state) => state.waitTimePredicts.loading);
  const doy = useSelector((state) => state.scheduling.doy);
  const doyLoadedFor = useSelector((state) => state.waitTimePredicts.doyFor);

  const dispatch = useDispatch();

  const doysMatch = doy.y===doyLoadedFor.y && doy.mo===doyLoadedFor.mo && doy.d===doyLoadedFor.d
  let loadButton;
  if (loading) {
    loadButton = <div>Loading...</div>
  } else {
    if (isUpToDate(lastWTUpdate) && doysMatch) {
      loadButton = null
    } else {
      loadButton = <button onClick={()=> loadWaitTimes(dispatch, doy)}>Load Predictions</button>
    }
  }

  return (
    <div>{loadButton}</div>
  )
}

export default WaitTimeLoad;

