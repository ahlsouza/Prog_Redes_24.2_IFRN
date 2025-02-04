
import random

print('\n------- [term.ooo] --------')
# Leitura do Arquivo:
# O programa deve ler um arquivo texto com uma lista de palavras com no mínimo 5 e no máximo 8 letras.
arquivo = input('\nbase de palavras: ')
# O programa deve armazenar as palavras em uma lista.
arquivo_aberto = open(arquivo, 'r')
texto = arquivo_aberto.read()
palavras = texto.split()
arquivo_aberto.close()

# O programa deve sortear uma palavra aleatória da lista de palavras.
oculta = random.choice(palavras).upper()
tentativas = 0
tamanho_palavra = len(oculta)
# O programa informa quantas letras a palavra sorteada tem.
print("\nQuantidade de letras: ", len(oculta))
exibida = '_'*len(oculta)
print(exibida, len(oculta), '[posições e 6 tentativas]')
print('')
ntentativas = 0

while ntentativas <6:
    # Solicita uma palavra do usuário com o mesmo número de letras da palavra oculta
    tentativa = input("\nDigite uma palavra: ").upper()
    
    if len(tentativa) != tamanho_palavra:
        print(f"A palavra deve ter {tamanho_palavra} letras. Tente novamente.")
        continue

    # Verifica a tentativa e fornece o retorno visual (texto com uma cor)
    retorno = []
    for i, letra in enumerate(tentativa):
        if letra == oculta[i]:
            retorno.append(f"\033[92m{letra}\033[0m")  # Verde para letra correta e na posição certa
        elif letra in oculta:
            retorno.append(f"\033[93m{letra}\033[0m")  # Amarelo para letra correta na posição errada
        else:
            retorno.append(f"\033[90m{letra}\033[0m")  # Cinza para letra incorreta

    # Exibe o retorno formatado
    print("\nretorno: ", " ".join(retorno))
    ntentativas += 1

# Se o usuário adivinhar a palavra em 6 tentativas ou menos, o programa deve parabenizá-lo e mostrar o número de tentativas utilizadas.
if tentativa == oculta:
    print(f"Parabéns! Você acertou a palavra '{oculta}' em {tentativas} tentativas.")
# Se o usuário não conseguir adivinhar a palavra em 6 tentativas, o programa deve revelar a palavra e informar que o usuário perdeu.
else:
    print("Tente novamente!")
print('\nA palavra é: ',oculta)