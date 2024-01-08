import math
# no python temos as funções internas e as funções externas importadas por modulos

# Funções externas importadas por modulos

x = 8
y = 100

raiz_quadrada = math.sqrt(x) # sqrt é uma função do modulo math que retorna a raiz quadrada de um numero
print(raiz_quadrada) # 2.8284271247461903
print(math.floor(raiz_quadrada)) # floor é uma função do modulo math que retorna o menor numero inteiro de um numero
print(math.ceil(raiz_quadrada)) # ceil é uma função do modulo math que retorna o maior numero inteiro de um numero


logoritmo = math.log10(y) # log10 é uma função do modulo math que retorna o logoritmo de um numero na base 10
print(logoritmo) # 2.0

print(math.pi) # pi é uma variavel do modulo math que retorna o valor de pi
print(math.factorial(x)) # factorial é uma função do modulo math que retorna o fatorial de um numero
print(x / math.inf) # inf é uma variavel do modulo math que retorna o valor de infinito



# Funções internas do python

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(valores)) # max é uma função interna do python retorna o maior valor da lista
print(min(valores)) # min é uma função interna do python retorna o menor valor da lista

a = -5
b = 4
print(abs(a)) # abs é uma função interna do python retorna o valor absoluto de um numero
print(pow(b, a)) # pow é uma função interna do python retorna o valor de um numero elevado a outro numero

c = 5.54902
print(round(c,3)) # round é uma função interna do python retorna o valor de um numero arredondado para um numero de casas decimais