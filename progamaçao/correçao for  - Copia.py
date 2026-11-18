# Aluno aprovado ou reprovado dependendo da suas notas


# variavel pedindo o nome do aluno
nome = input("Digite o nome do aluno: ")

# dua variavel que pede as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# calcula a média usando uma variavel para guardar o calculo das duas notas divido por 3
media = (nota1 + nota2 + nota3) / 3

# mostra a variavel media que esta o calculo
print("Média:", media)

# verifica se ele tirou mais que 7
if media >= 7:
    print(nome, "foi aprovado!") # se ele tirou mais que 7 ele foi aprovado

elif media >= 5:
    print(nome, "está de recuperação!") # se ele tirou 5 esta de recuperação 

else:
    print(nome, "foi reprovado!") # se nao esta reprovado



# lucas avelino: dou nota 9 ta funcionando ta com alguns erros de indentaçoes e colocaria mais comentarios mais em geral ta ok