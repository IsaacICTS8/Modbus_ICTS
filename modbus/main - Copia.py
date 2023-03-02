from pyModbusTCP.client import ModbusClient
import requests  #Biblioteca de requisição
import serial #Biblioteca que ler a serial

def ler_a_serial() : 
  dados = serial.Serial('COM16',9600)

  return (str(dados.readline()))

def transforma_dados(dado_lido) :   #Funcao responsável por transformar os dados pro SCADA

  aux = []
  scada = []

  
  for i in dado_lido : #Guarda os dados decimais de forma hexadecimal
    aux.append(hex(ord(i)))


  tamanho = 0

  while tamanho<len(aux):

    if tamanho != len(aux)-1 :
        scada.append((aux[tamanho+1][2::])+(aux[tamanho][2::])) #Concatena pares de registros
    else :
        scada.append(aux[tamanho][2::])
    tamanho+=2 

  return scada

modbus_client = ModbusClient('172.16.18.243', unit_id=255, auto_open=True) 

modbus_client.open()

while(1) :

    dados = ler_a_serial()
    dados_trat = (dados[2:len(dados)-5])
    registro=16
    registro2=50

    if (len(dados)%2==1) : dados+=" "

    string = transforma_dados(dados_trat)  #Chama a função pra salvar os dados

    for letra in string :   
        
        modbus_client.write_single_register(registro,int(letra,16))
        registro+=1

    for letra in dados :   
        
        modbus_client.write_single_register(registro2,ord(letra))
        registro2+=1

    leitura = modbus_client.read_holding_registers(50,len(dados)) #Guarda numa lista os registros lidos

    for i in leitura :
      print(chr(i),end="")
    modbus_client.close() 