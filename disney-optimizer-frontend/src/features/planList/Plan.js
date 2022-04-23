import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { setLoading, createPlanList } from './planListSlice';
import { loadWaitTimes } from '../waitTimeLoad/WaitTimeLoad';
import { isUpToDate } from '../../functions/util'

function Plan(props) {
  const lastWTUpdate = useSelector((state) => state.waitTimePredicts.lastUpdate)
  const waitTimePredicts = useSelector((state) => state.waitTimePredicts.data)
  const planList = useSelector((state) => state.planList.planList)
  const loading = useSelector((state) => state.planList.loading)


  const dispatch = useDispatch();

  const requestBody = {
    arrive: {'h': 8, 'mi': 0},
    depart: {'h': 23, 'mi': 50},
    rideWaitTimes: waitTimePredicts,
    tbr: 30
  }

  function makePlans() {
    if (isUpToDate(lastWTUpdate)) {
      const requestPlanOptions = {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody)
      };
      dispatch(setLoading())
      fetch('/requestPlans', requestPlanOptions).then(res => res.json()).then(data => {
        dispatch(createPlanList(data))
      });
    } else {
      loadWaitTimes(dispatch, {'y': 2022, 'mo': 4, 'd': 22})
    }
  }

  let loadButton;
  if (loading) {
    loadButton = <div>Loading...</div>
  } else {
    if (isUpToDate(lastWTUpdate)) {
      loadButton = <button onClick={makePlans}>Make Plans</button>
    } else {
      loadButton = null
    }
  }
  let tableOfPlans
  if (planList.length) {
    tableOfPlans = <table>
        <thead>
          <tr>
            <th>Ride</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {planList.map(ridePlan => 
            <tr>
              <td>{ridePlan.rideName}</td>
              <td>{ridePlan.startTime}</td>
            </tr>
          )}
        </tbody>
      </table>
  } else {
    tableOfPlans = null
  }
  return (
    <div>
      {loadButton}
      {tableOfPlans}
    </div>
  );
}

export default Plan;
