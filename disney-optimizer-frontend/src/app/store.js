import { configureStore } from '@reduxjs/toolkit'
import waitTimePredictsSlice from '../features/waitTimeLoad/waitTimePredictsSlice'
import planListSlice from '../features/planList/planListSlice'

export default configureStore({
  reducer: {
    waitTimePredicts: waitTimePredictsSlice,
    planList: planListSlice
  },
})