# string e convenção de como escrever variavel em python
user_name = 'Arthur'
print(user_name)


#tipos numericos
average = 0
n1 = n2 = n3 = n4 = 0.0
name, age, weight = 'Arthur', 25, 73.5
state = True

# Função type() retorna o tipo da variavel
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(weight)) # <class 'float'>
print(type(state)) # <class 'bool'>
print(type(1+2j)) # <class 'complex'>


# Função isistance() retorna se a variavel é do tipo especificado
a = 10
b = 'Sun'
# verifica se a variavel é do tipo int
print(isinstance(a, (int, float, complex))) # True
# verifica se a variavel é do tipo int, float ou complex
print(isinstance(a, (int, float, complex))) # True
# verifica se a variavel é do tipo str
print(isinstance(b, str)) # True
# verifica se a variavel é do tipo str
print(isinstance(b, int)) # False

# comentário de uma linha -> #

# comentário de multiplas linhas -> """ """