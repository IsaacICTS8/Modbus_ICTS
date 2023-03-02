from pyModbusTCP.client import ModbusClient
# from pymodbus.client import ModbusTcpClient
import requests

# Parte que faz a requisição da web
api_url = "https://viacep.com.br/ws/69073620/json/" #API CEP (Aqui vai a API do Williams)
response = requests.get(api_url)
dict = response.json()

bairro = dict['bairro']  #D100
ddd = dict['ddd'] #D200
localidade = dict['localidade']  #D300

modbus_client = ModbusClient('172.16.18.243', unit_id=255, auto_open=True)

modbus_client.open()

parametros = [bairro,ddd,localidade]

# string in the list

cont = 100
aux=1
for item in parametros:
    for j in item :
        modbus_client.write_multiple_registers(cont,[ord(str(j))])   #Escreve a mensagem no clp
        cont+=1
    aux+=1
    cont = 100*aux

cont = 100

lista_de_leituras = []

for item in parametros :
    lista_de_leituras.append(modbus_client.read_holding_registers(cont,len(item))) #Guarda numa lista os registros lidos
    cont+=100 

print(lista_de_leituras)

modbus_client.close() 
  