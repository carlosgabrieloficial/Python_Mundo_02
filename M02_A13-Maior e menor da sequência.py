# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maior = 0
menor = 0


for pessoa in range(1,6):
    peso_pessoa = float(input(f'Qual o peso da pessoa numero {pessoa} :'))
    if pessoa == 1 :
        maior = peso_pessoa
        menor = peso_pessoa
    else:
        if peso_pessoa > maior:
           maior = peso_pessoa 
        if peso_pessoa < menor:
           menor = peso_pessoa
    

print(f"O maior peso foi : {maior}\nE o menor peso foi : {menor}")
