import { createSlice } from '@reduxjs/toolkit'

export const waitTimePredictsSlice = createSlice({
  name: 'waitTimePredicts',
  initialState: {
    data: JSON.parse(localStorage.getItem('wt-data')) || {},
    loading: false,
    lastUpdate: JSON.parse(localStorage.getItem('last-update')).lastUpdate || 0,
    doyFor: JSON.parse(localStorage.getItem('doy-for')) || {y: 0, mo: 1, d: 1}
  },
  reducers: {
    setLoading: (state) => {
      state.loading = true
    },
    updateData: (state, data) => {
      state.data = {...state.data, ...data.payload.data}
      state.lastUpdate = Date.now()
      state.loading = false
      state.doyFor = data.payload.doy
    },
    resetData: (state) => {
      state.data = {}
      localStorage.setItem('wt-data', state.data)
    },
    storeData: (state) => {
      localStorage.setItem('doy-for', JSON.stringify(state.doyFor))
      localStorage.setItem('last-update', JSON.stringify({lastUpdate: state.lastUpdate}))
      localStorage.setItem('wt-data', JSON.stringify(state.data))
    }
  },
})

// Action creators are generated for each case reducer function
export const { setLoading, updateData, resetData, storeData } = waitTimePredictsSlice.actions

export default waitTimePredictsSlice.reducer