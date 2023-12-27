# Lista: representa uma sequência de valores

# Sintaxe: nome_da_lista = [valor1, valor2, valor3, ..., valorN]

# Exemplo:
n1 = [1, 2 ,3 ,4 ,5]
n2 = [6, 7, 8, 9, 10]
valores  = n1 + n2

print(valores) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(type(valores)) # <class 'list'>

print(valores[0]) # 1

print(valores[-1]) # 10 (último elemento) 

valores[0] = 20 # Altera o valor do primeiro elemento

print(valores[0]) # 20

print(valores[2:6]) # [3, 4, 5, 6] (do terceiro ao sexto elemento)

print(valores[:6]) # [20, 2, 3, 4, 5, 6] (do primeiro ao sexto elemento)

print(valores[2:]) # [3, 4, 5, 6, 7, 8, 9, 10] (do terceiro ao último elemento)

print(valores[-3:]) # [8, 9, 10] (do terceiro ao último elemento)

print(valores[-3:-1]) # [8, 9] (do terceiro ao penúltimo elemento)

print(valores[2:2]) # [] (lista vazia)

print(len(valores)) # 10 (tamanho da lista)

print(sorted(valores, reverse=True)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (lista ordenada de forma decrescente)

print(sum(valores)) # 55 (soma dos elementos da lista)

print(min(valores)) # 1 (menor elemento da lista)

print(max(valores)) # 10 (maior elemento da lista)

valores.append(11) # Adiciona o elemento 11 ao final da lista
print(valores) # [20, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

valores.pop() # Remove o último elemento da lista ou o eelemento de índice informado
print(valores) # [20, 2, 3, 4, 5, 6, 7, 8, 9, 10]

valores.insert(0, 23) # Insere o elemento 0 na posição 0 da lista
print(valores) # [23, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(12 in valores) # False (verifica se o elemento 12 está na lista)

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta) # Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano, Netuno
print('Fim do loop')

