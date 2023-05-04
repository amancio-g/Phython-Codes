import random

numeros_possiveis  = list(range(1, 76))
quantidade_numeros = 24 


random.shuffle(numeros_possiveis)


num_cartelas = int(input("Quantas cartelas voce quer no jogo? "))
cartelas = []
for i in range(num_cartelas):
    cartela = random.sample(numeros_possiveis, quantidade_numeros)
    cartela.sort()
    cartelas.append(cartela)


numeros_sortedados = []
bingos = []
while not bingos:
    numero_sorteado = random.choice(numeros_possiveis)
    numeros_possiveis.remove(numero_sorteado)
    numeros_sortedados.append(numero_sorteado)



    for i, cartela in enumerate(cartelas):
        if numero_sorteado in cartela:
            cartela.remove(numero_sorteado)
            if not cartela:
                bingos.append(i)


    print("numero sorteado:", numero_sorteado)
    
    print("Bingo! cartelas vencedroas:")
    for i in bingos:
        print(cartelas[i])



