animal = ["Cachorro", "Gato"]
print("Lista inicial: ", animal)

animal.append("Pato") #adiciona no fim da lista
print("Lista atualizado: ", animal)

animal.insert(1, "Coelho")
print("Lista atualizada: ", animal)

animal.extend(["macaco", "leão"]) #add mais de um
print("Lista atualizado: ", animal)

animal.remove("leão")
print(animal)

removido = animal.pop()
print(f"Removido: {removido}")
print("Após pop()", animal)

removido2 = animal.pop(1)
print(f"Removido do indice 1 {removido2}")
print("Após pop(1): ", animal)