export function isUpToDate(lastUpdate) {
  return (Date.now()-lastUpdate)/60000<120
}