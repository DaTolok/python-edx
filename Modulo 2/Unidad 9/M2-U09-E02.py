# Ejemplo 2
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

for p in soup.find_all("p"):
    if "contenido" in p.get_text():
        print(p.get_text())