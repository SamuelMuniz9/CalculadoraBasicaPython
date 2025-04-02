import os
#uma das coisas que tive que pensar foi a parte dele funcionar com mais de 2 numeros fixos
#dar a opçao para o usuario utilizar quantos numeros ele quiser.  
def soma (numeros): 
    return sum(numeros)

def subtracao(numeros): 
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicacao(numeros): 
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def divisao(numeros): 
    resultado = numeros[0]
    for num in numeros[1:]:
        if num == 0:
            return "Erro, divisão por zero. "
        resultado /= num
    return resultado

def menu(): 

    while True: 
        print('''
    Calculadora feita por- Samuel Muniz
           Bem vindo!!! 
          1- soma
          2- subtração
          3- multiplicação
          4- divisão 
          5- sair

 ''')
        try: 
            opcao=int(input("Selecione uma das opções:"))
            if opcao == 5: 
                print("Fim do progama!")
                break

            numeros = input("Digite os números separados por espaço: ").split()
            os.system("cls")

            #convertando os numeros da string para float 
            try:  
                numeros = [float(num) for num in numeros]
            except ValueError: 
                print("Erro.Todos os valores devem ser numeros")

            if opcao == 1:
                print(f"A soma é: {soma(numeros)}")
            elif opcao == 2: 
                print(f"A subtração é:  {subtracao(numeros)}")
            elif opcao == 3:
                print(f"A multiplicação é:  {multiplicacao(numeros)}")
            elif opcao == 4: 
                print(f"A divisão é:  {divisao(numeros)}")
            else: 
                print("numero inserido indisponivel")

            input("Pressione qualquer tecla para continuar")

        except ValueError:
            print("Erro. Entrada inválida")


menu()