# Aluno aprovado ou reprovado dependendo das suas notas
 
# Variável pedindo o nome do aluno
nome = input("Digite o nome do aluno: ")
 
# Duas variáveis que pedem as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
 
# Calcula a média somando as três notas e dividindo por 3
media = (nota1 + nota2 + nota3) / 3
 
# Mostra a média calculada
print("Média:", media)
 
# Verifica a situação do aluno baseado na média
if media >= 7:
    print(nome, "foi aprovado!")
elif media >= 5:
    print(nome, "está de recuperação!")
else:
    print(nome, "foi reprovado!")
 

#lucas avelino: dou nota 7 pra esse codigo ta basico teve alguns 
# erros de indentaçao mas esta funcionando


