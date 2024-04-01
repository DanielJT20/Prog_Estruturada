"""
Programação Estruturada
2024.1
01/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - 1 

"""

print("Hello World!")

"""
Programação Estruturada
2024.1
01/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - 2 
"""

A = int(input())
B = int(input())

X = (A + B)

print("X =", X)

"""
Programação Estruturada
2024.1
01/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - 3
"""

total = 0
for i in range(2):
    item = input().split(" ")
    cod = int(item[0])
    qtd = int(item[1])
    valor = float(item[2])
    total = total + qtd*valor
print("VALOR A PAGAR: R$ %.2f" %total)


"""
Programação Estruturada
2024.1
01/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - 4 
"""


a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorC = (maiorAB + c + abs(maiorAB - c))/2

print("%.0f eh o maior" %maiorC)

"""
Programação Estruturada
2024.1
01/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC6 - 5
"""


import math

x1, y1 = input(). split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
distancia= math.sqrt (((x2 - x1)**2)+(y2 - y1)**2)
print("%.4f" %distancia)

