import requests
from bs4 import BeautifulSoup
#class pars:
	#def __init__(self):
#	def get_page(self):
		#метод получения главной страницы
#		page = request.get("https://www.avito.ru")
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
page = requests.get("https://www.avito.ru",headers = headers)
soup = BeautifulSoup(page.text , 'lxml')
#cat = soup.findAll('a', class_='js-catalog-counts__link')
#'div', {'class': 'nameRus'}).find('a').get('href'
cat = soup.find[0](('div', {'class': 'catalog-counts__row clearfix'}).find('a').get('href'))
for ans in cat:
	print(ans)
