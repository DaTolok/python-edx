# Ejemplo 2
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.xml")
soup = BeautifulSoup(page.content, 'xml')

element = soup.find_all('child')[2]

element_text = element.text
print("element_text: \n", element_text)

element_contents = element.contents
print("element_contents: \n", element_contents)

element_attribute_name = element.get('name')
print("element_attribute_name: \n", element_attribute_name)