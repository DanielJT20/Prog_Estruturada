
"""
Programação Estruturada
2024.1
26/03/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercícios AC - extra
"""

# while True:
#     try:
#         cont = 0
#         expr = input("Insira sua Expressão: ")
#         for i in range(len(expr)):
#             if expr[i] == "(":
#                 cont += 1
#             elif expr[i] == ")":
#                 cont -= 1
#             if cont < 0:
#                 break
#         if cont != 0:
#             print("Incorrect")
#         else:
#             print("Correct")
#     except EOFError:
#         break

# def nome_ordena (nomes): 
#     for i in range (qtd (len (nomes))):
   
#     print (nome_ordena (nomes)) 



# par = []
# impar = []
# linha = int(input())

# while linha > 0:
#     num = int(input())
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
#     linha -= 1
    
# par.sort()
# impar.sort(reverse=True)
    
# lista = []
    
# for num in par:
#     lista.append(num)
# for num in impar:
#     lista.append(num)
# for num in lista:
#         print(num)

# linha = int(input())
# for i in range(linha):
#     names = input().split()
#     names= sorted(set(names))
#     print(" ".join(str(j) for j in names ))

linha = int(input())
for i in range(linha):
    names = input().split()
    names= sorted(set(names))

lista = []
lista.append(names)


print(lista)