from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
class Pars:
	def __init__(self):
		#city = self.get_location()
		#categ = self.get_categ(city)
		categ = 'https://m.avito.ru/kazan/komnaty'
		pages = self.get_pages(categ)
		self.get_elements(categ, pages)
		print('В выбраной категории '+str(pages)+' страниц')
	def connect_mysql:
		pass
	def load_data(self):
		pass
	def __driver(self):
		options = Options()
		options.add_argument("--headless")
		#headless браузер
		driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
		return driver
	def __driver_close(self,driver):
		driver.close()
	def get_data(self,url,driver):
		#метод получения номера
		urls =[]
		for Url in url:
			urls.append(Url.get_attribute('href'))
		for URL in urls:
			#URL.get_attribute('href')
			driver.get(URL)
		#поиск кнопки
			button = driver.find_element_by_xpath("//a[@title='Телефон продавца']")	
		#клик по кнопке
			button.click()
			answer = button.get_attribute('href')
			print(answer)
			time.sleep(40)
		#driver.close()
		#return answer
	def get_elements(self,url, pages):
		#метод получения ссылок объявлений на странице
		options = Options()
		options.add_argument("--headless")
		#headless браузер
		driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
		i = 1
		while i<=pages:
			URL= str(url) + '?p='+str(i)
			driver.get(URL)
			ads = driver.find_elements_by_xpath("//a[@class='item-link item-link-visited-highlight']")

			self.get_data(ads,driver)
	def get_pages(self, url):
		options = Options()
		options.add_argument("--headless")
		#headless браузер
		driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
		#получение списка регионов
		driver.get(url)
		try:
			#проверка на не нулевое количество объявлений
			pages = driver.find_element_by_xpath("//div[@class='nav-helper-content nav-helper-text']")
			pages = pages.text
			pages = pages.replace(' ', '')
			driver.close()
		
		
		except:
			print('В выбранной категории пусто!')
			driver.close()
			return 0
		if int(pages) <= 20:
			return 1
		if (int(pages)/20 + 1) > 100:
			return 100 
		else: 
			pages = int(pages)/20 + 1
			return int(pages)
	def get_location(self):
		options = Options()
		options.add_argument("--headless")
		#headless браузер
		driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
		#получение списка регионов
		driver.get('https://m.avito.ru/location')
		cityes = driver.find_elements_by_xpath("//a[@class='list-link']")
		
		#Выбор региона
		location = self.__loc(cityes)
		#проверка на ошибочный ввод
		if location == 1:
			return 1
		#проверка на пункт 'По всей России'
		if location == cityes[0].get_attribute('href'):
			return locations[location]
		
		else:
			driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
			driver.get(location)
			town = driver.find_elements_by_xpath("//a[@class='list-link']")
			city =  self.__loc(town, 0)
			driver.close()
			print('Вы выбрали город ' + str(city))
			return city
	def get_categ(self, city):
		#функция выбора категории
		options = Options()
		options.add_argument("--headless")
		#headless браузер
		driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
		#получение списка регионов
		driver.get(city)
		cityes = driver.find_elements_by_xpath("//a[@class='list-link']")
		location = self.__loc(cityes)
		if location == 1:
			return 1
		#проверка на пункт 'По всей России'
		if location == cityes[0].get_attribute('href'):
			return locations[location]
		
		else:
			driver = webdriver.Firefox(firefox_options=options,executable_path=r'E:\pythonPars\geck\geckodriver.exe')
			driver.get(location)
			town = driver.find_elements_by_xpath("//a[@class='list-link']")
			city =  self.__loc(town, 0)
			driver.close()
			print('Вы выбрали категорию ' + str(city))
			return city

	def __loc(self, elements, i = 1):
		#вспомагательная функция для выбора региона и категории
		locations = dict()
		for city in elements:
			if i !=0:
				print( str(i) + '. ' + city.get_attribute('text'))
				locations[str(i)] = str(city.get_attribute('href'))
			
			i = i+1
		location = input('Введите номер варианта: ')
		#проверка на ошибочный ввод
	
		if int(location) > i or int(location) <1:
			print("Ошибка ввода")
			return 1
		#ввод номера региона
		else:
			return locations[location]






parsing = Pars()
		

		
		

		
		

		
						#ans = parsing.get_number('https://m.avito.ru/sankt-peterburg/muzykalnye_instrumenty/gitara_1071824391')

						#print(get_number('https://m.avito.ru/sankt-peterburg/muzykalnye_instrumenty/gitara_1071824391'))
						#print(ans)
						#'https://m.avito.ru/sankt-peterburg/muzykalnye_instrumenty/gitara_1071824391'