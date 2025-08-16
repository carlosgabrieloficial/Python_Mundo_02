from datetime import date
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
atual = date.today().year
nasc  = int(input('ano de nascimento : '))
idade = atual - nasc
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if   idade == 18  :
     print('voce precisa se alistar ao serviço militar urgernte !!!')

elif idade > 18 :
     saldo = 18 - idade
     ano = atual + saldo
     print(f'voce tem mais de 18 anos , sua idade atual é {idade} e voce se alistou em {ano} logo')
     print('voce ja prestou serviço militar')

elif idade < 18 :
     saldo = 18 - idade
     ano = atual + saldo
     print(f'ainda falta {saldo} anos para vc se alistar no ano {ano}')
     print('voce ainda vai prestar o serviço militar')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


#-=-=-= fim do programa =-=-=-=-