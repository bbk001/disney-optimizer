import numpy as np
from datetime import timedelta
from datetime import datetime
from ortools.sat.python import cp_model

def lpApprox(jobsSorted, arrive, depart, rideList):
  model = cp_model.CpModel()
  dayStart = datetime(2022, 4, 22, arrive['h'], arrive['mi'])
  dayEnd = datetime(2022, 4, 22, depart['h'], depart['mi'])
  fullMatListT=[]
  objectiveVecList=[]
  vars = {}
  for job in jobsSorted:
    if (job.end-timedelta(minutes=int(job.tbr)*0.8))<=dayEnd:
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
        if name+'2'==job.ride:
          columnVec.append(newVar)
        else:
          columnVec.append(0)
      for name in rideList:
        if name+'3'==job.ride:
          columnVec.append(newVar)
        else:
          columnVec.append(0)
      fullMatListT.append(columnVec)
  fullMatList = list(zip(*fullMatListT))
  for row in fullMatList:
    model.Add(sum(row)<=1)
  model.Maximize(sum(map(lambda tup:tup[0]*tup[1],objectiveVecList)))
  solver = cp_model.CpSolver()
  status = solver.Solve(model)
  rides = []
  if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for var in vars.keys():
      if solver.Value(var)==1:
        rides.append(vars[var].toJSon())
  else:
    print('No solution found.')
  return rides

    
