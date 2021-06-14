# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.xml")
soup = BeautifulSoup(page.content, 'lxml')
print(soup.prettify())