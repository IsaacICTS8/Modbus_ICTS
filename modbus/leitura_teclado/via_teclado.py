from pyModbusTCP.client import ModbusClient
from pymodbus.client import ModbusTcpClient
import requests
import codecs

def transforma_dados(dado_lido) :   #Funcao responsável por transformar os dados pro SCADA

  aux = []
  scada = []

  for i in dado_lido : 
    aux.append(hex(ord(i)))   # Adiciona numa lista auxiliar os valores hexadecimais dos decimais correspondentes às letras

  tamanho = 0

  while tamanho<len(aux):

    if tamanho != len(aux)-1 :
        scada.append((aux[tamanho+1][2::])+(aux[tamanho][2::]))   #Une os registros para serem escritos em um único registro no CLP
    else :
        scada.append(aux[tamanho][2::])
    tamanho+=2 

  return scada

modbus_client = ModbusClient('172.16.18.243', unit_id=255, auto_open=True) 

modbus_client.open()

while(1) :
  dados = input("\ncodigo : ")

  registro=16

  string = transforma_dados(dados)  #Chama a função pra salvar os dados

  print(string)

  for letra in string :   
      
      modbus_client.write_single_register(registro,int(letra,16))
      registro+=1

  leitura = modbus_client.read_holding_registers(50,len(dados)) #Guarda numa lista os registros lidos

  for i in leitura :
    print(chr(i),end="")     
  modbus_client.close() 