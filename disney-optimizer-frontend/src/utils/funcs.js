import fullRideInfo from './fullRideInfo.json'

export function isUpToDate(lastUpdate) {
  return (Date.now()-lastUpdate)/60000<120
}

export function getRideInfo() {
  const excludedRides = localStorage.getItem('excluded-rides') || []
  let usableRideInfo = {}
  for (const ride in fullRideInfo) {
    if (!excludedRides.includes(ride)) {
      usableRideInfo[ride] = fullRideInfo[ride]
    }
  }
  return usableRideInfo
}