primeiro = int(input("Por favor diga um numero : "))
razao = int(input("Qual a razão : "))
contador = 1
termo = primeiro

print("O primeiro termo é")

while contador <= 10:
    print(f"{termo} --> ", end='')
    termo += razao
    contador += 1  

print("FIM DO PROGRAMA")

