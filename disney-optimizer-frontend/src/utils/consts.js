export const parkOpen = {h: 7, mi: 50}
export const parkClose = {h: 23, mi: 50}

const minTime = new Date()
minTime.setHours(parkOpen.h)
minTime.setMinutes(parkOpen.mi)

const maxTime = new Date()
maxTime.setHours(parkClose.h)
maxTime.setMinutes(parkClose.mi+1)

const zeroTime = new Date()
zeroTime.setHours(0)
zeroTime.setMinutes(0)

export {minTime, maxTime, zeroTime}
