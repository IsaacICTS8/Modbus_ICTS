from pyModbusTCP.client import ModbusClient

def signed_to_unsigned(num):
    # Verifica se o número é negativo
    is_negative = num

    # Calcula o complemento de dois, se necessário
    if is_negative:
        num = (1 << 16) + num

    # Converte o número para binário e adiciona zeros à esquerda
    binary = bin(num & 0xffff)[2:].zfill(16)

    # Inverte os bits, se necessário
    if is_negative:
        binary = bin(~int(binary, 2) & 0xffff)[2:].zfill(16)

    # Converte o número de volta para decimal
    unsigned = int(binary, 2)

    # Adiciona 1, se necessário
    if is_negative:
        unsigned += 1

    return unsigned


modbus_client = ModbusClient('192.168.1.5', unit_id=255, auto_open=True)

modbus_client.open()

# string in the list

while(1) :

    valor = (modbus_client.read_holding_registers(424,1))[0] #Guarda numa lista os registros lidos

    numero = (modbus_client.read_holding_registers(139,1))[0] #Registro

    if numero==0 :

     print(valor)

    else :
    
     print(valor*(-1))
