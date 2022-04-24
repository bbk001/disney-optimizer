import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { setLoading, setData } from './waitTimePredictsSlice';
import { isUpToDate } from '../../functions/util'

export function loadWaitTimes(dispatch, doy) {
  const arrive = {h: 8, mi: 0};
  const depart = {h: 23, mi: 50};
  const requestRidePredictOptions = {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      arrive: arrive,
      depart: depart,
      doy: doy
     })
  };
  dispatch(setLoading())
  fetch('/requestRidePredict', requestRidePredictOptions).then(res => res.json()).then(data => {
    dispatch(setData(data))
  });
}

function WaitTimeLoad() {
  const lastWTUpdate = useSelector((state) => state.waitTimePredicts.lastUpdate);
  const loading = useSelector((state) => state.waitTimePredicts.loading);
  const doy = useSelector((state) => state.scheduling.doy);

  const dispatch = useDispatch();

  let loadButton;
  if (loading) {
    loadButton = <div>Loading...</div>
  } else {
    if (isUpToDate(lastWTUpdate)) {
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

