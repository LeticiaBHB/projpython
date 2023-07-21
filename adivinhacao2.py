import random
def jogar():
    def lin():
        print('*'*30)


    lin()
    print('\033[4;46mBem Vindo ao jogo de adivinhação!\033[m')
    lin()

    #número_secreto = round(random.random() * 100) #round ele gera um numero entre 0.0 e 1.0 -> ele arredonda
    número_secreto = random.randrange(1,101)
    total = 0
    pontos = 1000

    print(f'qual nível de dificuldade vocÊ quer?\n [1] FÁCIL \n [2] MÉDIO \n [3] DIFÍCIL {número_secreto}')
    nível = int(input('defina o nível:'))
    if(nível == 1):
        total = 20
    elif (nível ==2):
        total = 10
    else:
        total = 5

    for rodada in range(1, total +1):
        n1 = str(input('digite um número de 1 a 100:'))
        n = int(n1)  # assim posso conver ter str para int
        print(f'você digitou {n}')

        if (n <1 or n > 100):
            print('vocÊ deve digitar um número entre 1 e 100!')
            continue#irmão do break, ele não sai do laço

        acertou = n == número_secreto
        maior = n > número_secreto
        menor = n < número_secreto
        print(f'tentativa {rodada} de {total}')
        if acertou:
            print(f'\033[32mvocê acertou e fez {pontos} pontos!\033[m')
            break #sai do laço, ela não vai continuar mais se ele acertar
        else:
            if maior:
                print('\033[31mvocê errou, seu chute foi maior\033[m')
            elif menor:
                print('\033[31mvocê errou, seu chute foi menor\033[m')
            pontos_perdidos = abs(número_secreto - n)#numero secreto - o chute. ex: 40-20=20, ex:60-40=-20 -> função absoluto ele tira a negatividade
            pontos = pontos - pontos_perdidos

        #não preciso incrementar pq o for internamente já faz isso pra mim. rodada = rodada + 1 -> vantagem do for
    print(f'o palpite era {número_secreto}')
    print('fim do jogo')

if(__name__ == "__main__"): #quando opython roda diretamente essa página advinhacao2, e ele é o programa principal, ele é o main ele seta a variável
    jogar()