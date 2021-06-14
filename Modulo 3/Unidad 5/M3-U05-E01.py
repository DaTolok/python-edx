# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.xml")
soup = BeautifulSoup(page.content, 'xml')

element = soup.find_all('child')[2]

element_parent = element.parent
print("element_parent:\n", element_parent)

element_children = element.children
print("element_children:\n", element_children)

element_prev_siblings = element.previous_siblings
print("element_prev_siblings:\n", element_prev_siblings)

element_next_siblings = element.next_siblings
print("element_next_siblings:\n", element_next_siblings)