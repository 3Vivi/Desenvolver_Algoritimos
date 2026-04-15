def calcular_total_compra():
    print("--- Caixa de Supermercado ---")
    
    try:
        # Solicita os dois produtos
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))
        
        # Calcula o total
        total = preco1 + preco2
        print(f"Valor total da compra: R$ {total:.2f}")
        
    except ValueError:
        # Tratamento de erros para valores não numéricos
        print("Erro: Os preços devem ser numéricos. Encerrando execução.")

# Chamada da função
calcular_total_compra()