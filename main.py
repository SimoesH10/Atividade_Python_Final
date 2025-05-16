def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """

    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f'Par')
    else:
        print(f'Impar')
        


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """

    import math
    texto = input("Digite o texto: ")
    tamanho = len(texto)
    meio = math.ceil(tamanho / 2)
    print(texto[meio:tamanho])


def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """

    numero = int(input("Digite um número para ver a tabuada: "))

    #print(numero)
    for i in range(1, 11):
        resultado = numero * i
        print(resultado,end=' ')

    


def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    preposicoes = ['da', 'de', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas', 'a', 'ao', 'aos', 'às']
    nome = input("Digite seu nome completo em letras minúsculas: ")
    palavras = nome.strip().split()

    for p in palavras:
        if p in preposicoes:
            palavra = p
        else:
            palavra = p[0].upper() + p[1:]
        print(palavra, end=' ')

def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """


    lado1 = int(input("Digite o valor do lado 1 do triângulo: "))
    lado2 = int(input("Digite o valor do lado 2 do triângulo: "))
    lado3 = int(input("Digite o valor do lado 3 do triângulo: "))

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

        if lado1 == lado2 == lado3:
            print("O triângulo é equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("O triângulo é isósceles")
        else:
            print("O triângulo é escaleno")
    else:
        print("Os valores informados não formam um triângulo válido")


def q6():
    '''
    Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. 
    Escrever um programa para ler o ano em que a criança toma a 1a dose e a 
    periodicidade (intervalo em anos) da vacina e exibir em que outros 
    anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.
    '''

    ano = int(input("Digite o ano da 1ª dose: "))
    intervalo = int(input("Digite o intervalo (em anos) entre as doses: "))

    for i in range(1, 4):
        print("Próxima dose em:", ano + i * intervalo)

def q7():
    '''
    Faça um programa que leia uma sequencia de números 
    e indique se eles são primos ou não.  
    Você deve parar ao ler o número -1.
    '''

    numeros = []

    while True:
        n = int(input("Digite um número (ou um valor negativo para encerrar): "))
        if n <= -1:
            break
        numeros.append(n)

    for n in numeros:
        if n % 2 == 0:
            print(n, "é par")
        else:
            print(n, "é ímpar")

def q8():
    '''
    Valquíria trabalha em uma padaria e foi roubada ontem. Seus clientes ficaram com 
    pena e resolveram organizar uma vaquinha para comprar um novo celular para ela. 
    Escreva um programa que receba como entrada o valor doado por cada cliente, até que 
    seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por eles.
    '''
    total = 0
    contador = 0

    while True:
        doacao = float(input("Digite o valor da doação (ou um valor negativo para encerrar): "))
        if doacao < 0:
            break
        total += doacao
        contador += 1

    if contador > 0:
        media = total / contador
        print(f"Total arrecadado: R${total:.2f}")
        print(f"Valor médio das doações: R${media:.2f}")
    else:
        print("Nenhuma doação foi feita.")

def q9():
    '''
    A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária,
      o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. 
      Cada quilômetro a mais custará uma taxa extra de R$ 12.

    Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada 
    por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.
    '''
    dias = int(input("Digite a quantidade de dias de aluguel: "))
    km_rodado = int(input("Digite a quilometragem total rodada: "))

    valor_diaria = 90
    km_incluso = 100
    taxa_extra = 12

    total = dias * valor_diaria

    if km_rodado > dias * km_incluso:
        km_extra = km_rodado - dias * km_incluso
        total += km_extra * taxa_extra

    print(f"Valor total a ser pago: R${total:.2f}")


def q10():
    '''
    Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário 
    para as outras escalas de medida.

    Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin 
    Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin 
    Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
    '''
    temperatura = float(input("Digite o valor em números da temperatura: "))
    escala = input("Digite a escala da temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

    if escala == 'C':
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = temperatura + 273.15
        print(f"{temperatura}°C é igual a {fahrenheit}°F e {kelvin}K")
    elif escala == 'F':
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temperatura}°F é igual a {celsius}°C e {kelvin}K")
    elif escala == 'K':
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temperatura}K é igual a {celsius}°C e {fahrenheit}°F")
    else:
        print("Escala inválida. Use C, F ou K.")



if __name__ == "__main__":
    q1()