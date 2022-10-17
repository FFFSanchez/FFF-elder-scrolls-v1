import requests
import re
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/review')
html = BS(r.content, 'html.parser')



items = html.select('._default-grid_1fhuj_203 > div > article > a')  # > .items > .item > a')

print(items[0]['href']) 


def parse_href(href):
	result = re.search(r'/show/(\d+)', href)
	return result.group(1)

print(parse_href('https://stopgame.ru/show/130658/grounded_review'))


link = 'https://stopgame.ru/show/130715/the_legend_of_heroes_trails_from_zero_my_zrya_propustili'
r1 = requests.get(link)
html1 = BS(r1.content, 'html.parser')

# parse poster image url
print(html1.select('div._image-wrapper_43hn6_90:nth-child(6) > a')[0]['href'])

img = html1.select('._gallery__content_43hn6_268 > div:nth-child(1) > a:nth-child(1) > picture:nth-child(1) > img:nth-child(3)')[0]['src']
print(f'img = {img}')

title = html1.select('h1')
print(f'title = {title[0].text}')

excep = html1.select('p._text_43hn6_35:nth-child(1)')
print(f'excep = {excep[0].text[:200]}...')

#poster = re.match(r'background-image:\s*url\((.+?)\)', html1.select('div._image-wrapper_43hn6_90:nth-child(6) > a'))#[0][style])
#print(poster) 
#parse_href(items[0]['href'])

#._gallery__content_43hn6_268 > div:nth-child(1) > a:nth-child(1) > picture:nth-child(1) > img:nth-child(3)
