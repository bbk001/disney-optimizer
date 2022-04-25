import { configureStore } from '@reduxjs/toolkit'
import planListSlice from '../features/planning/planList/planListSlice'
import schedulingSlice from '../features/planning/selectTiming/schedulingSlice'
import waitTimePredictsSlice from '../features/planning/waitTimeLoad/waitTimePredictsSlice'

export default configureStore({
  reducer: {
    waitTimePredicts: waitTimePredictsSlice,
    planList: planListSlice,
    scheduling: schedulingSlice,
  },
})