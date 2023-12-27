# Formas de importar um módulo:
# import math # Importa o módulo math inteiro

#from math import * # Importa todas as funções do módulo math
# podem ocorrer conflitos de nomes de funções com essa forma de importação

# import math as m # Importa o módulo math inteiro e renomeia para m

from math import sqrt # Importa apenas a função sqrt do módulo math

print(sqrt(25)) # 5.0

"""
import mod_func as mf

if __name__ == '__main__':
    mf.mensagem()

    num = int(input('Digite um valor: '))

    print(f'Calcular o fatorial do número: ')
    fat = mf.fatorial(num)
    print(f'O fatorial de {num} é {fat}')

Explicação do código

import mod_func as mf: Importa o módulo mod_func e o apelida de mf. Isso permite que você use as funções definidas em mod_func com o prefixo mf..

if __name__ == '__main__':: Esta construção verifica se o script está sendo executado como o programa principal (não sendo importado como um módulo). Isso é comum em scripts Python para garantir que o código dentro do bloco if __name__ == '__main__': seja executado apenas quando o script é executado diretamente e não quando é importado como um módulo.

mf.mensagem(): Chama a função mensagem() do módulo mod_func. Como no código anterior, presume-se que esta função exibe alguma mensagem.

num = int(input('Digite um valor: ')): Solicita ao usuário que insira um valor, converte a entrada para um número inteiro e armazena o resultado na variável num.

print(f'Calcular o fatorial do número: '): Imprime uma mensagem indicando que o programa irá calcular o fatorial do número inserido.

fat = mf.fatorial(num): Chama a função fatorial() do módulo mod_func passando o valor inserido pelo usuário (num) como argumento. O resultado (o fatorial) é armazenado na variável fat.

print(f'O fatorial de {num} é {fat}'): Imprime o resultado do cálculo do fatorial, indicando o número original e seu fatorial.

Lembre-se de que a compreensão total do script dependerá das implementações específicas das funções no módulo mod_func.
"""

