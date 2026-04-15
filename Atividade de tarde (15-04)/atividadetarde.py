def calcular_media_aluno():
    notas = []
    
    print("--- Sistema de Cálculo de Média ---")
    
    # Estrutura de repetição para entrada de 3 notas
    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)
        except ValueError:
            # Tratamento de erros para valores não numéricos
            print("Erro: As notas devem ser numéricas. Encerrando execução.")
            return # Encerra a função imediatamente

    # Cálculo da média
    media = sum(notas) / len(notas)
    print(f"Média final: {media:.2f}")

# Chamada da função
calcular_media_aluno()