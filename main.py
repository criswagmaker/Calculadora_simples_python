def calculadora ():
    operação = input('''
\nEscolha uma operação matemática que deseja efetuar

+ Soma
- Subtração
* Multiplicação
/ Divisão\n
''')
    
    if operação == "+":
        n1 = int(input("Insira um número: "))
        n2 = int(input("Outro número: "))
        soma_resultado = n1 + n2
        print(f'O resultado da soma entre {n1} e {n2} é igual a {soma_resultado}')

    elif operação == "-":
        n1 = int(input("Insira um número: "))
        n2 = int(input("Outro número: "))
        sub_resultado = n1 - n2
        print(f'O resultado da subtração entre {n1} e {n2} é igual a {sub_resultado}')

    elif operação == "*":
        n1 = int(input("Insira um número: "))
        n2 = int(input("Outro número: "))
        multi_resultado = n1 * n2
        print(f'O resultado da multiplicação entre {n1} e {n2} é igual a {multi_resultado}')

    elif operação == "/":
        n1 = int(input("Insira um número: "))
        n2 = int(input("Outro número: "))
        div_resultado = n1 / n2
        print(f'O resultado da divisão entre {n1} e {n2} é igual a {div_resultado}')

    else:
        print('Você não digitou um valor válido, por favor, inicie o programa novamente.')
    
    continuar()

def continuar():
    continuar = input(
        '''
        Você deseja realizar outro calculo?
        Y/y = SIM
        N/n = NÃO
        '''
    )

    if continuar == "Y" or "y":
        calculadora()

    elif continuar == "N" or "n":
        print("Até a próxima!!")

    else:
        print("Até a próxima!!")
        continuar()

calculadora()


