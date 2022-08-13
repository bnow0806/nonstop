#rgba(255, 255, 255, .5);


from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('계정 입력')
db = client.dbsparta

import json

Preview_Dict = dict()

url_recieve = "https://playvod.imbc.com//api/PreviewList?programId=1000327100000100000&curPage=1&pageSize=1"
url_recieve_2 = "https://playvod.imbc.com//api/PreviewList?programId=1000327100000100000&curPage=2&pageSize=1"

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url_recieve,headers=headers, verify=False)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

#detail_area

#print(soup)
#description = soup.select_one("#detail_area")

#2004년 10월 1일 (금) / 제 251 회<논스톱4 하이라이트 제 2 편>‘욕망이라는 이름의 뮤직비디오’ 편을 보내드립니다!
#print(description.text)

#페이지 주소 바뀌게??
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#vodSection > ul > li:nth-child(14) > a > div > p
#vodSection > ul > li:nth-child(38) > a > div > p
#movies = soup.select('#json > ul > li')
#p_tag=movies.selct_one('a > div > p')

#print(soup.text)
# a=soup.text.split(" ")
# print(a)
#https://playvod.imbc.com//api/PreviewList?programId=1000327100000100000&curPage=1&pageSize=1

#json > ul > li:nth-child(1) > div > ul > li > div > ul > li:nth-child(9) > div > span.type-string

json_string = requests.get(url_recieve,headers=headers, verify=False).text
data_list = json.loads(json_string)
#print(data_list['ContList'][0]['Preview'])


for page in range(1,252):   #1~251
    url_raw = "https://playvod.imbc.com//api/PreviewList?programId=1000327100000100000&curPage="+str(page)+"&pageSize=1"
    #print(url_raw)
    json_string = requests.get(url_raw, headers=headers, verify=False).text
    data_list = json.loads(json_string)
    #print(data_list['ContList'][0]['ContentNumber'],data_list['ContList'][0]['Preview'])

    ContentNumber_temp=int(data_list['ContList'][0]['ContentNumber'])   #정렬을 위한 key값 정수화
    Preview_temp=data_list['ContList'][0]['Preview']

    # data cleansing
    Preview_temp=Preview_temp.split("\r\n\r\n")[1]

    Preview_Dict[ContentNumber_temp] = Preview_temp

#print(Preview_Dict)

sort_Preview_Dict = dict(sorted(Preview_Dict.items()))
#print(sort_Preview_Dict)

#DB에 저장
for key, value in sort_Preview_Dict.items():

    doc = {'ContentNumber': str(key),       #정렬 후 key값 문자화
            'Preview': value,
               }
    print(doc)
    #db.preview.insert_one(doc)
