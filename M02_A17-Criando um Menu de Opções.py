from time import sleep

n1 = int(input("Digite um numero : "))
print('==='*20)
n2 = int(input("Digite outro numero: "))

opcao = 0
while opcao != 5:

    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros       
    [5] Sair do Programa               
""")
    
    opcao = int(input("Escolha uma opcao : "))

    if opcao == 1 :
        print('Somar' \
        f' {n1} + {n2}' \
        f' a soma é : {n1+n2}')

    elif opcao == 2 :
        print('[2] Multiplicar escolhida' \
        f'numero 1 {n1} * numero 2 {n2}' \
        f'a multiplicação é {n1*n2}')

    elif opcao == 3 :
        print('[3] Maior escolhida' \
        f'Entre o numero 1 {n1} e o numero 2 {n2}')
        if n1 > n2 :
            print('O Numero 1 é o maior')
        else:
            print('O numero 2 é o maior')
    
    elif opcao == 4 :
        print('[4] Novos numeros , escolhido')
        n1 = int(input("Por favor escolha um numero : "))
        n2 = int(input("Escolha um segundo numero   :"))
    
    elif opcao == 5 :
        print('finalizando')
    else:
        print('Opção invalida, Tente novamente')
    print("==="*20)
    sleep(2)
print('fim do programa')