from random import randint

while True:
    jogador = int(input("Escolha um numero :"))
    computador = randint(0,10)
    total = computador + jogador
    tipo= " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar [I/P]")).strip().upper()[0]
    print(f"Voce escolheu {jogador} e o computador {computador},o total  {total}")

    if tipo == "P":
        if total % 2 == 0 :
            print("VENCEU")
        else:
            print("PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1 :
            print("VENCEU")
        else:
            print("PERCEU")
    print("VAMOS JOGAR MAIS UMA")
print("FIM DO JOGO")