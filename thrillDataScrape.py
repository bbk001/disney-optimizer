import requests
import json
from datetime import datetime
import numpy as np

cookies = {
    '_ga': 'GA1.2.1249345273.1650519651',
    '_gid': 'GA1.2.857145664.1650519651',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lr_geo_location': 'US',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'pbjs-unifiedid': '%7B%22TDID%22%3A%2255af3dd1-29f8-4005-ba60-97dc409a2c14%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-03-21T05%3A40%3A58%22%7D',
    'csrftoken': '3wFNgnAwnUgg9nZoujRPoXoQOvSoVBDudOnzVtAOWBalFmDrkrIJ8HW6s0D90uhv',
    'sessionid': 'z8b1i41rnv3f7ej0cpk8upxsjnag87pr',
    'session': 'ee39fe58-f585-4ead-b721-1b5b797b27c1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.2.1249345273.1650519651; _gid=GA1.2.857145664.1650519651; _pbjs_userid_consent_data=3524755945110770; _lr_geo_location=US; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%2255af3dd1-29f8-4005-ba60-97dc409a2c14%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-03-21T05%3A40%3A58%22%7D; csrftoken=3wFNgnAwnUgg9nZoujRPoXoQOvSoVBDudOnzVtAOWBalFmDrkrIJ8HW6s0D90uhv; sessionid=z8b1i41rnv3f7ej0cpk8upxsjnag87pr; session=ee39fe58-f585-4ead-b721-1b5b797b27c1',
    'Referer': 'https://www.thrill-data.com/waits/attraction/disneyland/bigthundermountainrailroad/graphs/current/ds/high',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

def getWaitTimePredict(ride, park='disneyland', dateTimesToCheck=[datetime.now()]):
  now = datetime.now()

  y = dateTimesToCheck[0].year
  mo = dateTimesToCheck[0].month
  d = dateTimesToCheck[0].day
  fullListOfLines = []
  forFuture = datetime(y, mo, d) > datetime(now.year, now.month, now.day)
  for tagOption in ['week', 'dow','hist']:
    params = {
        'park': park,
        'title': ride,
        'dateStart': '{}-{:02d}-{:02d}'.format(y,mo,d),
        'tag': tagOption,
    }
    response = requests.get('https://www.thrill-data.com/waits/graph/quick/rideavg', headers=headers, params=params, cookies=cookies)
    textLeft = response.text
    textLeft = textLeft[textLeft.find("Plotly.newPlot"):]
    textLeft = textLeft[textLeft.find("["):textLeft.find("]}],")+3]
    textLeft = textLeft.replace('\\','')
    if forFuture:
      asListOfLines = json.loads(textLeft)
    else:
      asListOfLines = json.loads(textLeft)[:-1]
    fullListOfLines += (asListOfLines)
  if not forFuture:
    params = {
      'park': park,
      'title': ride,
      'dateStart': '{}-{:02d}-{:02d}'.format(y,mo,d),
      'tag': 'daily',
    }
    response = requests.get('https://www.thrill-data.com/waits/graph/quick/rideavg', headers=headers, params=params, cookies=cookies)
    textLeft = response.text
    textLeft = textLeft[textLeft.find("Disney Forecast"):]
    textLeft = textLeft[textLeft.find("y\\\":["):]
    textLeft = textLeft[4:textLeft.find(",\\\"yaxis")]
    try:
      disneyForecasts = json.loads(textLeft)
    except:
      disneyForecasts = []
  lastYield = 100
  dForecastsRatio = 1
  for dateTimeToCheck in dateTimesToCheck:
    h = dateTimeToCheck.hour
    mi = int(dateTimeToCheck.minute/10)*10
    if int(h)<22 or forFuture:
      predictionList = []
      for line in fullListOfLines:
        waitTimeDict = dict(zip(map(lambda x: datetime.strptime(x[:-4]+'0', '%Y-%m-%dT%H:%M'), line['x']), line['y']))
        try:
          predictionList.append(waitTimeDict[datetime(y, mo, d, h, mi)])
        except:
          try:
            predictionList.append(waitTimeDict[datetime(y, mo, d, h, mi-10)])
          except:
            pass
      try:
        predictionList.sort()
        if len(predictionList)>2:
          lastYield = int(np.sqrt(np.mean(np.array(predictionList[1:-1])**2)))
          if len(disneyForecasts)>=15:
            dForecastsRatio = dForecastsRatio*0.98 + 0.02*(lastYield/disneyForecasts[int(h)-8])
        else:
          lastYield = lastYield*1.1
      except:
        lastYield = lastYield*1.1
    elif len(disneyForecasts)>0:
      lastYield = (disneyForecasts[-1] if int(h)>22 else disneyForecasts[-2])*dForecastsRatio
    else:
      lastYield = lastYield*0.9
    yield lastYield