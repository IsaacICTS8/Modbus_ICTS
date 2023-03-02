import requests

api_url = "http://viacep.com.br/ws/69073620/json" #API CEP (Aqui vai a API do Williams)
response = requests.get(api_url)

print(response)