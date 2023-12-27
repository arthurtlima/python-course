# For loop
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)
print('Fim do loop')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
print('Fim do loop')

word = 'python'
for letter in word:
    print(letter)
print('Fim do loop')

for i in range(1, 11): # range(start, stop, step)
    print(i) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print('Fim do loop')

for i in range(10): # range(stop)
    print(i) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print('Fim do loop')

for i in range(0, 30, 5): # range(start, stop, step)
    print(i) # 0, 5, 10, 15, 20, 25
print('Fim do loop')

for i in range(0, -10, -1): # range(start, stop, step)
    print(i) # 0, -1, -2, -3, -4, -5, -6, -7, -8, -9
print('Fim do loop')

for i in range(-10, 0, 1): # range(start, stop, step)
    print(i) # -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
print('Fim do loop')

pedras = ('diamante', 'rubis', 'safira', 'esmeralda')
for pedra in pedras:
    if pedra == 'safira':
        continue # Pula para a próxima iteração
    print(pedra) # diamante, rubis, esmeralda
print('Fim do loop')