#-------------------------------------------------------------------------------
# Name:    1_questão   
# Purpose: calculadora de sub-rede em Python
#
# Author:      20222014050020
#
# Created:     15/10/2024
# Copyright:   (c) 20222014050020 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
#solicitar um endereço IP, uma máscara de rede inicial e uma máscara de rede final.
print('')
print('** Bem-vindo a calculadora de sub-redes em Python **')
print('')
strIPAddress = input('Digite o endereço IP: ')
intMascara1  = input('Digite a máscarade rede inicial (CIDR): ')
intMascara2  = input('Digite a máscarade rede final (CIDR): ')
print('')
maskaras=[]
maskaras.append(intMascara1)
maskaras.append(intMascara2)

#try:
#validar IP para garantir que está no formato correto
partesIP = strIPAddress.split(".")
for parte in partesIP:
    if len(partesIP) != 4:
        print("Endereço IP inválido. Deve estar no formato XXX.XXX.XXX.XXX, onde XXX é um número entre 0 e 255.")
        break
    if not parte.isdigit():
        print("Endereço IP inválido. Deve estar no formato XXX.XXX.XXX.XXX, onde XXX é um número entre 0 e 255.")
        break
    if int(parte) < 0 or int(parte) > 255:
        print("Endereço IP inválido. Deve estar no formato XXX.XXX.XXX.XXX, onde XXX é um número entre 0 e 255.")
        break
#mascara
for mask in maskaras:
    if not mask.isdigit():
        print("Máscara de rede inválida. Deve ser um número entre 0 e 32.")
        break
    if int(mask) < 0 or int(mask) > 32:
        print("Máscara de rede inválida. Deve ser um número entre 0 e 32.")
        break
# Verificar se intMascara1 é menor que intMascara2
if int(intMascara1) > int(intMascara2):
    intMascara1, intMascara2 = intMascara2, intMascara1  # Trocar os valores

# lista que o for vai pegar para gerar cada cálculo    
CIDR = list(range(int(intMascara1), int(intMascara2) + 1))
	
#except Exception as e:
#sys.exit(f'\nERRO: {e}')
#else:
   # Convertendo o endereço IP em bytes
for intMascaraCIDR in CIDR:
    print(f'Para máscara: /{intMascaraCIDR} ')
    bytesIPAddress  = bytes([int(b) for b in strIPAddress.split('.')])

   # Convertendo os bytes do IP para um inteiro
    intIPAddress    = int.from_bytes(bytesIPAddress, 'big')

   # Calculando o endereço de rede com base na máscara CIDR   
    ipNETAddress    = (intIPAddress >> (32 - intMascaraCIDR)) << (32 - intMascaraCIDR)

   # Calculando a máscara de rede em formato inteiro
    intMascara      = ((1 << intMascaraCIDR) - 1) << (32 - intMascaraCIDR)                   
   # Calculando o endereço de broadcast
    intBroadcast    = ipNETAddress | (~intMascara & 0xFFFFFFFF)

   # Calculando o primeiro host
    intPrimeiroHost = ipNETAddress + 1

   # Calculando o último host
    intUltimoHost   = intBroadcast - 1
   #####
   # Convertendo os endereços para strings
    strNETAddress   = '.'.join(map(str, ipNETAddress.to_bytes(4, 'big')))
    strMascara      = '.'.join(map(str, intMascara.to_bytes(4, 'big')))
    strBroadcast    = '.'.join(map(str, intBroadcast.to_bytes(4, 'big')))
    strPrimeiroHost = '.'.join(map(str, intPrimeiroHost.to_bytes(4, 'big')))
    strUltimoHost   = '.'.join(map(str, intUltimoHost.to_bytes(4, 'big')))

   # Convertendo os endereços para binário e formatando diretamente
    binIPAddress    = '.'.join([f'{intIPAddress:032b}'[i:i+8] for i in range(0, 32, 8)])
    binMascara      = '.'.join([f'{intMascara:032b}'[i:i+8] for i in range(0, 32, 8)])
    binNETAddress   = '.'.join([f'{ipNETAddress:032b}'[i:i+8] for i in range(0, 32, 8)])
    binBroadcast    = '.'.join([f'{intBroadcast:032b}'[i:i+8] for i in range(0, 32, 8)])
    binPrimeiroHost = '.'.join([f'{intPrimeiroHost:032b}'[i:i+8] for i in range(0, 32, 8)])
    binUltimoHost   = '.'.join([f'{intUltimoHost:032b}'[i:i+8] for i in range(0, 32, 8)])

   # Exibindo os dados
    print(f'Endereço IP fornecido ..: {strIPAddress:>15} / {binIPAddress}')
    print(f'Máscara de Rede ........: {strMascara:>15} / {binMascara}')
    print(f'Endereço de Rede .......: {strNETAddress:>15} / {binNETAddress}')
    print(f'Primeiro Host ..........: {strPrimeiroHost:>15} / {binBroadcast}')
    print(f'Endereço de Broadcast ..: {strBroadcast:>15} / {binPrimeiroHost}')
    print(f'Último Host ............: {strUltimoHost:>15} / {binUltimoHost}\n')

# Criar um dicionário com os dados
dados = {
    "Endereço IP fornecido": {
        "notação decimal": strIPAddress,
        "notação binária": binIPAddress
    },
    "Máscara de Rede": {
        "notação decimal": strMascara,
        "notação binária": binMascara
    },
    "Endereço de Rede": {
        "notação decimal": strNETAddress,
        "notação binária": binNETAddress
    },
    "Primeiro Host": {
        "notação decimal": strPrimeiroHost,
        "notação binária": binPrimeiroHost
    },
    "Endereço de Broadcast": {
        "notação decimal": strBroadcast,
        "notação binária": binBroadcast
    },
    "Último Host": {
        "notação decimal": strUltimoHost,
        "notação binária": binUltimoHost
    }
}

# Imprimir dados no formato JSON
# print(json.dumps(dados, indent=4))

# Salvar dados em arquivo JSON
with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)