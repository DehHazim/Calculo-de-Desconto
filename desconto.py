valor = float(input('Qual o valor do produto? '))
desconto = valor - (valor * 5 / 100)

print('O preço do produto, que custava R${:.2f} com desconto de 5% vai custar R${:.2f}.'.format(valor, desconto))
