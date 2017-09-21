import requests
from bs4 import BeautifulSoup

webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=wed'

response = requests.get(webtoon_url)
source = response.text
soup = BeautifulSoup(source, 'lxml')


with open('sample.txt', 'wt') as f:
    f.write(soup.prettify())
