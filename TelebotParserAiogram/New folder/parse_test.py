import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/review')
html = BS(r.content, 'html.parser')

smth = html.find(class_='_default-grid_1fhuj_203').find_all('div')
print(type(smth))
print(smth[0]['data-key'])
#print(smth[0].text.strip())
for x in smth:
	print(type(x))
	print(x['data-key'])
	print(x.find('article').get('aria-label'))
	print(x.find('a').get('href'))
	#for z in x.find_all('article'):
		#print(z.get('aria-label'))
	print('++++++++')
	print(x)
	print('----------------------------------------')


#smth = html.select('._main_1dnkd_218 > ._content_1fhuj_127 > .list-view > ._default-grid_1fhuj_203 > div:nth-child(1) > article:nth-child(1) > a:nth-child(1)')
#print(type(smth))
#for el in smth: #".items > .article-summary"
#	print(el)
	#title = el.select('.caption > a')

	#print(title[0].text)

#._default-grid_1fhuj_203 > div:nth-child(1)
#._default-grid_1fhuj_203 > div:nth-child(2)
#._default-grid_1fhuj_203 > div:nth-child(1) > article:nth-child(1) > a:nth-child(1)
	#html body main#main-content._main_1dnkd_218 section#catalog-content._content_1fhuj_127 div#w0.list-view div._default-grid_1fhuj_203
	#/html/body/main/section[2]/div[3]/div[1]
