# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

for item, element in enumerate(soup.descendants):
	print("Element {}: \n {}".format(item, element))