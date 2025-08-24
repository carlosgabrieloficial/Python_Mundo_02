num = int(input('Digite um numero :'))
total = 0

for c in range (1, num+1):
    if num % c == 0 :
        print('\033[034m',end=' ')
        total +=1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
print(f'\nO numero é {num}\ne foi divisivel {total}')

if total == 2:
    print('esse numero é primo')
else:
    print('esse numero não é primo')