#Atividade - Manipulção de Listas em Python

numeros = [10, 20, 30, 40, 20, 50]

# 1) Quantos elementos existem na lista
print("Quantidade de elementos:", len(numeros))

# 2) Quantas vezes o número 20 aparece
print("Quantas vezes 20 aparece:", numeros.count(20))

# 3) Posição do número 30
print("Posição do número 30:", numeros.index(30))

# Verificar se 100 está na lista
print("100 está na lista?", 100 in numeros)


import random

# Lista inicial
numeros = [91, 34, 67, 15, 82]

# Mostrar lista original
print("Lista original:", numeros)

# Ordem crescente
numeros.sort()
print("Ordem crescente:", numeros)

# Ordem decrescente
numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)

# Segunda lista
dados = [80, 7, 10, 9, 19]

# Embaralhar lista
random.shuffle(dados)
print("Lista embaralhada:", dados)

# Desafio
lista3 = [5, 12, 8, 20, 3, 15]

print("Terceira lista:", lista3)

lista3.sort()
print("Crescente:", lista3)

lista3.sort(reverse=True)
print("Decrescente:", lista3)

random.shuffle(lista3)
print("Embaralhada:", lista3)