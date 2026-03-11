contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "João"
}

# Obter chaves
print("Chaves: ")
for insta in contato.keys():
    print(insta)

#Obter valores
print("\n Valores:")
for nome in contato.values():
    print(nome)

#Obter pares (chave-valor)
print("\n Pàres: ") 
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

contato = {
    "@camila": 1.66,
    "@paola": 1.50,
    "@sheron": 1.80,
    "@bruna": 1.60,
    "@joao": 1.70
}
# Ordenar por chave 
print("Ordenar por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

#Ordenar por valor
from operator import itemgetter
print("\n Ordenando por valor (altura): ")
for insta, estrutura in sorted(contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estrutura:.2f}m")