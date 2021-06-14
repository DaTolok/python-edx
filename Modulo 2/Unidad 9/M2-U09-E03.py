# Ejemplo 3
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

for p in soup.find_all("p"):
    if p.get("class") and "outer-text" in p.get("class"):
        print(p.get("class"),p.get_text())