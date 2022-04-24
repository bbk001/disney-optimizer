import "flatpickr/dist/themes/material_green.css";

import React from 'react';
import Flatpickr from "react-flatpickr";
import { useSelector, useDispatch } from 'react-redux'
import { setArrival, setDeparture, setDoy } from './schedulingSlice'

function Scheduling() {
  const arrive = useSelector((state) => state.scheduling.arrive);
  const depart = useSelector((state) => state.scheduling.depart);
  const doy = useSelector((state) => state.scheduling.doy);

  const date = new Date()
  date.setFullYear(doy.y)
  date.setMonth(doy.mo-1)
  date.setDate(doy.d)

  const arriveDate = new Date()
  arriveDate.setHours(arrive.h)
  arriveDate.setMinutes(arrive.mi)

  const departDate = new Date()
  departDate.setHours(depart.h)
  departDate.setMinutes(depart.mi)

  const dispatch = useDispatch();
  return (
    <div>
      <Flatpickr
        key='date-picker'
        value={date}
        onChange={date => {
          dispatch(setDoy(date))
        }}
      />
      <Flatpickr
        data-enable-time
        key='arrive-picker'
        options={{noCalendar: true, dateFormat: "H:i", time_24hr: true}}
        value={arriveDate}
        onChange={arriveDate => {
          dispatch(setArrival(arriveDate))
        }}
      />
      <Flatpickr
        data-enable-time
        key='depart-picker'
        options={{noCalendar: true, dateFormat: "H:i", time_24hr: true}}
        value={departDate}
        onChange={departDate => {
          dispatch(setDeparture(departDate))
        }}
      />
    </div>
  )
}

export default Scheduling