import { parkClose, parkOpen } from '../../../utils/consts';
import { getRideInfo } from '../../../utils/funcs';
import { setLoading, updateData, resetData, storeData } from './waitTimePredictsSlice';

const numRequestsAtOnce = 3;

export default async function loadWaitTimes(dispatch, doy) {
  const arrive = parkOpen;
  const depart = parkClose;
  let someRideInfo = {};
  let counter = 0;
  dispatch(resetData());
  for (let key in getRideInfo()) {
    someRideInfo[key] = getRideInfo()[key];
    counter+=1;
    if (counter%numRequestsAtOnce===0) {
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
      dispatch(setLoading());
      const res = await fetch('/api/requestRidePredict', requestRidePredictOptions)
      const data = await res.json()
      dispatch(updateData({data, doy}));
      someRideInfo = {};
    }
  }
  const finalRequestRidePredictOptions = {
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
  dispatch(setLoading());
  const finalRes = await fetch('/api/requestRidePredict', finalRequestRidePredictOptions)
  const finalData = await finalRes.json()
  dispatch(updateData({data: finalData, doy}));
  dispatch(storeData())
}