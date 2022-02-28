
print('Bem vindo a Loja do Leonardo Estigarribia Silva')
valor = float(input('Entre com o valor do produto: '))
quant = int(input('Entre com o valor da quantidade: '))

valortotal = valor * quant
print('O valor total sem desconto é R${:.2f}'.format(valortotal))

if quant <= 9:
    desconto = valortotal - (valortotal * 0.00)
    print('O valor total com desconto de 0% é R${:.2f}'.format(desconto))
elif quant > 9 and quant <= 99:
    desconto = valortotal - (valortotal * 0.05)
    print('O valor total com desconto de 5% é R${:.2f}'.format(desconto))
elif quant > 99 and quant <= 999:
    desconto = valortotal - (valortotal * 0.10)
    print('O valor total com desconto de 10% é R${:.2f}'.format(desconto))
else:
    desconto = valortotal - (valortotal * 0.15)
    print('O valor total com desconto 15% é R${:.2f}'.format(desconto)) 