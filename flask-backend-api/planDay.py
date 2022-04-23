from thrillDataScrape import getWaitTimePredict
# from greedyAlpha import greedyAlpha
from Job import Job
# from lpApprox import lpApprox
from orToolsILP import lpApprox
from defaultRideDict import rideDict
from datetime import datetime
from datetime import timedelta
import argparse

rideList = rideDict.keys()
rideVals = rideDict.values()

def plan(arrive, depart, doy, timeBetweenRides, rideValsDict):
  rideWaitTimes = getAllDayPredict(arrive, depart, doy)[1]
  jobList = makeJobs(arrive, rideWaitTimes, timeBetweenRides, rideValsDict)
  result = lpApprox(jobList, arrive, depart)
  return result

def makeJobs(arrive, rideWaitTimes, timeBetweenRides, rideValsDict):
  jobList = []
  for rideName in rideValsDict.keys():
    timeOfDay = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
    waitTimes = rideWaitTimes[rideName]
    vals = rideValsDict[rideName]
    for wt in waitTimes:
      if wt:
        endTime = timeOfDay+timedelta(minutes=timeBetweenRides)+timedelta(minutes=wt)
        jobList.append(Job(timeOfDay, endTime, vals[0], rideName, timeBetweenRides))
        jobList.append(Job(timeOfDay, endTime, vals[1], rideName+'2', timeBetweenRides))
        jobList.append(Job(timeOfDay, endTime, vals[2], rideName+'3', timeBetweenRides))
      timeOfDay+=timedelta(minutes=10)
  jobList.sort(key=lambda x: x.end)
  return jobList

def getAllDayPredict(arrive, depart, doy):
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

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("date", help = "Enter day to plan for in yyyy/mm/dd form.", type=str)
  parser.add_argument("arrivalTime", help = "Enter day to plan for in hh:mm form.", type=str)
  parser.add_argument("leaveTime", help = "Enter day to plan for in hh:mm form.", type=str)
  parser.add_argument("timeBetweenRides", help = "Enter the time in minutes between rides.", type=int)
  args = parser.parse_args()

  dateList = args.date.split('/')
  startTimeList = args.arrivalTime.split(':')
  endTimeList = args.leaveTime.split(':')
  arrive = {'h': int(startTimeList[0]), 'mi': int(startTimeList[1])}
  depart = {'h': int(endTimeList[0]), 'mi': int(endTimeList[1])}
  doy = {'y': int(dateList[0]), 'mo': int(dateList[1]), 'd': int(dateList[2])}
  plans = plan(arrive, depart, doy, args.timeBetweenRides, rideDict)
  # for ride in plans:
  #   print(ride)
  # print('Total value: {}'.format(sum(map(lambda x: x.val, plans))))
