# São imutáveis

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
concatenated = tuple1 + tuple2
print(concatenated) # ('apple', 'banana', 'cherry', 1, 5, 7, 9, 3)
print(concatenated[0:2]) # ('apple', 'banana')

t1 = (1, 2, 3, 4, 3, 5, 6, 7, 3, 8, 9)
print(t1.count(3)) # 3

# Operações não disponíveis em tuplas: append(), remove(), pop(), insert(), clear()
# Tudo que altera o conteudo da tupla não é permitido

for numer in t1:
    print(numer)

# criar lista a partir de tupla
group17 = list(t1)
group17[0] = 17
print(group17) # [17, 2, 3, 4, 3, 5, 6, 7, 3, 8, 9]
print(type(group17)) # <class 'list'>

# criar tupla a partir de lista
pizzas = ("Pepperoni", "4 Queijos", "Marguerita")
pizzas_novas = tuple(pizzas)
print(pizzas_novas) # ('Pepperoni', '4 Queijos', 'Marguerita')
print(type(pizzas_novas)) # <class 'tuple'>

# Ordenar tupla em ordem alfabética ou numérica
# metodo sort() não funciona em tuplas
print(sorted(pizzas)) # ['4 Queijos', 'Marguerita', 'Pepperoni']
