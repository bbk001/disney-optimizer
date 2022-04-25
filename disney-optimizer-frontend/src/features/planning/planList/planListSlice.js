import { createSlice } from '@reduxjs/toolkit'

export const planListSlice = createSlice({
  name: 'planList',
  initialState: {
    planList: [],
    loading: false
  },
  reducers: {
    setLoading: (state) => {
      state.loading = true
    },
    createPlanList: (state, data) => {
      state.planList = data.payload.planList
      state.loading = false
    },
    resetPlanList: (state) => {
      state.planList = []
    }
  },
})

// Action creators are generated for each case reducer function
export const { setLoading, createPlanList, resetPlanList } = planListSlice.actions

export default planListSlice.reducer