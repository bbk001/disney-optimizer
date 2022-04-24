import sys
from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
import os

sys.path.insert(0, 'flask-backend-api')
from planDay import getAllDayPredict, makeJobs
from orToolsILP import lpApprox

app = Flask(__name__, static_folder='disney-optimizer-frontend/build', static_url_path='/')
server = app.server
cors = CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api')
@cross_origin()
def test():
  return {'test':'string'}

@app.route('/api/requestRidePredict', methods=['POST'])
@cross_origin()
def requestRidePredict():
  print('Getting predicts')
  return getAllDayPredict(request.json['arrive'], request.json['depart'], request.json['doy'], request.json['rideDict'].keys())[1]

@app.route('/api/requestPlans', methods=['POST'])
@cross_origin()
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
