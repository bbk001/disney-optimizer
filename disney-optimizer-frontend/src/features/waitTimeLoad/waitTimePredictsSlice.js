import { createSlice } from '@reduxjs/toolkit'

export const waitTimePredictsSlice = createSlice({
  name: 'waitTimePredicts',
  initialState: {
    data: [],
    loading: false,
    lastUpdate: 0
  },
  reducers: {
    setLoading: (state) => {
      state.loading = true
    },
    setData: (state, data) => {
      state.data = data.payload
      state.lastUpdate = Date.now()
      state.loading = false
    }
  },
})

// Action creators are generated for each case reducer function
export const { setLoading, setData } = waitTimePredictsSlice.actions

export default waitTimePredictsSlice.reducer