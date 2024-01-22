from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

'''
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            raise NumeroNegativoError # Levanta a exceção
    except NumeroNegativoError: # Captura a exceção
        print(f"Você digitou um número negativo.")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print(f"\nPrograma encerrado.")
'''
if __name__ == '__main__':
    try:
        while True:
            try:
                num = int(input("Digite um número: "))
                if num < 0:
                    raise NumeroNegativoError # Levanta a exceção
                break
            except NumeroNegativoError:
                print(f"Você digitou um número negativo.")
    except:
        print(f"Ocorreu um erro inesperado.")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print(f"\nPrograma encerrado.")
