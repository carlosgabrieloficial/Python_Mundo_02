#from math import factorial
#numero = int(input("Por favor informe o um numero : "))
#fatorial = factorial(numero)
#print(fatorial)


numero = int(input("Por favor informe um numero : "))

contador = numero
fatorial = 1 

print(f'Calculano o numero {numero} em fatorial é \n{contador} !', end=" = ")

while contador > 0 :
    print(f'{contador}', end=' ')
    print('x' if contador > 1 else ' = ', end= " ")
    fatorial *= contador
    contador -= 1

print(f"{fatorial}")