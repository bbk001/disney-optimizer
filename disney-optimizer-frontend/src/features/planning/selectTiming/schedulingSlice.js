import { createSlice } from '@reduxjs/toolkit'

const now = new Date(Date.now())

export const schedulingSlice = createSlice({
  name: 'scheduling',
  initialState: {
    arrive: {h: 8, mi: 0},
    depart: {h: 23, mi: 50},
    doy: JSON.parse(localStorage.getItem('doy-for')) || {y: now.getFullYear(), mo: now.getMonth()+1, d: now.getDate()},
    tbr: 30
  },
  reducers: {
    setDoy: (state, doy) => {
      state.doy = doy.payload
    },
    setArrival: (state, arg) => {
      const date = arg.payload
      state.arrive = date
    },
    setDeparture: (state, arg) => {
      const date = arg.payload
      state.depart = date
    },
    setTbr: (state, arg) => {
      state.tbr = arg.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { setDoy, setArrival, setDeparture, setTbr } = schedulingSlice.actions

export default schedulingSlice.reducer