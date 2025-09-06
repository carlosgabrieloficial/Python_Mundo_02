total18 = totalM = total20F = 0

while True:
    idade = int(input("Digite a sua idade :"))

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]  :")).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == "M":
        totalM += 1
    elif sexo == "F":
        total20F += 1
    
    resposta = " "
    while resposta not in "NS" :
        resposta = str(input("Quer continuar [N/S] : ")).strip().upper()[0]
    if resposta == "N":
        break
        
print(idade)
print(total18)
print(total20F)
print(totalM)
    
        

    