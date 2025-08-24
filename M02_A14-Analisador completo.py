#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0 
media_idade = 0

for paciente in range (1,5):
    
    print('------ Clinica Vida + -------')
    nome = str(input ('Por favor ,informe o seu nome :'))
    idade = int(input('Por favor,informe a sua idade :'))
    soma_idade += idade
    sexo = str(input('Sexo [M] / [F] :')).strip()


media_idade = soma_idade / 4

print(media_idade)