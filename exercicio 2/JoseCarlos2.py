from urllib import response
import urllib.request, json
import requests

cep = input("Informe um CEP EX:(12345-123):")

with urllib.request.urlopen(f"https://viacep.com.br/ws/{cep}/json/") as url:
    dados = json.loads(url.read().decode())

print('Estado: ' + dados['uf'])

if (dados['bairro'] != ""):
    print('Bairro: ' + dados['bairro'])

print('Cidade: ' + dados['localidade'])

if (dados['logradouro'] != ""):
    print('Rua: ' + dados['logradouro'])

print('DDD: ' + dados['ddd'])

API_KEY = '410dcc379e00ad1f291855fb43c6aa48'
cidade = dados['localidade']
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

req = requests.get(link)
nome = req.json()['name']
temperatura = req.json()['main']['temp'] - 273.15
descricao = req.json()['weather'][0]['description']
print(f'A temperatura em {nome} é de {temperatura}°C e o clima é {descricao}')
