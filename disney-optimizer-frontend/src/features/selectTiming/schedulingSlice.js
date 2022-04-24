import { createSlice } from '@reduxjs/toolkit'

const now = new Date(Date.now())

export const schedulingSlice = createSlice({
  name: 'scheduling',
  initialState: {
    arrive: {h: 8, mi: 0},
    depart: {h: 23, mi: 50},
    doy: {y: now.getFullYear(), mo: now.getMonth()+1, d: now.getDate()}
  },
  reducers: {
    setDoy: (state, arg) => {
      const date = arg.payload[0]
      state.doy = {y: date.getFullYear(), mo: date.getMonth()+1, d: date.getDate()}
    },
    setArrival: (state, arg) => {
      const date = arg.payload[0]
      state.arrive = {h: date.getHours(), mi: date.getMinutes()}
    },
    setDeparture: (state, arg) => {
      const date = arg.payload[0]
      state.depart = {h: date.getHours(), mi: date.getMinutes()}
    }
  },
})

// Action creators are generated for each case reducer function
export const { setDoy, setArrival, setDeparture } = schedulingSlice.actions

export default schedulingSlice.reducer