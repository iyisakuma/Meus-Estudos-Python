#Conjunto - Set
##Não ordenado e que não aceita elementos duplicados
frutas = {'laranja', 'banana', 'uva', 'pera', 'laranja', 'uva', 'abacate'}
print(frutas)

##As operações básicas da matemática sobre o conjunto estão disponiveis
a = set('abacaxi')
b = set('abacate')
print(f'Conjunto a: {a} \nConjunto b: {b}')
print(f'União: {a | b}')
print(f'Intersecção: {a & b}')
print(f'Diferença: {a - b}')
print(f'Diferença simétrica: {a ^ b}')