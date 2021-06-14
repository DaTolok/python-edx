# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

print("soup.children:", list(soup.children), "\n")
html = list(soup.children)[2]
print("html:", html, "\n")
body = list(html.children)[3]
print("body:", body, "\n")
p = list(body.children)[1]
print("text:", p.get_text())