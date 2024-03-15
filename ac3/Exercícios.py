
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

def soma(num1, num2):
  return num1 + num2

def subtracacao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0 : 
    return "Divisão por zero"  
  else:
    return(num1/num2)
   
def calcular():

  num1 = int(input("Informe um número: "))
  num2 = int(input("Informe outro número: "))
  operacao = input("Informe a operação: ")

  if operacao == "soma":
    resultado = soma(num1, num2)
  elif operacao == 'subtracao':
    resultado = subtracacao(num1, num2)
  elif operacao == 'multiplicacao':
    resultado = multiplicacao(num1, num2)
  elif operacao == 'divisao':
    resultado = divisao(num1, num2)
  else:
    resultado = "Operação inválida!"
  print(round(resultado, 2))

calcular()
  
