from thrillDataScrape import getWaitTimePredict
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


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
  doy = {'y': 2022, 'mo': 4, 'd': 21}
  result, timeList = getAllDayPredict(arrive, depart, doy)
  x = list(map(lambda dt: dt.strftime('%H:%M'), timeList))
  for line, ride in zip(result, rideList):
    plt.plot(x, line, label=ride[:5])
  plt.xticks(x[::6])
  plt.legend()
  plt.show()
