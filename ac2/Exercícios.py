
"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC2 - Ex1: parte 1
"""

def eq_seg_grau(a, b, c):
    delta = (b ** 2) - 4 * a * c
    x1 = (((-1)*b) + (delta**0.5))/(2*a)
    x2 = (((-1)*b) - (delta**0.5))/(2*a)
    return(x1, x2 )

print(eq_seg_grau(1, -6, 8))


"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC2 - Ex1: parte 2
"""

def bissexto(ano):
    ano = ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0 )
    return(ano)
print(bissexto(2000))

# Finalizado Ex1, segue Ex2 abaixo

"""
Programação Estruturada
2024.1
11/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC2 - Ex2

"""

def calculadora_salario(valor_hora, num_horas, irpf=0.275):
      
        salario = (valor_hora*num_horas)
        imposto = irpf * salario
        salario = (salario - imposto)
        return(round(salario,2))
print(calculadora_salario(25, 15))
