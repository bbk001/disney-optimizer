from datetime import timedelta

class Job:
  def __init__(self, startTime, endTime, value, ride, timeBetweenRides):
    self.start = startTime
    self.end = endTime
    self.val = value
    self.ride = ride
    self.tbr = int(timeBetweenRides)
  
  def __str__(self) -> str:
    startRide = self.start.strftime('%H:%M')
    endRide = (self.end - timedelta(minutes=self.tbr)).strftime('%H:%M')
    return 'Ride {} at {} until {} for a value of {}'.format(self.ride, startRide, endRide, self.val)
  
  def toJSon(self):
    startRide = self.start.strftime('%H:%M')
    endRide = (self.end - timedelta(minutes=self.tbr)).strftime('%H:%M')
    return {'rideName': self.ride, 'startTime': startRide, 'endTime': endRide, 'value': self.val}