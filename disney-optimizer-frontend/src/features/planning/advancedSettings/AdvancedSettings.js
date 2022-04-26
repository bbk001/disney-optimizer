import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { SegmentedControl } from 'segmented-control'
import './AdvancedSettings.css';
import { setMultiRidePrefs } from './advancedSettingsSlice';

function AdvancedSettings() {
  const multiRidePrefs = useSelector((state) => state.advancedSettings.multiRidePrefs)

  const dispatch = useDispatch()

  const optionsValues = [
    { label: "Yes!", value: 1/2},
    { label: "Usually", value: 1/3},
    { label: "Sometimes", value: 1/5},
    { label: "Rarely", value: 1/9},
    { label: "Never", value: 0}
  ]

  return (
    <div>
      <div className='explainer'>Do you like riding your favorite rides 2 or 3 times in the same day if you can?</div>
      <SegmentedControl
        name="choose"
        options={optionsValues.map(option => {return {...option, default: option.value===multiRidePrefs}})}
        setValue={newValue=>{dispatch(setMultiRidePrefs(newValue))}}
        style={{ height: 25, color: '#ab47bc' }} // purple400
      />
    </div>
  )
}

export default AdvancedSettings;

