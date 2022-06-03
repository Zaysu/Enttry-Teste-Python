import requests
import pickle
import json
from bs4 import BeautifulSoup

page = requests.get('https://enttry.com.br/contato')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find('meta', attrs={'name': 'description'})['content'])

arquivo = open("text.json", "a")
save = list() 
save.append(soup.find('meta', attrs={'name': 'description'})['content'])
arquivo.writelines(json.dumps(save))
