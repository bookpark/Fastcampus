from bs4 import BeautifulSoup

f = open('sample.txt', 'rt')
source = f.read()
soup = BeautifulSoup(source, 'html.parser')

result = soup
print(result)