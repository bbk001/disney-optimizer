from thrillDataScrape import getWaitTimePredict
from greedyAlpha import greedyAlpha
# from lpApprox import lpApprox
from orToolsILP import lpApprox
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np


rideList = [
  'bigthundermountainrailroad',
  'starwarsriseoftheresistance',
  'spacemountain',
  'splashmountain',
  'millenniumfalconsmugglersrun',
  'matterhornbobsleds',
  'indianajonesadventure',
  'buzzlightyearastroblasters',
  'startourstheadventurescontinue',
  'junglecruise',
  'mrtoadswildride',
  'autopia',
  'hauntedmansion',
  'piratesofthecaribbean'
]

rideVals = [
  (55,45),
  (100,55),
  (80,70),
  (40,30),
  (75,25),
  (50,45),
  (55,35),
  (45,35),
  (30,25),
  (40,30),
  (35,25),
  (35,20),
  (45,30),
  (45,25)
]

def plan(arrive, depart, doy, timeBetweenRides, valueList):
  rideWaitTimes = getAllDayPredict(arrive, depart, doy)[0]
  jobList = makeJobs(arrive, rideWaitTimes, timeBetweenRides, valueList)
  result = lpApprox(jobList, arrive, depart)
  # return result

class Job:
  def __init__(self, startTime, endTime, value, ride, timeBetweenRides):
    self.start = startTime
    self.end = endTime
    self.val = value
    self.ride = ride
    self.tbr = timeBetweenRides
  
  def __str__(self) -> str:
    startRide = self.start.strftime('%H:%M')
    endRide = (self.end - timedelta(minutes=self.tbr)).strftime('%H:%M')
    return 'Ride {} at {} until {} for a value of {}'.format(self.ride, startRide, endRide, self.val)

def makeJobs(arrive, rideWaitTimes, timeBetweenRides, valueList):
  jobList = []
  for name, waitTimes, vals in zip(rideList, rideWaitTimes, valueList):
    timeOfDay = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
    for wt in waitTimes:
      if wt:
        endTime = timeOfDay+timedelta(minutes=timeBetweenRides)+timedelta(minutes=wt)
        jobList.append(Job(timeOfDay, endTime, vals[0], name, timeBetweenRides))
        jobList.append(Job(timeOfDay, endTime, vals[1], name+'2', timeBetweenRides))
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
  return result, timeList

if __name__ == "__main__":
  arrive = {'h': 10, 'mi': 0}
  depart = {'h': 20, 'mi': 50}
  doy = {'y': 2022, 'mo': 4, 'd': 22}
  if True:
    timeBetweenRides = 30
    plans = plan(arrive, depart, doy, timeBetweenRides, rideVals)
    # for ride in plans:
    #   print(ride)
    # print('Total value: {}'.format(sum(map(lambda x: x.val, plans))))
