print("-=-="*20)
numero = int(input("Gostaria de ver tabuada de qual numero ?"))
print("-=-="*20)

while numero >= 0 :
    for numeros in range(1,11):
        print(f"{numero}  X {numeros} = {numero*numeros}")
    numero = int(input("Gostaria de ver tabuada de qual numero ?"))
print("tente novamente")
numero = int(input("Gostaria de ver tabuada de qual numero ?"))