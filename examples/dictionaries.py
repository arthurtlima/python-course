# Dicionários

# Dicionários são estruturas de dados que armazenam pares de chave-valor.
# As chaves são únicas e não podem ser repetidas.
# Os valores podem ser de qualquer tipo.
# Os dicionários são delimitados por chaves {}.
# Os pares de chave-valor são separados por vírgula.
# As chaves e os valores são separados por dois pontos.

elemento = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(f"Elemento: {elemento['brand']}") # Elemento: Ford
print(f"Elemento: {elemento.get('colors')}") # Elemento: ['red', 'white', 'blue']

# Atualizar um valor
elemento["year"] = 2020
print(f"Elemento: {elemento['year']}") # Elemento: 2020

# Adicionar um novo par de chave-valor
elemento["model"] = "Mustang"
print(f"Elemento: {elemento}") # Elemento: {'brand': 'Ford', 'electric': False, 'year': 2020, 'colors': ['red', 'white', 'blue'], 'model': 'Mustang'}  

# Remover um par de chave-valor
# elemento.pop("model") ou del elemento["model"]
del elemento["model"]
print(f"Elemento: {elemento}") # Elemento: {'brand': 'Ford', 'electric': False, 'year': 2020, 'colors': ['red', 'white', 'blue']}

# Limpar o dicionário
# elemento.clear()
# print(f"Elemento: {elemento}") # Elemento: {}

# Remover o dicionário
# del elemento
# print(f"Elemento: {elemento}") # NameError: name 'elemento' is not defined

print(elemento.items()) # dict_items([('brand', 'Ford'), ('electric', False), ('year', 1964), ('colors', ['red', 'white', 'blue'])])    
for chave, valor in elemento.items():
  print(f"Chave: {chave} - Valor: {valor}")

for chave in elemento.keys():
    print(f"Chave: {chave}")

for valor in elemento.values():
    print(f"Valor: {valor}")

for chave, valor in elemento.items():
    print(f"Chave: {chave} - Valor: {valor}")