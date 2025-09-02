
        
primeiro = int(input("PRIMEIRO TERMO :"))
razao = int(input("RAZAO : "))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0 :
    total = total + mais
    while contador <= total:
        print(f"{termo} --->", end=" ")
        termo += razao
        contador += 1
    print("PARA")
    mais = int(input("Quanto mais"))

print("ACABOU")

