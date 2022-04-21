from thrillDataScrape import getWaitTimePredict
from greedyAlpha import greedyAlpha
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
  return greedyAlpha(jobList)

class Job:
  def __init__(self, startTime, endTime, value, ride):
    self.start = startTime
    self.end = endTime
    self.val = value
    self.ride = ride

def makeJobs(arrive, rideWaitTimes, timeBetweenRides, valueList):
  jobList = []
  for name, waitTimes, vals in zip(rideList, rideWaitTimes, valueList):
    timeOfDay = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
    for wt in waitTimes:
      if wt:
        endTime = timeOfDay+timedelta(minutes=timeBetweenRides)+timedelta(minutes=wt)
        jobList.append(Job(timeOfDay, endTime, vals[0], name))
        jobList.append(Job(timeOfDay+timedelta(seconds=1), endTime+timedelta(seconds=1), vals[1], name+'2'))
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
  arrive = {'h': 8, 'mi': 0}
  depart = {'h': 23, 'mi': 50}
  doy = {'y': 2022, 'mo': 4, 'd': 22}
  if True:
    timeBetweenRides = 30
    plans = plan(arrive, depart, doy, timeBetweenRides, rideVals)
    for ride in plans:
      startRide = ride.start.strftime('%H:%M')
      endRide = (ride.end - timedelta(minutes=timeBetweenRides)).strftime('%H:%M')
      print('Ride {} at {} until {} for a value of {}'.format(ride.ride, startRide, endRide, ride.val))
    print('Total value: {}'.format(sum(map(lambda x: x.val, plans))))
  else:
    result, timeList = getAllDayPredict(arrive, depart, doy)
    x = list(map(lambda dt: dt.strftime('%H:%M'), timeList))
    for line, ride in zip(result, rideList):
      plt.plot(x, line, label=ride[:5])
    plt.xticks(x[::6])
    plt.legend()
    plt.show()
