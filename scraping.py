import requests
from bs4 import BeautifulSoup

#ページを取得
res = requests.get('https://joytas.net/kaba/')
res.encoding = res.apparent_encoding

#取得したページからhtml全体を取得
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)

element = soup.find('title')
print(element.text)

imgs = soup.find_all('img')
for img in imgs:
    print(img.get('src'))

div = soup.find(id='headerImageBox')
imgs = div.select('.headerImage')
for img in imgs:
    print(img.get('src'))

print()

main = soup.find('main')
names = main.select('table tbody tr td:first-child')
for name in names:
    print(name.text)

print()

ul = main.select_one('ul')
links = ul.select('li a')

with open('zoo.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write(f'{link.text}:{link.get("href")}\n')
        print(f'{link.text}:{link.get('href')}')

