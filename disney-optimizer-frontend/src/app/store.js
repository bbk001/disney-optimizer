import { configureStore } from '@reduxjs/toolkit'
import advancedSettingsSlice from '../features/planning/advancedSettings/advancedSettingsSlice'
import planListSlice from '../features/planning/planList/planListSlice'
import schedulingSlice from '../features/planning/selectTiming/schedulingSlice'
import waitTimePredictsSlice from '../features/planning/waitTimeLoad/waitTimePredictsSlice'

export default configureStore({
  reducer: {
    waitTimePredicts: waitTimePredictsSlice,
    planList: planListSlice,
    scheduling: schedulingSlice,
    advancedSettings: advancedSettingsSlice,
  },
})