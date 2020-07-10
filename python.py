from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def convertUrl(url):
    soup = bs(urlopen(url), 'lxml')
    return soup

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
soup = convertUrl(url)
soup = soup.find(id='R01200')#ищем элемент по ID в XML
charcode = soup.find('charcode').text#Извлекаем краткое название валюты
toRub = float(soup.find('value').text.replace(',','.'))/float(soup.find('nominal').text)#извлекаем каличество у.е и стоимость и пересчитываем на одну единицу
print('Символьный код валюты: {}'.format(charcode))
print('1 {} стоит {} RUB'.format(charcode,toRub))

"""
Примерный вывод:


Символьный код валюты: HKD
1 HKD стоит 9.19059 RUB


"""
