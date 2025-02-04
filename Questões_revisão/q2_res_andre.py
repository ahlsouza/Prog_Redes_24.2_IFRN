# Definição do Problema (encontrar um 'nonce' que gere um hash com uma certa quantidade de bits em zero)
import hashlib
import time

# Definir a função findNonce com dois argumentos: textoToHash (conjunto de bytes) e bitsToBeZero (número de bits iniciais que devem ser zero no hash).

def findNonce(textoToHash, bitsToBeZero):
    inicioTempo = time.time()
    # Inicializar um contador de nonce.
    nonce = 0   
    maxlimite = (1 << (256 - bitsToBeZero)) - 1  #define o limite máximo que o hash resultante pode atingir para ser considerado válido
    
    # Implementação do loop de mineração: Loop infinito até encontrar um nonce que atenda ao requisito.
    while nonce < 2**32:
    # agrega textoToHash + nonce (4 bytes)
        agregado = textoToHash + nonce.to_bytes(4, 'big')  #garante que o nonce seja sempre representado por 4 bytes
        
        # calcula o SHA-256 hash
        hashFinal = hashlib.sha256(agregado).digest()
        
        # tranformar hash em inteiro
        hash_inteiro = int.from_bytes(hashFinal, 'big')
        
        # Implementar uma função para verificar se o hash atende ao requisito de bits em zero.
        if hash_inteiro <= maxlimite:
            break
        
        # Incremento do nonce
        nonce += 1
    
    # Utilizar a função time() para medir o tempo de início e fim da execução.
    # Calcular o tempo de execução total.
    end_time = time.time()
    tempoCalculo = end_time - inicioTempo
    
    if nonce == 2**32:
        return None, tempoCalculo  # Indica que nenhum nonce foi encontrado dentro do limite de 4 bytes
    else:
        return nonce, tempoCalculo

# Exemplo de uso
dados = ["Esse é fácil", "Esse é fácil", "Esse é fácil", "Texto maior muda o tempo?", "Texto maior muda o tempo?", "Texto maior muda o tempo?", "É possível calcular esse?", "É possível calcular esse?", "É possível calcular esse?"]

bits = [8,10,15,8,10,15,18,19,20]

for x, y in zip(dados, bits):
    texto = x
    texto_bytes = texto.encode('utf-8')
    bits_zero = y
    nonce, duracao = findNonce(texto_bytes, bits_zero)

    # Retornar o nonce encontrado e o tempo de execução.
    if nonce is not None:
        print(f"Nonce encontrado: {nonce}, Tempo decorrido: {duracao:.2f} segundos, no texto {x}, com {y} bits em zero.")
    else:
        print(f"Nenhum nonce encontrado em 4 bytes, Tempo decorrido: {duracao:.2f} segundos, no texto {x}, com {y} bits em zero.")
