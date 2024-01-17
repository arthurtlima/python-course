# Set são coleções não ordenadas de elementos únicos.
# Podem ser criados usando chaves {} ou a função set().
# Os elementos de um set devem ser imutáveis.

planeta_anao = {'Plutão', 'Ceres', 'Eris'}
print(planeta_anao) # {'Plutão', 'Ceres', 'Eris'}
print(type(planeta_anao)) # <class 'set'>
print(len(planeta_anao)) # 3
print('Plutão' in planeta_anao) # True
print('Plutão' not in planeta_anao) # False

for astro in planeta_anao:
    print(astro.upper()) # PLUTÃO CERES ERIS

astros = ['Plutão', 'Ceres', 'Eris', 'Plutão']
print(astros, end=' ') # ['Plutão', 'Ceres', 'Eris', 'Plutão']
astro_set = set(astros)
print(astro_set) # {'Plutão', 'Ceres', 'Eris'} 
# Note que o segundo Plutão foi removido

astro1 = {'Plutão', 'Ceres', 'Eris'}
astro2 = {'Plutão', 'Ceres', 'Eris', 'Saturno'}
print(astros != astro2) # True
print(astro1 | astro2) # {'Plutão', 'Ceres', 'Eris', 'Saturno'}
print(astro1.union(astro2)) # {'Plutão', 'Ceres', 'Eris', 'Saturno'}

print(astro1 & astro2) # {'Plutão', 'Ceres', 'Eris'}
print(astro1.intersection(astro2)) # {'Plutão', 'Ceres', 'Eris'}

print(astro1 ^ astro2) # {'Saturno'}
print(astro1.symmetric_difference(astro2)) # {'Saturno'} 

astro1.add('Netuno') # Adiciona um elemento
print(astro1) # {'Plutão', 'Ceres', 'Netuno', 'Eris'}

astro1.remove('Netuno') # Gera erro se não existir
print(astro1) # {'Plutão', 'Ceres', 'Eris'}

astro1.discard('Netuno') # Não gera erro
print(astro1) # {'Plutão', 'Ceres', 'Eris'}

astro1.pop() # Remove um elemento aleatório
print(astro1) # {'Ceres', 'Eris'}

astro1.clear() # Remove todos os elementos
print(astro1) # set()