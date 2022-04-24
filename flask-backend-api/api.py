from flask import Flask, request
from planDay import getAllDayPredict, makeJobs
from orToolsILP import lpApprox
import os

app = Flask(__name__, static_folder='../disney-optimizer-frontend/build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/test')
def test():
  return {'test':'string'}

@app.route('/requestRidePredict', methods=['POST'])
def requestRidePredict():
  print('Getting predicts')
  return getAllDayPredict(request.json['arrive'], request.json['depart'], request.json['doy'], request.json['rideDict'].keys())[1]

@app.route('/requestPlans', methods=['POST'])
def requestPlans():
  print('Getting plans')
  rideWaitTimes = request.json['rideWaitTimes']
  arrive = request.json['arrive']
  depart = request.json['depart']
  jobList = makeJobs(arrive, depart, rideWaitTimes, request.json['tbr'], request.json['rideDict'])
  result = lpApprox(jobList, arrive, depart, request.json['rideDict'].keys())
  print('Got plans')
  return {'planList': result}

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
