import requests
from bs4 import BeautifulSoup
import pandas as pd

cookies1 = {
    'usprivacy': '1YNY',
    'IR_gbd': 'laughingplace.com',
    'IR_MPI': 'd3838696-c11c-11ec-9a95-03c6d702c0f2%7C1650595407993',
    '_ga': 'GA1.2.1071468187.1650509009',
    '_gid': 'GA1.2.20004477.1650509009',
    'PHPSESSID': 'uetimm417nskr5ldm0jio5u4jh',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'cto_bidid': 'VtrlLV91RU9OSW9Ba2V4QTdMWnN6Y3FaUUd0a1EwbGljUmp6aFZhY2liZEVJT3FLbzE0bjBocFNNNGslMkJNNmVOM3Jsd0tpOWtDSlRrVmJSaW5QbE9vbzdIMk1QcXh3elBjMnlORDFBc1VuMHklMkZSNWx2V05DY1ZSTmF3R3BYdk1aczRTTXA',
    '__gads': 'ID=c86a7fd276143284:T=1650509026:S=ALNI_MYCGJI0HZTiQGLkf9fcEszsupXt6g',
    '__gpi': 'UID=000004a674e510ee:T=1650509026:RT=1650509026:S=ALNI_MZoOueYZJWmWWEUTxp7Qk82m9UVvA',
    '_lr_geo_location': 'US',
    'IR_MPS': '1650509075105%7C1650509007993',
    'cto_bundle': 'pCFltV9aQm81NHU0VEtweHZMTkE4akhzaHFCNXpYYmpNU0o1JTJGSnpnZiUyQkx1dyUyQmlpJTJCS3hFT2xwR1VhQzdsbUlpVjE5U05EWmdDVzZ3V1RVZDNLS04zaUd1MEFjOTd5UzE1ZlV3eUVsNk4lMkJpRnElMkZqcjllQTUzdWlGTlhLUUFKNkhNcHc4VDZqMFR6MUI5dzJib1RucGF3bmFiMWclM0QlM0Q',
}

headers1 = {
    'authority': 'www.laughingplace.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'usprivacy=1YNY; IR_gbd=laughingplace.com; IR_MPI=d3838696-c11c-11ec-9a95-03c6d702c0f2%7C1650595407993; _ga=GA1.2.1071468187.1650509009; _gid=GA1.2.20004477.1650509009; PHPSESSID=uetimm417nskr5ldm0jio5u4jh; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; cto_bidid=VtrlLV91RU9OSW9Ba2V4QTdMWnN6Y3FaUUd0a1EwbGljUmp6aFZhY2liZEVJT3FLbzE0bjBocFNNNGslMkJNNmVOM3Jsd0tpOWtDSlRrVmJSaW5QbE9vbzdIMk1QcXh3elBjMnlORDFBc1VuMHklMkZSNWx2V05DY1ZSTmF3R3BYdk1aczRTTXA; __gads=ID=c86a7fd276143284:T=1650509026:S=ALNI_MYCGJI0HZTiQGLkf9fcEszsupXt6g; __gpi=UID=000004a674e510ee:T=1650509026:RT=1650509026:S=ALNI_MZoOueYZJWmWWEUTxp7Qk82m9UVvA; _lr_geo_location=US; IR_MPS=1650509075105%7C1650509007993; cto_bundle=pCFltV9aQm81NHU0VEtweHZMTkE4akhzaHFCNXpYYmpNU0o1JTJGSnpnZiUyQkx1dyUyQmlpJTJCS3hFT2xwR1VhQzdsbUlpVjE5U05EWmdDVzZ3V1RVZDNLS04zaUd1MEFjOTd5UzE1ZlV3eUVsNk4lMkJpRnElMkZqcjllQTUzdWlGTlhLUUFKNkhNcHc4VDZqMFR6MUI5dzJib1RucGF3bmFiMWclM0QlM0Q',
    'if-modified-since': 'Thu, 21 Apr 2022 02:40:17 GMT',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

cookies2 = {
    'usprivacy': '1YNY',
    'IR_gbd': 'laughingplace.com',
    'IR_MPI': 'd3838696-c11c-11ec-9a95-03c6d702c0f2%7C1650595407993',
    '_ga': 'GA1.2.1071468187.1650509009',
    '_gid': 'GA1.2.20004477.1650509009',
    'PHPSESSID': 'uetimm417nskr5ldm0jio5u4jh',
    '_pbjs_userid_consent_data': '3524755945110770',
    '_lr_retry_request': 'true',
    '_lr_env_src_ats': 'false',
    'cto_bidid': 'VtrlLV91RU9OSW9Ba2V4QTdMWnN6Y3FaUUd0a1EwbGljUmp6aFZhY2liZEVJT3FLbzE0bjBocFNNNGslMkJNNmVOM3Jsd0tpOWtDSlRrVmJSaW5QbE9vbzdIMk1QcXh3elBjMnlORDFBc1VuMHklMkZSNWx2V05DY1ZSTmF3R3BYdk1aczRTTXA',
    '__gads': 'ID=c86a7fd276143284:T=1650509026:S=ALNI_MYCGJI0HZTiQGLkf9fcEszsupXt6g',
    '__gpi': 'UID=000004a674e510ee:T=1650509026:RT=1650509026:S=ALNI_MZoOueYZJWmWWEUTxp7Qk82m9UVvA',
    '_lr_geo_location': 'US',
    '__adblocker': 'true',
    'IR_MPS': '1650512218651%7C1650509007993',
    'cto_bundle': 'bwX52V9aQm81NHU0VEtweHZMTkE4akhzaHFDNlZQZyUyRkdpRDRKdTElMkZsd1VLRG13QXFiRXRSWUdQNTZtNHM2bldlZXlyZTZJTHJnTlYyVzNtWll6elpRemtEMTNLeUZldWdLTnJ3WE0yOTVveUdSU0tCd3NZNW1TVEwyTm5BR0FKNXdsbFdpYTBHOGJJMWlTb2s0dzNNaklGb0JnJTNEJTNE',
}

headers2 = {
    'authority': 'www.laughingplace.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'usprivacy=1YNY; IR_gbd=laughingplace.com; IR_MPI=d3838696-c11c-11ec-9a95-03c6d702c0f2%7C1650595407993; _ga=GA1.2.1071468187.1650509009; _gid=GA1.2.20004477.1650509009; PHPSESSID=uetimm417nskr5ldm0jio5u4jh; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; cto_bidid=VtrlLV91RU9OSW9Ba2V4QTdMWnN6Y3FaUUd0a1EwbGljUmp6aFZhY2liZEVJT3FLbzE0bjBocFNNNGslMkJNNmVOM3Jsd0tpOWtDSlRrVmJSaW5QbE9vbzdIMk1QcXh3elBjMnlORDFBc1VuMHklMkZSNWx2V05DY1ZSTmF3R3BYdk1aczRTTXA; __gads=ID=c86a7fd276143284:T=1650509026:S=ALNI_MYCGJI0HZTiQGLkf9fcEszsupXt6g; __gpi=UID=000004a674e510ee:T=1650509026:RT=1650509026:S=ALNI_MZoOueYZJWmWWEUTxp7Qk82m9UVvA; _lr_geo_location=US; __adblocker=true; IR_MPS=1650512218651%7C1650509007993; cto_bundle=bwX52V9aQm81NHU0VEtweHZMTkE4akhzaHFDNlZQZyUyRkdpRDRKdTElMkZsd1VLRG13QXFiRXRSWUdQNTZtNHM2bldlZXlyZTZJTHJnTlYyVzNtWll6elpRemtEMTNLeUZldWdLTnJ3WE0yOTVveUdSU0tCd3NZNW1TVEwyTm5BR0FKNXdsbFdpYTBHOGJJMWlTb2s0dzNNaklGb0JnJTNEJTNE',
    'if-modified-since': 'Thu, 21 Apr 2022 03:36:07 GMT',
    'referer': 'https://www.laughingplace.com/w/p/disneyland-current-wait-times/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

def process(time):
  if time == 'Open':
    return 10
  elif time == 'Closed':
    return 10000001
  elif time == 'Down':
    return 10000002
  elif time == 'Refurb':
    return 10000003
  else:
    try:
      return int(time[:-8])
    except:
      print(time)
      return 10000004

if __name__ == "__main__":
  response = requests.get('https://www.laughingplace.com/w/p/disneyland-current-wait-times/', headers=headers1, cookies=cookies1)
  html_string = response.text
  soup = BeautifulSoup(html_string, 'html.parser')
  waitTimesTable = soup.find_all('table')[0]
  data = {}
  for row in waitTimesTable.find_all('tr'):
    entries = row.find_all('td')
    data[entries[0].text] = process(entries[1].text)

  response = requests.get('https://www.laughingplace.com/w/p/disney-california-adventure-current-wait-times/', headers=headers2, cookies=cookies2)
  html_string = response.text
  soup = BeautifulSoup(html_string, 'html.parser')
  waitTimesTable = soup.find_all('table')[0]
  for row in waitTimesTable.find_all('tr'):
    entries = row.find_all('td')
    data[entries[0].text] = process(entries[1].text)
  
  df = pd.DataFrame([data])
  print(df)
