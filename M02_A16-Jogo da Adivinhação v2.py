from random import randint
computador = randint(0 , 10)
tentativas = 0 

acertou = False

print
("""
Olá sou o seu computador , vamos jogar um jogo,
descubra um numero entre 0 a 10 que eu escolhir
""")

while not acertou :
    jogador = int(input("Escolha um numero entre 0 a 10 :"))
    tentativas += 1
    if jogador == computador:
        print("fim de jogo")
        acertou = True
    else:
        if jogador < computador :
            print("Escolha um numero maior")
        else:
            print('Escolha um numero menor')

print(f"O computador escolheu esse numero{computador}")
print(f"E você teve {tentativas} tentativas para acertar")