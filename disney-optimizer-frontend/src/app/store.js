import { configureStore } from '@reduxjs/toolkit'
import waitTimePredictsSlice from '../features/waitTimeLoad/waitTimePredictsSlice'
import planListSlice from '../features/planList/planListSlice'
import schedulingSlice from '../features/selectTiming/schedulingSlice'

export default configureStore({
  reducer: {
    waitTimePredicts: waitTimePredictsSlice,
    planList: planListSlice,
    scheduling: schedulingSlice,
  },
})