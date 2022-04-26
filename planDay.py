from thrillDataScrape import getWaitTimePredict
# from greedyAlpha import greedyAlpha
from Job import Job
# from lpApprox import lpApprox
from orToolsILP import lpApprox
from datetime import datetime
from datetime import timedelta

def plan(arrive, depart, doy, timeBetweenRides, rideValsDict):
  rideWaitTimes = getAllDayPredict(arrive, depart, doy, rideValsDict.keys())[1]
  jobList = makeJobs(arrive, depart, rideWaitTimes, timeBetweenRides, rideValsDict, 0.5)
  result = lpApprox(jobList, arrive, depart, rideValsDict.keys())
  return result

def makeJobs(arrive, depart, rideWaitTimes, timeBetweenRides, rideValsDict, rideDecay):
  jobList = []
  skipUntil = int((arrive['h']-8)*6+arrive['mi']/10)
  endOn = int((depart['h']-8)*6+depart['mi']/10)+1
  for rideName in rideValsDict.keys():
    timeOfDay = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
    waitTimes = rideWaitTimes[rideName]
    onRideTime = int(rideValsDict[rideName]['onRideTime'])
    vals = rideValsDict[rideName]['rideVals']
    if len(vals) == 1:
      firstVal = float(rideValsDict[rideName]['rideVals'][0])
      vals = [firstVal, firstVal*rideDecay, firstVal*rideDecay*rideDecay]
    for wt in waitTimes[skipUntil:endOn]:
      if wt:
        endTime = timeOfDay+timedelta(minutes=int(timeBetweenRides))+timedelta(minutes=wt)+timedelta(minutes=onRideTime)
        jobList.append(Job(timeOfDay, endTime, vals[0], rideName, timeBetweenRides))
        if vals[1]>20:
          jobList.append(Job(timeOfDay, endTime, vals[1], rideName+'2', timeBetweenRides))
          jobList.append(Job(timeOfDay, endTime, vals[2], rideName+'3', timeBetweenRides))
      timeOfDay+=timedelta(minutes=10)
  jobList.sort(key=lambda x: x.end)
  return jobList

def getAllDayPredict(arrive, depart, doy, rideList):
  y = doy['y']
  mo = doy['mo']
  d = doy['d']
  timeList = []
  nextTime = datetime(y, mo, d, arrive['h'], arrive['mi'])
  while nextTime <= datetime(y, mo, d, depart['h'], depart['mi']):
    timeList.append(nextTime)
    nextTime += timedelta(minutes=10)
  result = [list(getWaitTimePredict(ride, dateTimesToCheck=timeList)) for ride in rideList]
  resultDist = {}
  for rideResults, ride in zip(result, rideList):
    resultDist[ride] = rideResults
  return timeList, resultDist
