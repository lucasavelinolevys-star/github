# matriz 4x4 que mostra o maior numero que o usuario digitou
 
 
num1 = int(input("Dígite o número (inteiro) para a  : "))

num2 = int(input("Dígite o número (inteiro) para a  : "))

num3 = int(input("Dígite o número (inteiro) para a  : "))

num4 = int(input("Dígite o número (inteiro) para a  : "))

num5 = int(input("Dígite o número (inteiro) para a  : "))

num6 = int(input("Dígite o número (inteiro) para a  : "))

num7 = int(input("Digite o número (inteiro) para a  : "))

num8 = int(input("Digite o número (inteiro) para a  : ")) # deixaria mais simples se esse tanto de repetiçao
num9 = int(input("Digite o número (inteiro) para a  : "))

num10 = int(input("Dígite o número (inteiro) para a : "))

num11 = int(input("Dígite o número (inteiro) para a : "))

num12 = int(input("Dígite o número (inteiro) para a : "))

num13 = int(input("Dígite o número (inteiro) para a : "))

num14 = int(input("Dígite o número (inteiro) para a : "))

num15 = int(input("Dígite o número (inteiro) para a : "))

num16 = int(input("Dígite o número (inteiro) para a : "))
 
matriz = [

    [num1, num2, num3, num4],

    [num5, num6, num7, num8],    #criei a matriz com "[[]]" e com as varíaveis que criei la em cima

    [num9, num10, num11, num12],

    [num13, num14, num15, num16],

]
 
maior = matriz[0][0] # pega o primeiro número da matriz

# e guarda na variável maior
 
for linha in matriz : #aqui arruma cada linha da matriz

     print(linha)

     for numero in linha: #aqui arruma cada numero da matriz

        if numero > maior: #se o numero for maior

            maior = numero #o maior é igual a numero
 
print(f"Esse é o maior numero da matriz: {maior}") #mostrar o maior numero da matriz como explicado na linha 3


# lucas avelino: esse codigo ta com pouca explicaçao ta com alguns 
# erros de indentaçao e tiraria essa repeticao mas ta funcionando dou nota 8.
 