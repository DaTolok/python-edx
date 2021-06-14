# Ejemplo 1
import requests
from bs4 import BeautifulSoup

page = requests.get("https://datolok.github.io/python-edx/webscrapping/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

all_p_tags = soup.find_all('p')
print("all_p_tags: ", all_p_tags)

all_p_class_tags = soup.find_all('p', class_='outer-text')
print("all_p_class_tags: ", all_p_class_tags)

all_class_tags = soup.find_all(class_='outer-text')
print("all_class_tags: ", all_class_tags)

id_tag = soup.find_all(id='first')
print("id_tag: ", id_tag)