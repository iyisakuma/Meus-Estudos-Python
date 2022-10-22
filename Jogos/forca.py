def print_menu():
    print(
        "*************************************************************************************************************")
    print(
        "****************************************Bem-vindo ao jogo da Forca!******************************************")
    print(
        "*************************************************************************************************************")
def print_chutes(letras_chutadas):
    print('Letras chutadas: ', end='')
    for letra in letras_chutadas:
        print( letra + ' - ', end='')
    print()
def to_string(list):
    string = ''
    for letra in list:
        string += letra
    return string

print_menu()
palavra_secreta='banana'
letra_acertadas = ['*', '*', '*' ,'*', '*','*']
letras_chutadas = []
numero_tentativas = 3
acertou = False
enforcou = False
while not acertou and not enforcou:
    if len(letras_chutadas) != 0:
        print_chutes(letras_chutadas)
    print('Qual a letra? ' + to_string(letra_acertadas) )
    chute = input('--> ')
    if chute in letras_chutadas:
        print('Letra ja utilizada!')
        continue
    elif chute.upper() in palavra_secreta.upper():
        print('Otima tentiva')
        contador = 0
        for letra in palavra_secreta:
            if chute == letra:
                letra_acertadas[contador] = chute
            contador += 1
        if to_string(letra_acertadas) == palavra_secreta:
            acertou = True
    else :
        numero_tentativas -= 1
        if numero_tentativas == 0:
            enforcou = True
    letras_chutadas.append(chute)
print('Resposta: ' + palavra_secreta)
print('Fim do jogo')


