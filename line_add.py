

#LINEトークンを取得する
token = "hSwmjvbwtUel1nLdaqIvyfh8lw7yASYvlyRsbsyVEGG"
#APIドキュメント　通知系
url = "https://notify-api.line.me/api/notify"

import requests

#pip install BeautifulSoup4 をインストール WEB上のHTMLの情報を取得する
from bs4 import BeautifulSoup

tenki_url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
response = requests.get(tenki_url)

#htmlを見やすくする
html = BeautifulSoup(response.text,"html.parser")
#htmlの天気予報の箇所を取得 リスト表示されるのでそれの０番目
forecast = html.find_all("div",attrs={"class":"forecastCity"})[0]
#明日の天気予報の箇所を取得
tomorror = forecast.find_all("div")[1]
#天気取得
weather = tomorror.find_all("p",attrs={"class":"pict"})[0].text.replace("\n","").replace("","")
#最低気温最高気温取得
high = tomorror.find_all("li")[0].text
low = tomorror.find_all("li")[1].text
#降水確率
rain_0006 = tomorror.find_all("td")[4].text
rain_0612 = tomorror.find_all("td")[5].text
rain_1218 = tomorror.find_all("td")[6].text
rain_1824 = tomorror.find_all("td")[7].text

message ="""
明日の天気は{}
最高気温は{}
最低気温は{}
降水確率は
0-6時:{}
6-12時:{}
12-18時:{}
18-24時:{}
です""".format(weather,high,low,rain_0006,rain_0612,rain_1218,rain_1824)


#辞書の形でdataは通知したい内容を記載する　authは鍵の書き方。APIによって書き方は異なる。
#この時点で通知がいく
auth = {"Authorization":"Bearer "+token}
content = {"message":message}
requests.post(url,headers=auth,data=content)
