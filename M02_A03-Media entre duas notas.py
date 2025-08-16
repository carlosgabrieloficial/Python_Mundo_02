#calcule a média de duas notas
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
num_1 = float(input('primeira nota :'))
num_2 = float(input('segunda nota  :'))
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
notas = [num_1,num_2]
soma  = sum(notas)
div   = len(notas)
media = soma/div
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
print(f'a primeira nota é {num_1}, e a segunda nota é {num_2}')
print(f'a soma das notas é {soma} e a media é {media} ')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
if   media < 5.0 :
     print('REPROVADO')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
elif 5.0 < media < 6.9 :
     print('RECUPARAÇÃO')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
elif media >= 7:
     print('APROVADO')
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=