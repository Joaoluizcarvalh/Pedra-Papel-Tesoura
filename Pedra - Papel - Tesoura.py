from random import randint
from time import sleep
computador = randint(0, 2)
lista = ('PEDRA', 'PAPEL', 'TESOURA')
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua opção:'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print('Computador escolheu {}'.format(lista[computador]))
print('Jogador escolheu {}'.format(lista[jogador]))
print('-=' * 15)
if computador == 0:      # Computador escolheu PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VOCÊ VENCEU :(')
    elif jogador == 2:
        print('JOGADOR PERDEU HAHAH')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 1:    # Computador escolheu PAPEL
    if jogador == 0:
        print('JOGADOR PERDEU HAHAH')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VOCÊ VENCEU :(')
    else:
        print('OPÇÃO INVALIDA')
elif computador == 2:    # Computador escolheu TESOURA
    if jogador == 0:
        print('JOGADOR VOCÊ VENCEU :(')
    elif jogador == 1:
        print('JOGADOR PERDEU HAHAH')
    elif jogador == 2:
        print('EMPATE')
else:
    print('OPÇÃO INVALIDA')
