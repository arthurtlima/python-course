# Sintaxe:
# print(objeto, argumentos)

# Exemplos:
msg = 'Hello World!'
print(msg) # Hello World!
print('Hello World!') # Hello World!

name = 'Arthur Teodoro'
print('Hello, my name is', name) # Hello, my name is Arthur Teodoro

print('Hello, my name is ' + name + " I'm from brazil") # Hello, my name is Arthur TeodoroI'm from brazil
print('Outro texto')

print('Imprime a mensagem.', end="") # Imprime a mensagem.
print(' Continua na mesma linha.') # Continua na mesma linha da mensagem de cima.


name = 'Maria'
age = 30
formatted_msg = 'Hello, my name is {0} and I am {1} years old.'.format(name, age) # Forma mais complexa de formatar uma string
print(formatted_msg) # Hello, my name is Maria and I am 30 years old.

formatted_msg = f"Hello, my name is {name} and I am {age} years old." # Forma mais simples de formatar uma string
print(formatted_msg) # Hello, my name is Maria and I am 30 years old.

a = 10
b = 20
formatted_msg = f"{a} + {b} = {a + b}" # Forma mais simples de formatar uma string
print(formatted_msg) # 10 + 20 = 30

value = 314.1592653589793 
print(f"O valor é {value:.2f}") # O valor é 314.16
print(f'O valor é \'{value:.3f}\'') # O valor é 314.159

name = 'João'
age = 32
# usamdp tabulação para alinhar os valores
print(f'Name: {name}\tIdade: {age}') # Name: João	Idade: 32 