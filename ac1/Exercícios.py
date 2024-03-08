
"""
Programação Estruturada
2024.1
08/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC1 - 1
"""

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

x1 = (((-1)*b) + (delta**0.5))/(2*a)

x2 = (((-1)*b) - (delta**0.5))/(2*a)

print("As raizes da equação são:", round(x1, 3) ,"e", round(x2, 3))


# Exercício terminado, segue o outro a baixo:

"""
Programação Estruturada
2024.1
08/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC1 - 2
"""

ano = int(input("Informe um ano: "))

print(((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0 )) 
