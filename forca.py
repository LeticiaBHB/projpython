import random

def jogar():
    lin()
    print('\033[4;46mBem Vindo ao jogo de forca!\033[m')
    lin()
    palavra_secreta = carrega_palavra_secreta()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) #temos uma parametro pra função
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    #enquanto não false e não false -> true and true
    while (not enforcou and not acertou):
        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas #o _ não deveria estar dentro das letras acetadas
        print(letras_acertadas)
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
#######
def lin():
        print('*' * 30)

def carrega_palavra_secreta():
        arquivo = open('palavras.txt', 'r')
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()
        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra] # a palavra secreta não existe dentro dessa função.
#uma função define um escopo, o escopo significa que as variáveias declaradas dentro dessa função só são visiveis dentro dessa função

def pede_chute():
    chute = str(input('qual letra?')).lower()
    chute = chute.strip()  # sem espaços
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0  # posição
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print(f'você perdeu! \n a palavra secreta era {palavra_secreta}')

def imprime_mensagem_vencedor():
    print('você ganhou!')

def desenha_forca(erros):
    print('_____\n|/   |')
    if(erros ==1):
        print('|   (_)  ')
        print('|        ')
        print('|        ')
        print('|        ')
    if(erros ==2):
        print('|   (_)  ')
        print('|   \    ')
        print('|        ')
        print('|        ')
    if(erros ==3):
        print('|   (_)  ')
        print('|   \|   ')
        print('|        ')
        print('|        ')
    if(erros == 4):
        print('|   (_)  ')
        print('|   \|/  ')
        print('|        ')
        print('|        ')
    if(erros == 5):
        print('|   (_)  ')
        print('|   \|/  ')
        print('|    |   ')
        print('|        ')
    if(erros == 6):
        print('|   (_)  ')
        print('|   \|/  ')
        print('|    |   ')
        print('|   /    ')
    if(erros ==7):
        print('|   (_)  ')
        print('|   \|/  ')
        print('|    |   ')
        print('|   / \  ')
    print('|        ')
    print('|____')
    print()
if __name__ =="__main__": #forca é o principal, se esse for o caso chama o jogar
    jogar()