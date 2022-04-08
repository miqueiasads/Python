import os
def decimabin(inteiro, fracao=0):
    calculo = ''
    while inteiro > 0:
        res = inteiro // 2
        al_bin = inteiro % 2
        inteiro = res
        calculo += str(al_bin)
    calculo = calculo[::-1]
    # partedecimal
    result = ''
    imp = ''
    cal_rest = fracao / 100
    for i in range(0, 5):
        resulta = cal_rest * 2
        inte = int(resulta)
        string = str(inte)
        imp += string
        cal_rest = resulta
    if imp == 1:
        cal_rest = cal_rest - 1
         
    return (calculo, imp)

# codigo decimal para octal

def decimaaoctal(x):
    resultado = ''
    while x > 0:
        resultado = str(x % 8) + resultado
        x = int(x / 8)
    return resultado

# codigo de decimal para hexadecimal

def decahex(x):
    hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    resultado = []
    impressao = ''
    while x > 0:
        resultado.append(hexa[(x % 16)])
        x = x // 16

    for indice in resultado:
        impressao += str(indice)

    return impressao[::-1]

# binario para decimal
def bpd(x):
    x = str(x)
    x = x[::-1]
    lista = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024']
    res = ''
    conversor = 0
    for con in range(len(x)):
        if x[con] == '1':
            res = lista[con]
            conversor += int(res)

    return conversor

# octal para decimal
def opd (numero):
    resposta = []
    soma = 0
    numero = str(numero)
    numero = numero[::-1]
    cont = 0
    for num in numero:
        num = int(num)
        resposta.append(num)
    for i in resposta:
        soma += i * (8 ** cont)
        cont += 1
    return soma

# decimal para hexadecimal

def hexdec(x):
    num = int(x, 16)
    return num

def main():
    os.system("cls")
    while True:
        print('SELECIONE UMA OPÇÃO DE CONVERSAO:\n'
              '1 - DEC > BIN\n'
              '2 - DEC > OCT\n'
              '3 - DEC > HEX\n'
              'PARA REALIZAR O INVERSO\n'
              'DUPLIQUE O OPÇÃO\n'
              'EX: 11 - BIN > DEC')
        print(30 * '-')
        acao = int(input("> "))
        os.system("cls")
        if acao == 1:
            num = int(input('DIGITE O VALOR:'))
            print('O resultado da conversão é:',decimabin(num))
        elif acao == 2:
            num = int(input('DIGITE O VALOR:'))
            print('O resultado da conversão é:',decimaaoctal(num))
        elif acao == 3:
            num = int(input('DIGITE O VALOR:'))
            print('O resultado da conversão é:',decahex(num))
        elif acao == 11:
            num = map(input('DIGITE O VALOR:').split(","))
            print('O resultado da conversão é:',bpd(num))
        elif acao == 22:
            num = int(input('DIGITE O VALOR:'))
            print('O resultado da conversão é:',opd(num))
        elif acao == 33:
            num = input('DIGITE O VALOR:')
            print('O resultado da conversão é:',hexdec(num))

main()
