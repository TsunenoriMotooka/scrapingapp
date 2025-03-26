import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os
import urllib
import time

#ページを取得
load_url='https://joytas.net/kaba/'
res = requests.get(load_url)
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

print()

out_folder = Path('downloaded')
out_folder.mkdir(exist_ok=True)

for img in imgs:
    src = img.get('src')
    img_url = urllib.parse.urljoin(load_url, src)
    print(img_url)

    loaded_img = requests.get(img_url)

    file_name = src.split(os.sep)[-1]
    print(file_name)
    out_path = out_folder.joinpath(file_name)

    with open(out_path, "wb") as file:
        file.write(loaded_img.content)

    time.sleep(1)


