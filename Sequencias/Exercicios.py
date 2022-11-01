#1.
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8 ,3,3, -52]
##a
print(f'Maior elemento da lista é {max(lista)}')
##b
print(f'Menor elemento da lista é {min(lista)}')
##c
print('Os números pares são: ', end=' ')
for x in lista:
    if x % 2 == 0 :
        print( x, end=' ')
print()
##d
primeiro_elemento = lista[0]
contador  = 0
for x in lista:
    if x == primeiro_elemento:
        contador += 1
print(f'O primeiro elemento {primeiro_elemento} foi repetido {contador} vezes')
##e
valor_total = 0
for x in lista:
    valor_total += x
print(f'A média é {valor_total / len(lista)}')
##f
valor_total_negativo = 0
for x in lista:
    if x < 0:
        valor_total_negativo += x
print(f'Valor total negativo é {valor_total_negativo}')