
"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC3 - Exercício 1

"""

def determina_tipo_triangulo(l1, l2, l3):
    if l1 == 4 and l2 == 4 and l3 == 4:
        tri = ("Triangulo Equilatero")
    elif l1 == 2 and l2 == 4 and l3 == 4:
        tri = ("Triangulo Isósceles")
    elif l1 == 3 and l2 == 4 and l3 == 5:
        tri = ("Triangulo Escaleno")
    elif l1 == 1 and l2 == 1 and l3 == 4:
        tri = ("Não é triangulo ")
    return(tri)

print("Essa figura geométrica é:", determina_tipo_triangulo(1, 1, 4))


# Finalizado Ex1, segue Ex2 abaixo:

"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC3 - Exercício 2

"""

def dia_semana(dia):
   if dia == 1 :
    return "Domingo"
   elif dia == 2:
    return "Segunda-Feira"
   elif dia == 3:
    return "Terça-Feira"
   elif dia == 4: 
    return "Quarta-Feira"
   elif dia == 5: 
    return "Quinta-Feira"
   elif dia == 6: 
    return "Sexta-Feira"
   elif dia == 7: 
    return "Sábado"
   else:
    return "string inválida"
    
print(dia_semana(1))
    

# Finalizado Ex2, segue Ex3 abaixo:

"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC3 - Exercício 3

"""
# num1 = print(float(input("Informe um número: ")))
# num2 = print(float(input("Informe um número: ")))
# operacao = print(input("Informe a operação: "))
# if operacao == soma:
#     print(num1 + num2)
# def calculadora():
#   if operacao == soma:
#     soma = num1 + num2 , 
#     return soma,  "soma"
#   elif operacao == subtracao:
#     return num1 - num2 , "subtração"
#   elif operacao == multiplicacao:
#     return num1 * num2, "Multiplicação"
#   elif operacao == divisao:
#     return num1 / num2, "Divisão"
#   else:
#     return "Operação inválida"
# print(calculadora(2,3, "soma"))
