COMPRAS = ["arroz", "feijão", "macarrão", "leite", "açúcar"]

print("Lista inicial:", COMPRAS)

# Adiciona no final
COMPRAS.append("café")
print("Após append():", COMPRAS)

# Insere em uma posição específica
COMPRAS.insert(1, "óleo")
print("Após insert():", COMPRAS)

# Adiciona mais de um item
COMPRAS.extend(["biscoito", "refrigerante"])
print("Após extend():", COMPRAS)

# Remove um item pelo nome
COMPRAS.remove("açúcar")
print("Após remove():", COMPRAS)

# Remove o último item
removido = COMPRAS.pop()
print(f"Removido: {removido}")
print("Após pop():", COMPRAS)

# Remove pelo índice
removido2 = COMPRAS.pop(1)
print(f"Removido do índice 1: {removido2}")
print("Lista final:", COMPRAS)