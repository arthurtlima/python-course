print('Digite o nome de 5 bebidas: ')

bebidas = []

for i in range(5):
    print("Digite o nome da bebida: ")
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print('Suas bebidas favoritas são: ')
for bebida in bebidas:
    print(bebida)