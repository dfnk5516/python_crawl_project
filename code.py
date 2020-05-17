import json
import urllib.request as req
from fake_useragent import UserAgent
import urllib.parse
import csv

ua = UserAgent()

headers = {
    'User-Agent': ua.ie,
    'referer': 'https://map.naver.com/'
}

# params = urllib.parse.urlencode(values)
searchCode = '송파구 동물병원'
searchCount = '10'

# url = "https://map.naver.com/v5/api/search?caller=pcweb&query=%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&type=all&searchCoord=127.01148033142091;37.55424027601126&page=1&displayCount=20&isPlaceRecommendationReplace=true&lang=ko"
encodedSearchCode = urllib.parse.quote_plus(searchCode)
encodedSearchCount = urllib.parse.quote_plus(searchCount)
url = "https://map.naver.com/v5/api/search?caller=pcweb&query=" + encodedSearchCode + "&type=all&searchCoord=1;37.55424027601126&page=1&displayCount="+ encodedSearchCount +"&isPlaceRecommendationReplace=true&lang=ko"
print(url)

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

rank_json = json.loads(res)['result']
print()
print()
print()

hospitals = (rank_json['place'])['list']
print(hospitals)
print(type(hospitals))
from csv import DictWriter

newHospital = []
for v in hospitals:
    hospital = {'rank' : v['rank'], 'name' : v['name'], 'tel':v['tel'], 'address':v['address'], 'roadAddress' : v['roadAddress'], 'x':v['x'], 'y':v['y']}
    #hospital = {'index' : v['index'], 'rank' : v['rank'], 'name' : v['name'], 'tel':v['tel'], 'category' : v['category'], 'address':v['address'], 'roadAddress' : v['roadAddress'], 'abbrAddress' : v['abbrAddress'], 'x':v['x'], 'y':v['y']}
    #hospital = {'hospt_no' : v['rank'], 'hospt_nm' : v['name'], 'hospt_tel':v['tel'], 'hospt_address':v['address'], 'hospt_roadAddress' : v['roadAddress'], 'hospt_nigthCare' : v['abbrAddress'], 'x':v['x'], 'y':v['y']}
    print(hospital)
    newHospital.append(hospital)

print()
print()
print('newHospital', newHospital)
    

with open('spreadsheet.csv','w') as outfile:
    #writer = DictWriter(outfile, ('index','rank','name','tel','category','address','roadAddress','abbrAddress','x','y'))
    writer = DictWriter(outfile, ('rank', 'name', 'tel', 'address', 'roadAddress', 'x', 'y'))
    writer.writeheader()
    writer.writerows(newHospital)

