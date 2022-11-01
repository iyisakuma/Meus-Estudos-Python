#Tuplas
## Tuplas é uma lista imutavel, porém se usa parênteses como delimitador, podendo omitir parenteses
dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
print(f"{dias} é um {type(dias)}")
## Pode se criar tupla a partir de tipos iteráveis como listas e string
lista = [1, 2, 4, 5]
print(tuple(lista))

##Quando é necessário armazenar uma coleção de dados que não possa ser alterada, prefira usar tuplas
##a lista. Outra vantagem é que tuplas podem ser usadas como chaves de dicionários.