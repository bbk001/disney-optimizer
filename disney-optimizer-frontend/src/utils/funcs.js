import fullRideInfo from './fullRideInfo.json'

export function isUpToDate(lastUpdate) {
  return (Date.now()-lastUpdate)/60000<120
}

export function getRideInfo() {
  const rideDecay = 2/3
  const excludedRides = JSON.parse(localStorage.getItem('excluded-rides')) || [];
  const ridesSorted = JSON.parse(localStorage.getItem('sorted-rides'));
  const ridesRates = JSON.parse(localStorage.getItem('ride-ratings'));
  const {tieOrder, tieData} = JSON.parse(localStorage.getItem('tie-data')) || {tieOrder: [], tieData: {}};
  const ridesAreRated = ridesSorted && ridesRates;
  let rideRatesDict = {};
  if (ridesAreRated) {
    for (let idx = 0; idx < ridesSorted.length; idx++) {
      rideRatesDict[ridesSorted[idx]] = ridesRates[idx];
    }
  }
  for (const rideTied of tieOrder) {
    // Set the value of the ride that is tied and not yet reated to the value of the ride that is tied and is rated.
    rideRatesDict[rideTied] = rideRatesDict[tieData[rideTied]]
  }
  let usableRideInfo = {}
  for (const ride in fullRideInfo) {
    if (!excludedRides.includes(ride)) {
      usableRideInfo[ride] = fullRideInfo[ride]
      if (ridesAreRated) {
        const rideVal = rideRatesDict[ride]
        usableRideInfo[ride].rideVals = [rideVal, rideVal*rideDecay, rideVal*rideDecay*rideDecay]
      }
    }
  }
  return usableRideInfo
}