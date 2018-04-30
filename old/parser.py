import requests
from bs4 import BeautifulSoup
#class pars:
	#def __init__(self):
#	def get_page(self):
		#метод получения главной страницы
#		page = request.get("https://www.avito.ru")
page = requests.get("https://www.avito.ru")
soup = BeautifulSoup(page.text , 'lxml')
cat = soup.findAll('a', class_='js-catalog-counts__link')
for ans in cat:
	print(ans['href'])
