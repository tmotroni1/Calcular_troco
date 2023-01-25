import os

while True:

    valor_dado = input('Digite o dinheiro recebido: ')
    valor_da_compra = input('Digite o valor total da compra: ')
    print('Somando seu troco...')

    if valor_dado > valor_da_compra:
        troco = float(valor_dado) - float(valor_da_compra)
        print(f'O troco é de {troco} R$')
    elif valor_dado < valor_da_compra:
        troco = float(valor_dado) - float(valor_da_compra)
        print(f'Está faltando {troco} R$')
    elif valor_dado == valor_da_compra:
        print('Não precisa de troco')
    else:
        print('Digite o numero corretamente')

    continuar = input('Deseja somar outro troco? [s]im [n]ão ')
    
    if continuar == 's':
        os.system('cls')
        continue
    else:
        os.system('cls')
        break