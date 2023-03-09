def impressao(leitura):
  # Endereço IP da impressora
    ip = "192.168.3.30"

    # Comando ZPL para imprimir a palavra Renato
    zpl = "^XA^FO50,50^A0N,50,50^FD"+(leitura)+"^FS^XZ"

    # Cria um objeto socket e conecta à impressora
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 9100))

    # Envia o comando ZPL para a impressora
    s.send(bytes(zpl, "utf-8"))

    # Fecha a conexão com a impressora
    s.close()



from pyModbusTCP.client import ModbusClient
import socket
import time

modbus_client = ModbusClient('192.168.3.3', unit_id=255, auto_open=True) 
estado = 5

modbus_client.open()

while(1):

  statusDaLeitura = modbus_client.read_holding_registers(2,1)
  if statusDaLeitura[0] != estado:
    
    estado = modbus_client.read_holding_registers(2,1)[0]
  
    if estado == 0:
        print("ok")
        impressao("ok")
        time.sleep(1)
        estado = 0


    else:
      print("ng")
      time.sleep(1)
      estado = 1
      impressao("ng")
