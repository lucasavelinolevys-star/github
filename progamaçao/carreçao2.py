# aqui recebe um número digitado pelo usuário
num = float(input("Digite um número: "))

# ja essa condição verifica se o número é negativo menor que 0
if num < 0:
    print("Número negativo")

# aqui verifica se é positivo e par
# % 2 significa o resto da divisão por 2
# se o resto for 0, é par
elif num > 0 and num % 2 == 0:
    print("Positivo e par")

# verifica se é positivo e ímpar
# se o resto da divisão por 2 for diferente de 0, é ímpar
elif num > 0 and num % 2 != 0:
    print("Positivo e ímpar")

# se não entrou em nenhuma condição acima, então é zero
else:
    print("Zero")