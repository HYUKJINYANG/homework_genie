import requests
from bs4 import BeautifulSoup

#res=requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#resjson=res.json()
#print(resjson['RealtimeCityAir']['row'][0]['NO2'])

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#print(soup.select('title')[0].get_text())
#print(soup.select_one('title').get_text())
#print(soup.select_one('title').string)
#print(soup.select('.list_ranking tr>td.title a'))
#############################
# (입맛에 맞게 코딩)
#############################
list=soup.select('.list-wrap > tbody > tr')
rank=1
for item in list:
    title=item.select_one('a.title.ellipsis')
    singer=item.select_one('a.artist.ellipsis')
    if title is not None:
        print(rank, title.string, singer.string)
        rank+=1