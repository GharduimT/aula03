# titulo
# enunciado("Sabendo que hoje é o dia do desconto de 13 por cento em qualquer camiseta que voce comprar desenvova um programa para que você possasaber o valor do desconto e o valor final de uma camiseta que na semana passada, você viu que estava or um valor de Rs83')#
# processamento#
print('EXERCÍCIO 01')

preco = (int(input('informe o valor da camisa: ')))
desconto = preco * (13 / 100)
valor_final = (preco - desconto)
print('o valor do descontto é: ', desconto)

print('O valorfinal da camisa é: ', valor_final)


# código do professor#

preco = 83.0
desconto = preco * (13/100)
val_final = preco - desconto

print(val_final)