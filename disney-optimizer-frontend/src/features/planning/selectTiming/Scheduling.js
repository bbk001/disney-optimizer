import "flatpickr/dist/themes/material_green.css";

import React from 'react';
import Flatpickr from "react-flatpickr";
import { useSelector, useDispatch } from 'react-redux'
import { minTime, maxTime } from "../../../utils/consts";
import { setArrival, setDeparture, setDoy, setTbr } from './schedulingSlice'

const timePickerOptions = {
  noCalendar: true, 
  dateFormat: "H:i", 
  time_24hr: true, 
  minuteIncrement: 10,
  minDate: minTime,
  maxDate: maxTime
};

function Scheduling() {
  const arrive = useSelector((state) => state.scheduling.arrive);
  const depart = useSelector((state) => state.scheduling.depart);
  const doy = useSelector((state) => state.scheduling.doy);
  const tbr = useSelector((state) => state.scheduling.tbr);

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
      <div>
        <div className="explainer">Choose which day you will go:</div>
        <Flatpickr
          key='date-picker'
          value={date}
          onChange={dates => {
            const date = dates[0]
            dispatch(setDoy({y: date.getFullYear(), mo: date.getMonth()+1, d: date.getDate()}))
          }}
        />
      </div>
      <div>
        <div className="explainer">Choose roughly when you will arrive:</div>
        <Flatpickr
          data-enable-time
          key='arrive-picker'
          options={timePickerOptions}
          value={arriveDate}
          onChange={arriveDates => {
            const date = arriveDates[0]
            dispatch(setArrival({h: date.getHours(), mi: date.getMinutes()}))
          }}
        />
      </div>
      <div>
        <div className="explainer">Choose roughly when you will leave:</div>
        <Flatpickr
          data-enable-time
          key='depart-picker'
          options={timePickerOptions}
          value={departDate}
          onChange={departDate => {
            const date = departDate[0]
            dispatch(setDeparture({h: date.getHours(), mi: date.getMinutes()}))
          }}
        />
      </div>
      <div>
        <div className="explainer">Choose how much time you will take between rides in minutes:</div>
        <input 
          type="number" 
          key="tbr" 
          value={tbr} 
          onChange={tbrNew => dispatch(setTbr(tbrNew.target.value))}
          step={5}
        />
        {/* <Flatpickr
          data-enable-time
          options={{...timePickerOptions, minDate: zeroTime, minuteIncrement: 5}}
          value={tbrDate}
          onChange={tbrDate => {
            const date = tbrDate[0]
            dispatch(setTbr(date.getHours()*60+date.getMinutes()))
          }}
        /> */}
      </div>
    </div>
  )
}

export default Scheduling