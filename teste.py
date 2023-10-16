import os

while True:

    valor_dado = input('Digite o dinheiro recebido: ')
    valor_da_compra = input('Digite o valor total da compra: ')
    float_valor_dado = float(valor_dado)
    float_valor_da_compra = float(valor_da_compra)
    print('Somando seu troco...')

    if float_valor_dado > float_valor_da_compra:
        troco = float_valor_dado - float_valor_da_compra
        print(f'O troco é de {troco:.2f} R$')
    elif float_valor_dado < float_valor_da_compra:
        troco = float_valor_dado - float_valor_da_compra
        print(f'Está faltando {troco:.2f} R$')
    elif float_valor_dado == float_valor_da_compra:
        print('Não precisa de troco')
    else:
        print('Digite o numero corretamente')

    continuar = input('Deseja somar outro troco? [s]im [n]ão ')
    
    if continuar == 's':
        os.system('cls') # dependendo do seu sistema operacional, pode ser que o 'cls' não funcione, se der erro, substitua por 'clear'
        continue
    else:
        os.system('cls')
        break
