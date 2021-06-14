# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.xml")
soup = BeautifulSoup(page.content, 'xml')

element = soup.find_all('child')[2]
print(element)

element.name = "stepchild"
element["name"] = "Jess"
print(element)

element.string = "Tercera"
print(element)
file = open("nuevo.xml", "w")
file.write(str(soup))
file.close()