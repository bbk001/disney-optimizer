import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { isUpToDate } from '../../../utils/funcs'
import loadWaitTimes from './loadWaitTimes';

function WaitTimeLoad() {
  const lastWTUpdate = useSelector((state) => state.waitTimePredicts.lastUpdate);
  const loading = useSelector((state) => state.waitTimePredicts.loading);
  const doy = useSelector((state) => state.scheduling.doy);
  const doyLoadedFor = useSelector((state) => state.waitTimePredicts.doyFor);

  const dispatch = useDispatch();

  const doysMatch = doy.y===doyLoadedFor.y && doy.mo===doyLoadedFor.mo && doy.d===doyLoadedFor.d
  let loadButton;
  if (loading || (isUpToDate(lastWTUpdate) && doysMatch)) {
    loadButton = null;
  } else {
    loadButton = <button onClick={()=> loadWaitTimes(dispatch, doy)}>Load Predictions</button>
  }

  return (
    <div>{loadButton}</div>
  )
}

export default WaitTimeLoad;

