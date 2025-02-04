#Planejamento das Entradas
key = input("Digite a palavra-passe: ")
txt = input ("Nome do arquivo a ser processado: ")
destino = input("Nome do arquivo de destino: ")
print('')
#Nome do arquivo de destino (onde os dados processados serão salvos).

#Leitura do Arquivo de Origem
origem = open(txt,'rb')
bytes = origem.read()
origem.close()

#lista de bytes do Arquivo de Origem
lista_bytes = []
for i in bytes:
   lista_bytes.append(i)
#print(lista_bytes) 
#print(bytes)

#Processamento da Palavra-Passe
lista_ascii=[]
for letra in key:
    valor_ascii = 0
    for i, letra_ascii in enumerate("0123456789"):
        if letra == letra_ascii:
            valor_ascii = bin(i + 48)[2:].zfill(8) # Valores ASCII de 0 a 9
            keybytes=int(valor_ascii, 2)           # Converter string binaria em números binários
            break
    if valor_ascii == 0:
        for i, letra_ascii in enumerate("abcdefghijklmnopqrstuvwxyz"):
            if letra == letra_ascii:
                valor_ascii = bin(i + 97)[2:].zfill(8)  # Valores ASCII de a a z
                keybytes=int(valor_ascii, 2)            # Converter string binaria em números binários
                break
    lista_ascii.append(keybytes)

#print(lista_ascii)

'''
5. **Aplicação da Operação ‘xor’**: Para cada byte lido do arquivo de origem, aplicar a operação ‘xor’ com o byte correspondente da palavra-passe. Aqui, é necessário um controle para saber qual byte da palavra-passe usar a cada iteração. Além disso, devemos ter uma lógica para repetir a palavra-passe quando todos os seus bytes já tiverem sido usados.
'''

# Aplicação da Operação ‘xor’
tamanho_maximo = max(len(lista_bytes), len(lista_ascii))

if len(lista_bytes) < len(lista_ascii):
   lista_bytes = lista_bytes * (tamanho_maximo // len(lista_bytes)) + lista_bytes[:tamanho_maximo % len(lista_bytes)]
elif len(lista_ascii) < len(lista_bytes):
        lista_ascii = lista_ascii * (tamanho_maximo // len(lista_ascii)) + lista_ascii[:tamanho_maximo % len(lista_ascii)]
resultado = []
for k in range(tamanho_maximo):
   resultado.append(lista_bytes[k] ^ lista_ascii[k])

print(resultado)

'''
6. **Preparação dos Dados para Saída**: Após processar todos os bytes, devemos armazenar os resultados em uma estrutura adequada para posteriormente escrever no arquivo de destino.
'''
arqDest=[]
for g in resultado:
    final=bin(g)[2:].zfill(8)
    arqDest.append(final)
#print(arqDest)

'''
7. **Escrita no Arquivo de Destino**: Criar ou abrir o arquivo de destino e escrever os dados processados nele, garantindo que tudo esteja salvo corretamente.
'''
arquivo = open(destino, "w")
arquivo.write(' '.join(arqDest))
arquivo.close()

print('')
print('<Arquivo gerado>')