import { createSlice } from '@reduxjs/toolkit'

export const waitTimePredictsSlice = createSlice({
  name: 'waitTimePredicts',
  initialState: {
    data: [],
    loading: false,
    lastUpdate: 0,
    doyFor: {y: 0, mo: 1, d: 1}
  },
  reducers: {
    setLoading: (state) => {
      state.loading = true
    },
    setData: (state, data) => {
      state.data = data.payload.data
      state.lastUpdate = Date.now()
      state.loading = false
      state.doyFor = data.payload.doy
    }
  },
})

// Action creators are generated for each case reducer function
export const { setLoading, setData } = waitTimePredictsSlice.actions

export default waitTimePredictsSlice.reducer