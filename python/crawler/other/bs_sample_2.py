from bs4 import BeautifulSoup

f = open('sample2.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'lxml')

webtoon_table = soup.select_one('table.viewlist')
print(webtoon_table)

tr_list = webtoon_table.find_all('tr', recursive=False)
for tr in tr_list:
    td_title = tr.select_one('td.title')
