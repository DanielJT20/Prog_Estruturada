
"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC7 
"""

salario = float(input())
reajuste = 0

if(salario <= 400.00):
    reajuste = 15
elif(salario <= 800.00):
    reajuste = 12
elif(salario <= 1200.00):
    reajuste = 10
elif(salario <= 2000.00):
    reajuste = 7
else:
    reajuste = 4

print(f'Novo salario: {salario * (1 + reajuste/100):.2f}')
print(f'Reajuste ganho: {salario * reajuste/100:.2f}')
print(f'Em percentual: {reajuste} %')


"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 2 - AC7 
"""

pares = 0

for _ in range(5):
    numero = int(input())

    pares += not (numero % 2)

print(f'{pares} valores pares')


"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 3 - AC7 
"""

X = int(input())
Y = int(input())

if (X > Y):
    X, Y = Y, X

soma = 0
for i in range(X, Y + 1):
    if(i % 13 == 0):
        continue
    soma += i

print(soma)


"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 4 - AC7 
"""

V = int(input())

produto = V
for i in range(10):
    print(f'N[{i}] = {produto}')
    produto <<= 1


"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 5 - AC7 
"""

N = int(input())
X = [int(x) for x in input().strip().split()]

menor_valor = X[0]
posicao = 0

for i in range(1, len(X)):
    valor = X[i]

    if(valor < menor_valor):
        menor_valor = valor
        posicao = i

print(f'Menor valor: {menor_valor}')
print(f'Posicao: {posicao}')


"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 6 - AC7 
"""

C = int(input())
T = input()

soma = 0.0
for _ in range(12):
    for j in range(12):
        numero = float(input())

        if(j == C):
            soma += numero

if(T == 'S'):
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')
    
    
"""
Programação Estruturada
2024.1
17/04/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 7 - AC7 
""" 

def ordena_tamanho(strings):
    return sorted(strings, key=lambda x: len(x), reverse = True)

def main():
    num_casos_teste = int(input())
    
    for _ in range(num_casos_teste):
        conjunto_strings = input().split()
        
        if len(conjunto_strings) < 1 or len(conjunto_strings) > 50:
            print("Número de Strings por caso de teste deve ser menor/igual a 1, até maior/igual a 50")
            return
        
        for string in conjunto_strings:
            if len(string) < 1 or len(string) > 50:
                print("Número de caracteres da string deve ser menor/igual a 1, até maior/igual a 50")
                return
            
        conjunto_ordenado = ordena_tamanho(conjunto_strings)
        print(" ".join(conjunto_ordenado))
if __name__ == "__main__":
    main()
