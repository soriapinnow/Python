conjunto = {1, 2, 3, 4, 5}
conjunto2={5, 6, 7, 8}
print(conjunto,conjunto2)
conjunto_uniao = conjunto2.union(conjunto)
print (conjunto_uniao)
conjunto_interseccao = conjunto2.intersection(conjunto)
print(conjunto_interseccao)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_diff_simetrica))
conjunto_a = {1, 2 ,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset=conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de b: {}'.format(conjunto_subset))
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é um superconjunto de b ? {}'.format(conjunto_superset))
lista = ['cachorro', 'cachorro', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)