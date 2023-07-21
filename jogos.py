import forca
import adivinhacao2
#quando eu chamo o import ele já começa a executar mesmo sem eu chamar


def escolha_jogo():
    def linha():
        print('¨' * 30)
    linha()
    print(' ESCOLHA O JOGO ')
    linha()
    print('[1] FORCA \n[2] ADIVINHAÇÃO')

    jogo = int(input('qual o jogo?'))
    if jogo == 1:
        print('jogando forca')
        forca.jogar()
    elif jogo == 2:
        print('jogando adivinhação')
        adivinhacao2.jogar()

if __name__ == "__main__":
    escolha_jogo()


