import random

# 1. Jogo de adivinhação

numero_secreto = random.randint(1, 100)
tentativas = 0

print("=== Jogo de Adivinhação ===")

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Acertou! Número de tentativas: {tentativas}")
        break
    elif palpite < numero_secreto:
        print("maior")
    else:
        print("menor")

# 2. Números repetidos

print("\n=== Verificar números repetidos ===")

numeros = []

for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

contagem = {}

for num in numeros:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print("\nNúmeros repetidos:")

repetidos = False
for num, qtd in contagem.items():
    if qtd > 1:
        print(f"{num} apareceu {qtd} vezes")
        repetidos = True

if not repetidos:
    print("Nenhum número foi repetido")