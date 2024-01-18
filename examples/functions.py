# Funções
# Modulação é a divisão de um programa grande em partes menores e independentes.
# Funções são blocos de código que executam uma tarefa específica.
# Reutilizar funções é uma parte importante da programação modular.
# Legibilidade é outra vantagem de usar funções.

def hello():
    print('Olá, mundo!')

hello() # Olá, mundo!

# Função com argumentos
def hello(nome):
    print('Olá, ' + nome + '!')
hello('Arthur') # Olá, Arthur!

def mult(x, y): # Função com dois argumentos
    return x * y # Retorna o resultado da multiplicação
a = 4
b = 5
c = mult(a, b) # Chama a função mult()
print(f'O produto de {a} e {b} é {c}') # 20

def div(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossível dividir por zero!'


if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))

    r = div(a, b)
    print(f'O resultado da divisão é {r}')

    def quadrado(val): # Função com um argumento
        quadrados = [] # Lista vazia
        for x in val: # Para cada elemento de val
            quadrados.append(x ** 2) # Adiciona o quadrado de x
        return quadrados # Retorna a lista de quadrados
    
if __name__ == '__main__': # Se for o programa principal
    valores = [1, 2, 3, 4, 5] # Lista de valores
    quadrados = quadrado(valores) # Chama a função quadrado()
    print(quadrados) # [1, 4, 9, 16, 25]
# OU 
    for g in quadrados:
        print(g) # 1 4 9 16 25