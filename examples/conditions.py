# Existem os condicionais simples, composto e encadeado

# Condicional simples
# if condicao:
#     codigo

# Condicional composto
# if condicao:
#     codigo
# else:
#     codigo

# Condicional encadeado
# if condicao:
#     codigo
# elif condicao:
#     codigo
# else:
#     codigo

n1 = n2 = 0
average = 0.0

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

average = (n1 + n2) / 2

if average >= 7:
    print("Aprovado.") # Nesse caso precisamos converter o valor float para string quando estamos concatenando com uma string
elif average >= 5:
    print("Recuperação.")
else:
    print("Reprovado.") # Nesse caso precisamos converter o valor float para string quando estamos concatenando com uma string
print("A sua nota é {}".format(average))