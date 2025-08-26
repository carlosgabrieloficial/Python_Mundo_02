#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo por favor [M]/[F]')).strip().upper()[0]

while sexo not in "MF":
    sexo = str(input("Informação incorreta, Por favor tente novamente,Informe o seu sexo por favor [M]/[F]")).strip().upper()[0]

print('Cadastro aprovado')
print(f'Cadastro como {sexo}')