def imc():
    try:
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))

        resultado = peso / (altura * altura)

        if resultado < 18.5:
            print("Magro")
        elif resultado <= 24.9:
            print("Normal")
        else:
            print("Acima do peso")

    except:
        print("Erro nos dados")

imc()