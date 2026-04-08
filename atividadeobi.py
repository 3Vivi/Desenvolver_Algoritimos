# Leitura dos dados
Pão = int(input())
Doces = int(input())
Bolo = int(input())

# Cálculo da pontuação total
total = Pão*1 + Doces*2 + Bolo*3

# Verificação das condições
if total >= 150:
    print('B')
elif total >= 120:
    print('D')
elif total >= 100:
    print('P')
else:
    print('N')