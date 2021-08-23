def jogar():

    print("*****bem-vindo******")
    print("jogo de adivinhação")

    import random
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 100

    print("nivel de dificuldade: ")
    print("(1) fácil (2)médio (3)díficl ")
    nivel = int(input("escolha o nivel de dificuldade : "))

    if( nivel == 1 ):
        total_de_tentativas = 15
    elif( nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1 ,total_de_tentativas + 1 ):
        print("Tentaivas {} de {} ". format(rodada,total_de_tentativas))
        chute_str = input(" escolha um número de 1 a 100 : ")
        print("você digitou :",chute_str)
        chute =int(chute_str)
        if(chute < 1 or chute > 100):
            print("você deve digitar um numero entre 1 e 100 ")
            continue
        acertou = chute  == numero_secreto
        maior =   chute >   numero_secreto
        menor =   chute <   numero_secreto

        if(acertou):
            print("Você acertou! e fez {} pontos de 100".format(pontos))
            break
        else:

            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("fim do jogo")
    print("o numero escolhido foi",numero_secreto)

def tentardenovo():
    print("Quer jogar novamente ? ")
    print("(1)sim (2)não")
    novatentativa = int(input("escolha 1 ou 2 : "))
    if (novatentativa == 1):
        print("Mais uma vez")
        jogar();
    else:
        print("Até a proxima");


jogar();
tentardenovo();
