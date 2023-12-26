# Comparison Operators
x = y = z = False
n1 = n2 = 0

print("Digite um número: ")
n1 = int(input())
print("Digite outro número: ")
n2 = int(input())

print("n1 == n2: ", n1 == n2)
print("n1 != n2: ", n1 != n2)
print("n1 > n2: ", n1 > n2)
print("n1 < n2: ", n1 < n2)
print("n1 >= n2: ", n1 >= n2)
print("n1 <= n2: ", n1 <= n2)

y = n1 == n2
print("São iguais?" + (y)) # Nesse caso precisamos converter o valor booleano para string quando estamos concatenando com uma string 