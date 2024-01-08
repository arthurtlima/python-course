nome = 'Arthur'
sobrenome = 'Lima'
frase = 'O rato roeu a roupa do rei de roma'
email = 'arthur@teste.com'

print(nome + ' ' + sobrenome) # Concatenação de strings

print(nome * 3) # Repete a string 3 vezes
print(nome[0]) # Retorna o primeiro caracter da string
print(nome[0:3]) # Retorna os caracteres da posição 0 a 3
print(nome[-1]) # Retorna o ultimo caracter da string
print(len(nome)) # Retorna o tamanho da string
print(nome.find('h')) # Retorna a posição da primeira letra encontrada

palavras = frase.split() # Separa a string em uma lista de strings
print(palavras) # ['O', 'rato', 'roeu', 'a', 'roupa', 'do', 'rei', 'de', 'roma']

for letra in nome: # Percorre a string
    print(letra) # Imprime cada letra da string

arroba = email.find('@') # Retorna a posição da primeira letra encontrada
print(arroba) # 6
print(email[:arroba]) # Retorna os caracteres do inicio da string até a posição 6
print(email[arroba+1:]) # Retorna os caracteres da posição 7 até o final da string

produtos = 'banana nanica e maçã'
print('maçã' in produtos) # Verifica se a string esta contida na outra string
print('maçã' not in produtos) # Verifica se a string não esta contida na outra string

segunda_frase = 'A capivara é um animal muito legal'
print(segunda_frase.upper()) # Converte a string para maiusculo
print(segunda_frase.lower()) # Converte a string para minusculo
print(segunda_frase.capitalize()) # Converte a primeira letra da string para maiusculo
print(segunda_frase.title()) # Converte a primeira letra de cada palavra da string para maiusculo

replace_segunda_frase = segunda_frase.replace('capivara', 'cachorro') # Substitui uma string por outra string
print(replace_segunda_frase) # A cachorro é um animal muito legal

terceira_frase = '   A capivara é um animal muito legal   '
print(terceira_frase.strip()) # Remove os espaços em branco no inicio e no final da string
print(terceira_frase.rstrip()) # Remove os espaços em branco no final da string
print(terceira_frase.lstrip()) # Remove os espaços em branco no inicio da string

fruta = 'banana'
print(fruta.center(20)) # Centraliza a string em um espaço de 20 caracteres
print(fruta.ljust(20)) # Alinha a string a esquerda em um espaço de 20 caracteres
print(fruta.rjust(20)) # Alinha a string a direita em um espaço de 20 caracteres
print(fruta.center(20, "-")) # Centraliza a string em um espaço de 20 caracteres e preenche com o caracter '-' 

print(terceira_frase.count('a')) # Conta quantas vezes a string aparece na outra string
print(terceira_frase.count('a', 0, 13)) # Conta quantas vezes a string aparece na outra string entre as posições 0 e 13

print(terceira_frase.zfill(50)) # Preenche a string com zeros a esquerda até completar 50 caracteres

p = 'Treinamentos de Python para Iniciantes'
print(p.startswith('T')) # Verifica se a string começa com a string passada
print(p.endswith('s')) # Verifica se a string termina com a string passada

# Docstrings
"""
Docstring é uma espécie de comentário que serve para documentar o código.
"""
docstring = """ 
Testando docstrings
"""
print(docstring) # Testando docstrings