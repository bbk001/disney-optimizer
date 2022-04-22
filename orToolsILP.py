import numpy as np
from datetime import timedelta
from datetime import datetime
from ortools.sat.python import cp_model

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
  model = cp_model.CpModel()
  dayStart = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
  dayEnd = datetime(2022, 4, 22, depart['h'], depart['mi'])
  fullMatListT=[]
  objectiveVecList=[]
  vars = {}
  for job in jobsSorted:
    currentTime = dayStart
    columnVec=[]
    newVar = model.NewIntVar(0, 1, job.ride+job.start.strftime('%H:%M'))
    vars[newVar] = job
    objectiveVecList.append((job.val, newVar))
    while currentTime<=dayEnd+timedelta(minutes=60):
      if job.start<=currentTime and job.end>=currentTime:
        columnVec.append(newVar)
      else:
        columnVec.append(0)
      currentTime+=timedelta(minutes=10)
    for name in rideList:
      if name==job.ride:
        columnVec.append(newVar)
      else:
        columnVec.append(0)
    for name in rideList:
      if name==job.ride[:-1]:
        columnVec.append(newVar)
      else:
        columnVec.append(0)
    fullMatListT.append(columnVec)
  fullMatList = list(zip(*fullMatListT))
  for row in fullMatList:
    model.Add(sum(row)<=1)
  model.Maximize(sum(map(lambda tup:tup[0]*tup[1],objectiveVecList)))
  solver = cp_model.CpSolver()
  print('Ready to solve...')
  status = solver.Solve(model)
  if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'Maximum of objective function: {solver.ObjectiveValue()}\n')
    for var in vars.keys():
      if solver.Value(var)==1:
        print(vars[var])
  else:
    print('No solution found.')

    
