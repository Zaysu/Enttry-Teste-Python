import csv
import requests
from bs4 import BeautifulSoup

page = requests.get('https://enttry.com.br/contato')
soup = BeautifulSoup(page.content, 'html.parser')


csv_file = open('links.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['id','link'])

id = 0
armazenamento = soup.find_all('link', rel='stylesheet')
for i in armazenamento:
    print(i)
    csv_writer.writerow([id, i])
    id+=1

csv_file.close()