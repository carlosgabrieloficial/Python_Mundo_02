numero = contador = soma = 0 
numero = int(input("Digite um numero [999 ele para]"))

while numero != 99:
    soma += numero
    contador += 1 
    numero = int(input("Digite um numero [999 ele para]"))
print(contador,soma)
