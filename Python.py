print ('|----------------------------PIZZARIA PIZZA PLANET ------------------------------------| ')
print ('|                                                                                      | ')
print ('|        Olá! Seja Bem Vindo a nossa Pizzaria, Qual sabor deseja degustar hoje?        | ')
print ('|                                                                                      | ')
print ('|--------------------------------------------------------------------------------------| ')
print ('|             |               |                             |                          | ')
print ('|   CODIGO    | SABORES       |       PIZZA MÉDIA (M)       |     PIZZA GRANDE (G)     | ')
print ('|     01      | NAPOLITANA    |        R$ 20,00             |      R$25,00             | ')
print ('|     02      | FRANGO        |        R$ 21,00             |      R$26,00             | ')
print ('|     03      | ESPANHOLA     |        R$ 22,00             |      R$27,00             | ')
print ('|     04      | ITALIANA      |        R$ 23,00             |      R$28,00             | ')
print ('|     05      | 4 QUEIJOS     |        R$ 24,00             |      R$29,00             | ')
print ('|     06      | MARGUERITA    |        R$ 25,00             |      R$30,00             | ')
print ('|     07      | CAIPIRA       |        R$ 26,00             |      R$31,00             | ')
print ('|     08      | CALIFORNIA    |        R$ 27,00             |      R$32,00             | ')
print ('|     09      | BRIGADEIRO    |        R$ 28,00             |      R$33,00             | ')
print ('|     10      | ROMEU JULIETA |        R$ 29,00             |      R$34,00             | ')
print ('|             |               |                             |                          | ')
print ('|--------------------------------------------------------------------------------------| ')
acumulador = 0
while True:
  tamanho = input("Qual o tamanho da pizza desejada? (M) ou (G)? " )
  tamanho = tamanho.upper()
  print ("------------------------------------------------------------")
  if tamanho != 'M' and tamanho != 'G' :
    print ("Opção inválida, digite apenas tamanhos existentes!")
    continue

  codigo = input('Qual o codigo do sabor da pizza desejada? ')
  if codigo != '01' and codigo != '02' and codigo != '03' and codigo != '04' and codigo != '05' and codigo != '06' and codigo != '07' and codigo != '08' and codigo != '09' and codigo != '10' :
    print ("Opção inválida, digite apenas sabores que existem!")
    continue
    print ("------------------------------------------------------------")
  if codigo == '01' and tamanho == 'M':
    print('voce escolheu a pizza napolitana  tamanho M')
    acumulador = acumulador + 20

  elif codigo == '01' and tamanho == 'G':
    print('voce escolheu a pizza napolitana  tamanho G')
    acumulador = acumulador + 25

  elif codigo == '02' and tamanho == 'M':
    print('voce escolheu a pizza de Frango  tamanho M')
    acumulador = acumulador + 21

  elif codigo == '02' and tamanho == 'G':
    print('voce escolheu a pizza Frango  tamanho G')
    acumulador = acumulador + 26

  elif codigo == '03' and tamanho == 'M':
    print('voce escolheu a pizza Espanhola tamanho M')
    acumulador = acumulador + 22

  elif codigo == '03' and tamanho == 'G':
    print('voce escolheu a pizza Espanhola  tamanho G')
    acumulador = acumulador + 27

  elif codigo == '04' and tamanho == 'M':
    print('voce escolheu a pizza Italiana  tamanho M')
    acumulador = acumulador + 23

  elif codigo == '04' and tamanho == 'G':
    print('voce escolheu a pizza Italiana  tamanho G')
    acumulador = acumulador + 28

  elif codigo == '05' and tamanho == 'M':
    print('voce escolheu a pizza de 4 Queijos  tamanho M')
    acumulador = acumulador + 24

  elif codigo == '05' and tamanho == 'G':
    print('voce escolheu a pizza 4 Queijos  tamanho G')
    acumulador = acumulador + 29

  elif codigo == '06' and tamanho == 'M':
    print('voce escolheu a pizza de Marguerita  tamanho M')
    acumulador = acumulador + 25

  elif codigo == '06' and tamanho == 'G':
    print('voce escolheu a pizza de Marguerita  tamanho G')
    acumulador = acumulador + 30

  elif codigo == '07' and tamanho == 'M':
    print('voce escolheu a pizza Caipira  tamanho M')
    acumulador = acumulador + 26

  elif codigo == '07' and tamanho == 'G':
    print('voce escolheu a pizza Caipira  tamanho G')
    acumulador = acumulador + 31

  elif codigo == '08' and tamanho == 'M':
    print('voce escolheu a pizza California  tamanho M')
    acumulador = acumulador + 27

  elif codigo == '08' and tamanho == 'G':
    print('voce escolheu a pizza California  tamanho G')
    acumulador = acumulador + 32

  elif codigo == '09' and tamanho == 'M':
    print('voce escolheu a pizza de Brigadeiro  tamanho M')
    acumulador = acumulador + 28

  elif codigo == '09' and tamanho == 'G':
    print('voce escolheu a pizza de Brigadeiro  tamanho G')
    acumulador = acumulador + 33

  elif codigo == '10' and tamanho == 'M':
    print('voce escolheu a pizza de Romeu e Julieta  tamanho M')
    acumulador = acumulador + 29

  elif codigo == '10' and tamanho == 'G':
    print('voce escolheu a pizza de Romeu e Julieta  tamanho G')
    acumulador = acumulador + 34
  print ("------------------------------------------------------------")

  pedir_mais =input('deseja pedir mais alguma pizza?  S (sim) | Qualquer tecla (não):')
  pedir_mais = pedir_mais.upper()
  if pedir_mais == 'S':
    continue
  else:
    print ("--------------------------------------------------")
    print('O total do seu pedido é: R${:.2f}' . format(acumulador))
    break
print ("------------------------------------------------------------")