import { createSlice } from '@reduxjs/toolkit'

export const advancedSettingsSlice = createSlice({
  name: 'advancedSettings',
  initialState: {
    multiRidePrefs: 1/3
  },
  reducers: {
    setMultiRidePrefs: (state, data) => {
      state.multiRidePrefs = data.payload
    }
  },
})

// Action creators are generated for each case reducer function
export const { setMultiRidePrefs } = advancedSettingsSlice.actions

export default advancedSettingsSlice.reducer