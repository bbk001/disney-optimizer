from flask import Flask
from defaultRideDict import rideDict
from planDay import plan

app = Flask(__name__)

rideList = rideDict.keys()
rideVals = rideDict.values()

@app.route('/test')
def test():
  return {'test':'string'}

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