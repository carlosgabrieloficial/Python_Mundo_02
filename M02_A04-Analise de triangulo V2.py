# mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

r1 = int(input('diga o valor da primeira linha :'))
r2 = int(input('diga o valor da segunda linha  :'))
r3 = int(input('diga o valor da terceira linha :'))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2 :
    print('podem formar segmentos')

    if  r1==r2==r3 :
        print('esse trinagulo é equielatero')

    elif r1 != r2 != r3 != r1 :
        print('esse triangulo é escaleno')

    else :
        print('esse triangulo e isoscales')

else:
    print('nao podem formar segmento')