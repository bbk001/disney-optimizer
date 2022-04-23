from flask import Flask, request
from defaultRideDict import rideDict
from planDay import plan, getAllDayPredict, makeJobs
from orToolsILP import lpApprox

app = Flask(__name__)

rideList = rideDict.keys()
rideVals = rideDict.values()

@app.route('/test')
def test():
  return {'test':'string'}

@app.route('/requestRidePredict', methods=['POST'])
def requestRidePredict():
  print('Getting predicts')
  return getAllDayPredict(request.json['arrive'], request.json['depart'], request.json['doy'])[1]

@app.route('/requestPlans', methods=['POST'])
def requestPlans():
  print('Getting plans')
  rideWaitTimes = request.json['rideWaitTimes']
  arrive = request.json['arrive']
  depart = request.json['depart']
  jobList = makeJobs(arrive, depart, rideWaitTimes, request.json['tbr'], rideDict)
  result = lpApprox(jobList, arrive, depart)
  print('Got plans')
  return {'planList': result}

@app.route('/default')
def default():
  print("called")
  arrive = {'h': 8, 'mi': 0}
  depart = {'h': 23, 'mi': 50}
  doy = {'y': 2022, 'mo': 4, 'd': 22}
  timeBetweenRides = 30
  plans = plan(arrive, depart, doy, timeBetweenRides, rideVals)
  print('planned')
  return {'planList': plans}