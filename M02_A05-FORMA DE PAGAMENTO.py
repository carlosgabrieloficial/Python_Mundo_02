#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

print('='*6,'LOJAS DO GUANABARA','='*6)
produto = float(input('Qual o valor da sua compra ?'))

print('Formas de pagamento')
print('[ 1 ] à vista em debito')
print('[ 2 ] à vista em credito')
print('[ 3 ] 2X no cartão')
print('[ 4 ] 3X ou mais no cartão')

pagamento = int(input('Qual é a opção ?'))

if  pagamento == 1 :
    desconto = produto-(produto*0.10)
    print('debito escolhido')
    print(f'O seu valor era {produto} e com o descoto o valor ficou {desconto} .')

elif pagamento == 2 :
    desconto = produto-(produto*0.05)
    print('credito escolhido')
    print(f'O seu valor era {produto} e com o descoto o valor ficou {desconto} .')

elif pagamento == 3 :

    print(f'O seu valor final da sua compra é {produto} e nao tem desconto.')

elif pagamento == 4 :
    desconto = produto + (produto * 0.20)
    parcela = int(input('quantas vezes voce planeja em em parcelar ? '))

    print('debito escolhido')
    print(f'O seu valor era {produto} e com os juros o valor ficou {desconto} .')
    print(f'e o numero de parcelas é {parcela} e o valor de cada parcela é {desconto/parcela}')

else:
    print('forma invalida, tente novamente')
    