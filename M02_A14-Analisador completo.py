#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0 
media_idade = 0
maioridade_homem = 0 
nome_homemvelho = 0
total_mulheres = 0 


for paciente in range (1,5):
    
    print('------ Clinica Vida + -------')
    nome = str(input ('Por favor ,informe o seu nome :'))
    idade = int(input('Por favor,informe a sua idade :'))
    soma_idade += idade
    sexo = str(input('Sexo [M] / [F] :')).strip()
   
    if sexo in "Ff" and idade > 20 :
        total_mulheres += 1

    if paciente == 1 and sexo in "Mm":
        nome_homemvelho = nome
        maioridade_homem = idade

    if sexo in "Mm" and idade > maioridade_homem:
        maioridade_homem = idade
        nome_homemvelho = nome


media_idade = soma_idade / 4

print(f"A media entre todos os paciantes é {media_idade}")

print(f'O homem mais velho é o {nome_homemvelho} e a sua idade é {maioridade_homem}')

print(f'Tem o total de {total_mulheres} mulheres acima dos 20 anos')