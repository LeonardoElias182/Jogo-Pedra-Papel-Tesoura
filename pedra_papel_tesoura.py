import random

opcoes = ['pedra', 'papel', 'tesoura']

escolha = random.choice(opcoes)

jogador = input('Escolha entre pedra, papel ou tesoura: ')

print (f'Computador escolheu {escolha}')

if jogador == escolha:
    print ('Empate!')
elif jogador == 'pedra' and escolha == 'tesoura':
    print ('Você venceu! Parabéns!')
elif jogador == 'tesoura' and escolha == 'papel':
    print ('Você venceu! Parabéns!')
elif jogador == 'papel' and escolha == 'pedra':
    print ('Você venceu! Parabéns!')
else:
    print ('O computador venceu. Que pena!')

        



