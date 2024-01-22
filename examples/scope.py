# Escopo Global e Local

var_global = "global"

def escreve_texto():
    global var_global # Acessa a variável global
    var_global = "global 2" # Altera a variável global
    var_local = "local"
    print(f'Variável Global: {var_local}')
    print(f'Variável Local: {var_global}')

if __name__ == '__main__':
    escreve_texto()
    print(f'Variável Global: {var_global}')
    #print(f'Variável Local:{var_local}') # Erro


