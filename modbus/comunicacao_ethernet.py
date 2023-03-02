from cpppo.server.enip.get_attribute import proxy_simple

# Endereço IP do controlador
plc_ip = '172.16.18.235'

# Path do tag que desejamos ler/escrever
tag_path = 'D20'

# Realizar a leitura do valor do tag
data = proxy_simple(plc_ip, tag_path)

# Imprimir o valor lido
print(data)

# Escrever um novo valor no tag
new_value = 1
proxy_simple(plc_ip, tag_path, value=new_value)

# Realizar a leitura do valor atualizado
updated_data = proxy_simple(plc_ip, tag_path)

# Imprimir o novo valor lido
print(updated_data)