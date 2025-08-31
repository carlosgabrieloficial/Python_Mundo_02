primeiro = int(input("Por favor diga um numero : "))
razao = int(input("Qual a razão : "))
contador = 0
termo = primeiro

print(f"O primeiro termo é")

while contador <= 9:
    print(f"{termo}->", end=' ')
    termo += razao
    contador += 1  

