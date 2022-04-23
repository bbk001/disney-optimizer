import numpy as np
from datetime import timedelta
from scipy.optimize import linprog
from datetime import datetime

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

def lpApprox(jobsSorted, arrive, depart):
  dayStart = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
  dayEnd = datetime(2022, 4, 22, depart['h'], depart['mi'])
  fullMatList=[]
  objectiveVecList=[]
  for job in jobsSorted:
    objectiveVecList.append(0-job.val)
    currentTime = dayStart
    columnVec=[]
    while currentTime<=dayEnd:
      if job.start>=currentTime and job.end<=currentTime:
        columnVec.append(1)
      else:
        columnVec.append(0)
      currentTime+=timedelta(minutes=10)
    for name in rideList:
      if name==job.ride:
        columnVec.append(1)
      else:
        columnVec.append(0)
    for name in rideList:
      if name==job.ride[:-1]:
        columnVec.append(1)
      else:
        columnVec.append(0)
    fullMatList.append(columnVec)
  objectiveVec=np.array(objectiveVecList)
  fullMat=np.array(fullMatList).T
  constraintOnMat=np.ones(len(columnVec))
  result = linprog(c=objectiveVec, A_ub=fullMat, b_ub=constraintOnMat)
  for yn, jobToDo in zip(result.x, jobsSorted):
    if yn>0:
      print(yn, jobToDo)
  print(0-result.fun)

    
