# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.xml")
soup = BeautifulSoup(page.content, 'xml')

result = soup.find_all('data')
print(result)

result = soup.find_all('unique')
print(result)

result = soup.find_all('parent')
print(result)