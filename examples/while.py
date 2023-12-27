# While loop
i = 1
while i < 6:
  print(i)
  i += 1
print('Fim do loop')


# Enquanto não digitar x, o programa vai continuar pedindo para digitar um número
nome = None

while True:
    print("Digite seu nome, ou X para parar: ")
    nome = input()
    if nome == 'x' or nome != 'X':
        break
    print("Seu nome é " + nome)
print("Fim do programa")