numero = int(input("QUANTOS NUMEROS VOCE QUER MOSTRAR"))
termo01 = 0 
termo02 = 1 

print(f"{termo01},{termo02}", end=" ")
contador = 3

while contador <= numero:
    termo03 = termo01+termo02
    print(f"{termo03}", end=" ")
    termo01 = termo02
    termo02 = termo03
    contador += 1
print("FIM ")