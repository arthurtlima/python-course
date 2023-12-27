# tabela verdade para and 
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# tabela verdade para or
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# tabela verdade para not
# not True = False
# not False = True
age = 29
height = 1.75

result = (age >= 18) and (height >= 1.70)
msg = 'Pode participar do evento? ' + str(result) # Nesse caso precisamos converter o valor booleano para string quando estamos concatenando com uma string
print(msg) # True

# Programa de disparo de alarme
port = 'c'
alarm = 'on'

result =  (port == 'o') or (alarm == 'on')
msg = 'Alarme disparado? ' + str(result) # Nesse caso precisamos converter o valor booleano para string quando estamos concatenando com uma string
print(msg) # False

# Programa que checa se tem dinheiro
has_money = False
has_money = not has_money # Inverte o valor da variável
msg = 'Tem dinheiro? ' + str(has_money) # Nesse caso precisamos converter o valor booleano para string quando estamos concatenando com uma string
print(msg) # True