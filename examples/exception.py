# Exceção é um erro que ocorre durante a execução do programa. 
# Quando uma exceção ocorre, o programa é interrompido e o interpretador Python exibe uma mensagem de erro.
# Bloco try/except


def div(k, j):
    return round(k/j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input("Digite um número: "))
            n2 = int(input("Digite outro número: "))
            break
        except ValueError:
            print(f'Ocorreu um erro, tente novamente.')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f"Não é possível dividir por zero.")
    except:
        print(f"Ocorreu um erro inesperado.")
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\nPrograma encerrado.')