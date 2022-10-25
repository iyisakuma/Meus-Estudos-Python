# # Uma lista é uma sequencia de valores onde cada valor é índice iniciado por 0.
# ## Forma de inicialização de uma lista:
# ### lista de inteiros
# lista1 = [1, 3, -5]
# ### lista de string
# lista2 = ['python', 'java', 'c#']
# ## Uma lista sempre inicia com o índice 0
# print( f'primeiro elemento da lista de inteiro é {lista1[0]} e o primeiro elemento da lista de String é {lista2[0]}')\
# ## Contudo se pode ter uma lista heterogenea, como a seguir:
# lista = [1, 2, 'python', 3.5, 'java']
# print('Printando todos os elementos da lista heterogenea: ')
# for elemento in lista:
#     print(elemento, end=' ')
# ## As listas podem possuir índices negativos, sendo assim os elementos começam de trás para frente
# print(lista[-1])

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
tentativas = 0
# while tentativas < 4:
#     mes = int(input('Escolha um mês (1 - 12): '))
#     if 1 <= mes < 13:
#         print('O mês é {}'.format(meses[mes-1]))
#     tentativas += 1
# ## Podemos pegar os elementos da lista em fatias:
# ### Por exemplo:
# #### Apenas n, nesse caso 2, elementos
# print('Printando apenas 2 elementos da lista de meses')
# for mes in meses[:2]:
#     print(mes, end=' ')
# #### Excluindo o n, nesse caso 2, elementos inicias da lista
# print('\nPrintando todos os elementos da lista, exceto 2 elementos iniciais.')
# for mes in meses[2:]:
#     print(mes, end=' ')
# #### fatiando a lista
# print('\nPrintando a partir do 3 elemento elemento até o 6, ou seja, de Março à Junho ')
# for mes in meses[2:6]:
#     print(mes, end=' ')
# ##### Obs: os índices podem ser números negativos e além disso, a nomenclatura [n:m] pode ser lido como de n até m
# ### Usa-se append para adicionar so um elemento a lista e extend para adicionar mais de um elemento de uma vez
lista = []
print(f'Adicionando um elemento a lista vazia: {lista}' )
lista.append('primeiro elemento adicionado')
print(f'Lista: {lista}')
print('Adicionando mais de um elemento a lista de uma unica vez')
lista.extend(['segundo elemento', 'terceiro elemento'])
print(f'Lista: {lista}')
