"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 1 - AC8 
"""

def MDC(a, b):
    return a if b == 0 else MDC(b, a % b)


N = int(input())

for _ in range(N):
    F1, F2 = [int(x) for x in input().strip().split(' ')]
    print(MDC(F1, F2))


"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 2 - AC8 
"""

while True:
    try:
        [X1, Y1, X2, Y2] = [int(x) for x in input().strip().split(' ')]

        if(not X1 and not Y1 and not X2 and not Y2):
            break

        if(X1 == X2 and Y1 == Y2):
            print(0)
        elif(X1 == X2 or Y1 == Y2 or abs(X1 - X2) == abs(Y1 - Y2)):
            print(1)
        else:
            print(2)
    except EOFError:
        break
     
"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 3 - AC8 
"""

F = [0 for _ in range(21)]
F[0] = 1


def Fatorial(n):
    if(F[n] == 0):
        F[n] = n * Fatorial(n - 1)
    return F[n]


while True:
    try:
        M, N = [int(x) for x in input().strip().split(' ')]

        print(Fatorial(M) + Fatorial(N))
    except EOFError:
        break
    
"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 4 - AC8 
"""

import math

N = int(input())

for _ in range(N):
    C = float(input())

    print(f'{math.ceil(math.log2(C))} dias')

"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 5 - AC8 
"""

n = int(input())

frequencias = [0 for _ in range(2001)]

for _ in range(n):
    x = int(input())
    
    frequencias[x] += 1

for i in range(1, 2001):
    if(frequencias[i] > 0):
        print(f"{i} aparece {frequencias[i]} vez(es)")

"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 6 - AC8 
"""

import math

numeroDeCasos = int(input())

for i in range(numeroDeCasos):

    number = int(input())
    isPrime = True

    if number % 2 == 0 and number > 2:

        isPrime = False
    else:

        root = int(math.sqrt(number))

        for j in range(3, root + 1, 2):

            if number % j == 0:

                isPrime = False
                break
    
    if isPrime:

        print("Prime")
    else:

        print("Not Prime")
        
"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 7 - AC8 
"""

while True:
    try:
        N = int(input())

        R = [int(x) for x in input().strip().split(' ')]

        joao = sum(R)
        maria = N - joao

        print(f"Mary won {maria} times and John won {joao} times")
    except EOFError:
        break

"""
Programação Estruturada
2024.1
03/05/2024

Daniel de Jesus Teixeira
Ciência de Dados e IA, turma: 8001

Exercício 8 - AC8 
"""

def r(x, y):
    return (3 * x) * (3 * x) + y * y


def b(x, y):
    return 2 * x * x + (5 * y) * (5 * y)


def c(x, y):
    return -100 * x + y * y * y


N = int(input())

for _ in range(N):
    x, y = [int(x) for x in input().strip().split(' ')]

    rafael = r(x, y)
    beto = b(x, y)
    carlos = c(x, y)

    if(rafael > beto and rafael > carlos):
        print('Rafael ganhou')
    elif(beto > carlos):
        print('Beto ganhou')
    else:
        print('Carlos ganhou')

