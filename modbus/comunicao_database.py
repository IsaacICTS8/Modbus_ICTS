from pyModbusTCP.client import ModbusClient
from pymodbus.client import ModbusTcpClient
import requests,sqlite3

# Parte que faz a requisição da web

def transforma_dados(dado_lido) :   #Funcao responsável por transformar os dados pro SCADA

  aux = []
  scada = []
  scada_total = {}

  for item in dado_lido :
    for i in item : #Guarda os dados decimais de forma hexadecimal
      aux.append(hex(ord(i)))

    tamanho = 0

    while tamanho<len(aux):

      if tamanho != len(aux)-1 :
          scada.append((aux[tamanho+1][2::])+(aux[tamanho][2::])) #Concatena pares de registros
      else :
          scada.append(aux[tamanho][2::])
      tamanho+=2 
    scada_total[item] = scada
    aux = []
    scada = []
    
  return scada_total

consulta_post = []  # List of users

modbus_client = ModbusClient('172.16.18.243', unit_id=255, auto_open=True)

modbus_client.open()  

con = sqlite3.connect('test.sdb')
cursor = con.cursor()

for row in cursor.execute('SELECT * FROM pessoas'):
    consulta_post.append(row[0])

con.close()
  ###  CONSULTA NO BANCO DE DADOS DELES

while (1) :
  if (modbus_client.read_coils(8)==[1]) : ## Botao de confirmacao no SCADA

    leitura = modbus_client.read_holding_registers(60,4) #Guarda numa lista os registros lidos

    for i in range(0,len(leitura)):
      leitura[i] = hex(leitura[i])[2::]

    testador = transforma_dados(consulta_post) ## Consulta do banco de dados

    if (leitura in testador.values()) :

      modbus_client.write_single_coil(7,1)
      modbus_client.write_single_coil(9,0)
      print("Retorno de Apto")

    else :

      modbus_client.write_single_coil(7,0)
      modbus_client.write_single_coil(9,1)
      print("Retorno de negado")


  else : 

    modbus_client.write_single_coil(7,0)
    modbus_client.write_single_coil(9,0)


modbus_client.close() 

