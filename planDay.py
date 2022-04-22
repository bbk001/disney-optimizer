from thrillDataScrape import getWaitTimePredict
from greedyAlpha import greedyAlpha
# from lpApprox import lpApprox
from orToolsILP import lpApprox
from datetime import datetime
from datetime import timedelta
import argparse



rideDict = {
  'bigthundermountainrailroad': (70,50,40),
  'starwarsriseoftheresistance': (110,60,50),
  'spacemountain': (100,75,65),
  'splashmountain': (75,55,45),
  'millenniumfalconsmugglersrun': (80,40,30),
  'matterhornbobsleds': (72,55,45),
  'indianajonesadventure': (70,45,35),
  'buzzlightyearastroblasters': (52,45,40),
  'startourstheadventurescontinue': (45,35,25),
  'junglecruise': (45,35,25),
  'mrtoadswildride': (35,20,10),
  'autopia': (40,25,15),
  'hauntedmansion': (55,45,30),
  'piratesofthecaribbean': (55,45,30),
  'snowwhitesenchantedwish': (30,15,10),
  'storybooklandcanalboats': (20,10,5),
  'themanyadventuresofwinniethepooh': (25,10,5),
  'pinocchiosdaringjourney': (30,15,10),
  'peterpansflight': (35,20,10),
  'madteaparty': (15,5,1),
  'kingarthurcarrousel': (15,5,1),
  'dumbotheflyingelephant': (15,5,1),
  'caseyjrcircustrain': (20, 10, 5),
  'astroorbitor': (20,10,5),
  'aliceinwonderland': (25,10,5),
  'itsasmallworld': (30,15,10)
}

rideList = rideDict.keys()
rideVals = rideDict.values()

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
        jobList.append(Job(timeOfDay, endTime, vals[2], name+'3', timeBetweenRides))
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
  if True:
    plans = plan(arrive, depart, doy, args.timeBetweenRides, rideVals)
    # for ride in plans:
    #   print(ride)
    # print('Total value: {}'.format(sum(map(lambda x: x.val, plans))))
