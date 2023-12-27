import random

print("Gerar cinco números aleatórios entre 1 e 50:")
for i in range(5):
    n = random.randint(1, 50)
    print(f'Número gerado: {n}')
print('Fim dos loops')

valor = random.random()
print(f'Número gerado: {round(valor * 10, 2)}') # Número gerado por exemplo: 3.14

valor = random.uniform(1, 100)
print(f'Número: {round(valor, 4)}') # Número gerado por exemplo: 3.1415

L = [1, 2, 3, 4, 5]
n = random.choice(L)
print(f'Número escolhido: {n}') # Número escolhido por exemplo: 3

n = random.sample(L, 3) # Escolhe 3 números aleatórios da lista
print(f'Números escolhidos: {n}') # Números escolhidos por exemplo: [3, 5, 1]

#Embaralha a lista
print(f'Lista original: {L}') # Lista original: [1, 2, 3, 4, 5]
print(f"Embaralhando a lista...") 
n = random.shuffle(L)
print(f'Lista embaralhada: {L}') # Lista embaralhada: [3, 1, 5, 4, 2]